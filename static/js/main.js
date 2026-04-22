/* ============================================================
   PORTFOLIO JS — Animaciones e interacciones
   ============================================================ */

(function () {
    'use strict';

    /* ---------- Page loader ---------- */
    window.addEventListener('load', function () {
        const loader = document.querySelector('.page-loader');
        if (loader) {
            setTimeout(() => loader.classList.add('done'), 400);
        }
    });

    document.addEventListener('DOMContentLoaded', function () {

        /* ---------- Scroll progress bar ---------- */
        const progressBar = document.querySelector('.scroll-progress');
        if (progressBar) {
            const updateProgress = () => {
                const scrollTop = window.scrollY;
                const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
                progressBar.style.width = pct + '%';
            };
            window.addEventListener('scroll', updateProgress, { passive: true });
            updateProgress();
        }

        /* ---------- Navbar mobile toggle ---------- */
        const navToggle = document.querySelector('.nav-toggle');
        const navLinks = document.querySelector('.nav-links');
        if (navToggle && navLinks) {
            navToggle.addEventListener('click', () => {
                navLinks.classList.toggle('open');
            });
            // Cerrar al clickear un link
            navLinks.querySelectorAll('a').forEach(a => {
                a.addEventListener('click', () => navLinks.classList.remove('open'));
            });
        }

        /* ---------- Active nav link ---------- */
        const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
        document.querySelectorAll('.nav-links a').forEach(a => {
            const href = a.getAttribute('href').replace(/\/$/, '') || '/';
            if (href === currentPath) a.classList.add('active');
        });

        /* ---------- Scroll reveal with IntersectionObserver ---------- */
        const revealEls = document.querySelectorAll('.reveal');
        if (revealEls.length && 'IntersectionObserver' in window) {
            const io = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        io.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

            revealEls.forEach(el => io.observe(el));
        } else {
            revealEls.forEach(el => el.classList.add('visible'));
        }

        /* ---------- Typewriter effect ---------- */
        const typedEl = document.querySelector('[data-typed]');
        if (typedEl) {
            let words = [];
            try {
                words = JSON.parse(typedEl.getAttribute('data-typed'));
            } catch (e) { words = [typedEl.getAttribute('data-typed')]; }

            if (words.length) {
                let wi = 0, ci = 0, deleting = false;
                const tick = () => {
                    const current = words[wi];
                    if (!deleting) {
                        typedEl.textContent = current.slice(0, ++ci);
                        if (ci === current.length) {
                            deleting = true;
                            setTimeout(tick, 1800);
                            return;
                        }
                    } else {
                        typedEl.textContent = current.slice(0, --ci);
                        if (ci === 0) {
                            deleting = false;
                            wi = (wi + 1) % words.length;
                        }
                    }
                    setTimeout(tick, deleting ? 40 : 80);
                };
                tick();
            }
        }

        /* ---------- Count up for stats ---------- */
        const counters = document.querySelectorAll('[data-count]');
        if (counters.length && 'IntersectionObserver' in window) {
            const countIo = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const el = entry.target;
                        const target = parseInt(el.getAttribute('data-count'), 10) || 0;
                        const duration = 1400;
                        const startTime = performance.now();
                        const tick = (now) => {
                            const progress = Math.min((now - startTime) / duration, 1);
                            const eased = 1 - Math.pow(1 - progress, 3);
                            el.textContent = Math.round(target * eased);
                            if (progress < 1) requestAnimationFrame(tick);
                            else el.textContent = target;
                        };
                        requestAnimationFrame(tick);
                        countIo.unobserve(el);
                    }
                });
            }, { threshold: 0.5 });
            counters.forEach(c => countIo.observe(c));
        }

        /* ---------- Back to top ---------- */
        const backTop = document.querySelector('.back-top');
        if (backTop) {
            const toggleBackTop = () => {
                backTop.classList.toggle('visible', window.scrollY > 400);
            };
            window.addEventListener('scroll', toggleBackTop, { passive: true });
            backTop.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        /* ---------- Copy to clipboard ---------- */
        document.querySelectorAll('[data-copy]').forEach(btn => {
            btn.addEventListener('click', async () => {
                const text = btn.getAttribute('data-copy');
                try {
                    await navigator.clipboard.writeText(text);
                    const orig = btn.textContent;
                    btn.textContent = '✓ copiado';
                    btn.style.color = 'var(--accent)';
                    btn.style.borderColor = 'var(--accent)';
                    setTimeout(() => {
                        btn.textContent = orig;
                        btn.style.color = '';
                        btn.style.borderColor = '';
                    }, 1600);
                } catch (e) {
                    console.warn('No se pudo copiar:', e);
                }
            });
        });

        /* ---------- Contact form client-side validation ---------- */
        const form = document.getElementById('contact-form');
        if (form) {
            const showError = (input, message) => {
                input.classList.add('error');
                input.classList.remove('success');
                const errEl = input.parentElement.querySelector('.field-error');
                if (errEl) {
                    errEl.textContent = message;
                    errEl.classList.add('visible');
                }
            };
            const clearError = (input) => {
                input.classList.remove('error');
                input.classList.add('success');
                const errEl = input.parentElement.querySelector('.field-error');
                if (errEl) errEl.classList.remove('visible');
            };

            form.addEventListener('submit', (e) => {
                let ok = true;
                const nombre = form.querySelector('[name="nombre"]');
                const email = form.querySelector('[name="email"]');
                const mensaje = form.querySelector('[name="mensaje"]');

                if (!nombre.value.trim() || nombre.value.trim().length < 2) {
                    showError(nombre, 'Ingresá tu nombre (mínimo 2 caracteres)');
                    ok = false;
                } else clearError(nombre);

                const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRe.test(email.value.trim())) {
                    showError(email, 'Ingresá un email válido');
                    ok = false;
                } else clearError(email);

                if (!mensaje.value.trim() || mensaje.value.trim().length < 10) {
                    showError(mensaje, 'El mensaje debe tener al menos 10 caracteres');
                    ok = false;
                } else clearError(mensaje);

                if (!ok) {
                    e.preventDefault();
                    form.querySelector('.error')?.focus();
                }
            });

            // Char counter
            const textarea = form.querySelector('[name="mensaje"]');
            const counter = form.querySelector('[data-counter-for="mensaje"]');
            if (textarea && counter) {
                const max = parseInt(textarea.getAttribute('maxlength'), 10) || 500;
                const update = () => {
                    counter.textContent = `${textarea.value.length} / ${max}`;
                };
                textarea.addEventListener('input', update);
                update();
            }
        }

        /* ---------- Auto-dismiss alerts ---------- */
        document.querySelectorAll('.alert-dev[data-auto-dismiss]').forEach(el => {
            setTimeout(() => {
                el.style.transition = 'opacity 0.5s, transform 0.5s';
                el.style.opacity = '0';
                el.style.transform = 'translateY(-10px)';
                setTimeout(() => el.remove(), 500);
            }, 5000);
        });

        /* ---------- Parallax sutil en hero visual ---------- */
        const heroVisual = document.querySelector('.terminal-card');
        if (heroVisual && window.innerWidth > 768) {
            document.addEventListener('mousemove', (e) => {
                const x = (e.clientX / window.innerWidth - 0.5) * 6;
                const y = (e.clientY / window.innerHeight - 0.5) * 6;
                heroVisual.style.transform = `translate(${x}px, ${y}px)`;
            });
        }

    });
})();
