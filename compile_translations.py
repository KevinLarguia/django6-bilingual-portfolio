"""
Compila archivos .po a .mo (formato gettext binario).

Uso:
    python compile_translations.py

Busca todos los .po bajo locale/ y genera los .mo correspondientes.
Implementación pure-Python - no depende de gettext del sistema, útil en Windows.
"""

import ast
import re
import struct
import sys
from pathlib import Path


def parse_string(line_after_keyword):
    """Dada la parte de una línea .po que contiene un string entre comillas,
    devuelve los bytes decodificados."""
    m = re.search(r'"(.*)"\s*$', line_after_keyword, re.DOTALL)
    if not m:
        return b""
    try:
        return ast.literal_eval('"' + m.group(1) + '"').encode("utf-8")
    except Exception:
        return b""


def compile_po(po_path, mo_path):
    """Parsea un .po y genera su .mo correspondiente."""
    messages = {}

    msgid = b""
    msgstr = b""
    msgid_plural = b""
    msgctxt = None
    msgstr_plural = {}
    fuzzy = False
    last_key = None
    entry_started = False

    def make_flush():
        def flush():
            nonlocal messages
            if not entry_started or fuzzy:
                return
            if msgid_plural and msgstr_plural:
                key = msgid + b"\x00" + msgid_plural
                parts = [msgstr_plural.get(i, b"") for i in sorted(msgstr_plural.keys())]
                val = b"\x00".join(parts)
            else:
                key = msgid
                val = msgstr
            if msgctxt is not None:
                key = msgctxt + b"\x04" + key
            if key or val:
                messages[key] = val
        return flush

    with open(po_path, "rb") as f:
        lines = f.read().splitlines()

    for raw in lines:
        line = raw.decode("utf-8").rstrip()
        stripped = line.strip()

        if not stripped:
            # Flush manual
            if entry_started and not fuzzy:
                if msgid_plural and msgstr_plural:
                    key = msgid + b"\x00" + msgid_plural
                    parts = [msgstr_plural.get(i, b"") for i in sorted(msgstr_plural.keys())]
                    val = b"\x00".join(parts)
                else:
                    key = msgid
                    val = msgstr
                if msgctxt is not None:
                    key = msgctxt + b"\x04" + key
                if key or val:
                    messages[key] = val
            msgid = b""
            msgstr = b""
            msgid_plural = b""
            msgctxt = None
            msgstr_plural = {}
            fuzzy = False
            last_key = None
            entry_started = False
            continue

        if stripped.startswith("#"):
            if stripped.startswith("#,") and "fuzzy" in stripped:
                fuzzy = True
            continue

        if stripped.startswith("msgctxt "):
            msgctxt = parse_string(stripped[7:].strip())
            last_key = "msgctxt"
            entry_started = True
        elif stripped.startswith("msgid_plural "):
            msgid_plural = parse_string(stripped[12:].strip())
            last_key = "msgid_plural"
        elif stripped.startswith("msgid "):
            msgid = parse_string(stripped[5:].strip())
            last_key = "msgid"
            entry_started = True
        elif stripped.startswith("msgstr["):
            m = re.match(r"^msgstr\[(\d+)\]\s*(.*)$", stripped)
            if m:
                idx = int(m.group(1))
                msgstr_plural[idx] = parse_string(m.group(2).strip())
                last_key = f"msgstr[{idx}]"
        elif stripped.startswith("msgstr "):
            msgstr = parse_string(stripped[6:].strip())
            last_key = "msgstr"
        elif stripped.startswith('"'):
            continuation = parse_string(stripped)
            if last_key == "msgid":
                msgid += continuation
            elif last_key == "msgstr":
                msgstr += continuation
            elif last_key == "msgid_plural":
                msgid_plural += continuation
            elif last_key == "msgctxt":
                msgctxt = (msgctxt or b"") + continuation
            elif last_key and last_key.startswith("msgstr["):
                m = re.match(r"msgstr\[(\d+)\]", last_key)
                if m:
                    idx = int(m.group(1))
                    msgstr_plural[idx] = msgstr_plural.get(idx, b"") + continuation

    # Última entrada
    if entry_started and not fuzzy:
        if msgid_plural and msgstr_plural:
            key = msgid + b"\x00" + msgid_plural
            parts = [msgstr_plural.get(i, b"") for i in sorted(msgstr_plural.keys())]
            val = b"\x00".join(parts)
        else:
            key = msgid
            val = msgstr
        if msgctxt is not None:
            key = msgctxt + b"\x04" + key
        if key or val:
            messages[key] = val

    # Generar binario .mo
    keys = sorted(messages.keys())
    offsets = []
    ids = b""
    strs = b""
    for key in keys:
        value = messages[key]
        offsets.append((len(ids), len(key), len(strs), len(value)))
        ids += key + b"\x00"
        strs += value + b"\x00"

    keystart = 7 * 4 + 16 * len(keys)
    valuestart = keystart + len(ids)
    koffsets = []
    voffsets = []
    for o1, l1, o2, l2 in offsets:
        koffsets += [l1, o1 + keystart]
        voffsets += [l2, o2 + valuestart]
    offsets_flat = koffsets + voffsets

    output = struct.pack(
        "Iiiiiii",
        0x950412DE, 0, len(keys),
        7 * 4, 7 * 4 + len(keys) * 8,
        0, 0,
    )
    output += struct.pack("i" * len(offsets_flat), *offsets_flat)
    output += ids
    output += strs

    with open(mo_path, "wb") as f:
        f.write(output)
    return len(messages)


def main():
    locale_dir = Path(__file__).parent / "locale"
    if not locale_dir.is_dir():
        print(f"No se encontró la carpeta locale/ en {locale_dir}")
        sys.exit(1)

    total = 0
    for po_file in sorted(locale_dir.rglob("*.po")):
        mo_file = po_file.with_suffix(".mo")
        count = compile_po(po_file, mo_file)
        print(f"  [{count:3d} msgs] {po_file.relative_to(locale_dir.parent)} -> {mo_file.relative_to(locale_dir.parent)}")
        total += count

    print(f"\n✓ Compilados {total} mensajes en total.")


if __name__ == "__main__":
    main()
