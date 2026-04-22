"""
Carga las traducciones al inglés para los proyectos y experiencias
que vienen precargados en la DB.

Uso:
    python manage.py shell < load_en_translations.py

Se puede ejecutar múltiples veces sin problemas (sobrescribe los campos _en).
"""

from app_portfolio.models import Proyecto, Experiencia


# =============================================================================
# PROYECTOS
# =============================================================================
proyectos_en = {
    "gomitas.sf - Gestión de Emprendimiento & Growth": {
        "titulo_en": "gomitas.sf — Entrepreneurship & Growth Management",
        "tecnologia_en": "Meta Ads, ManyChats, Google Spreadsheets",
        "descripcion_en": (
            "Built a digital ecosystem to scale a local candy-stand business. "
            "The project includes automation of a \"Unified Inbox\" for customer "
            "support, design of stock control dashboards and the execution of "
            "Meta Ads campaigns that drove both organic and paid growth of the "
            "brand from zero in Santa Fe City."
        ),
    },
    "Data Infrastructure & Business Intelligence": {
        "titulo_en": "Data Infrastructure & Business Intelligence",
        "tecnologia_en": "MySQL, Power BI, SQL Stored Procedures, ETL",
        "descripcion_en": (
            "Transformation of an informal business operation into a professional BI system.\n"
            "• Data Engineering: Design of a MySQL relational DB (15 tables) with audit and business-logic layers.\n"
            "• Automation: Triggers, Stored Procedures and Functions for stock control, logistic costs and ROI calculation.\n"
            "• Analytics: Power BI dashboards for monitoring sales KPIs, geographic reach in Santa Fe and staff efficiency."
        ),
    },
    "Diseño de Infraestructura de Redes de Fibra Óptica (FTTH)": {
        "titulo_en": "Fiber Optic Network Infrastructure Design (FTTH)",
        "tecnologia_en": "AutoCAD, Google Earth Pro, GIS",
        "descripcion_en": (
            "Detailed design and planimetry for fiber optic network rollouts in urban areas of Santa Fe.\n"
            "• Detailed Engineering: Precise technical plans for aerial and underground (FTTH) cabling deployment.\n"
            "• Feasibility Analysis: Digitization of field surveys and geospatial data to optimize network routes and distribution points.\n"
            "• Documentation: Splice diagrams and technical packages ready for execution."
        ),
    },
    "Bienestar Digital & Salud Mental - Data Analytics": {
        "titulo_en": "Digital Well-being & Mental Health — Data Analytics",
        "tecnologia_en": "Power BI, DAX, Star Schema Data Modeling, ETL",
        "descripcion_en": (
            "Comprehensive analysis of the relationship between technology consumption and psychological well-being over a 500-record sample.\n"
            "• Architecture: Star-schema data model in Power BI to optimize processing.\n"
            "• Analysis: Impact assessment of screen time on critical variables such as stress levels and sleep quality using DAX measures.\n"
            "• Visualization: Interactive 5-view dashboard with demographic segmentation."
        ),
    },
    "Structural Engine Desktop": {
        "titulo_en": "Structural Engine Desktop",
        "tecnologia_en": "C++, wxWidgets, wxFormBuilder, Zinjai IDE",
        "descripcion_en": (
            "Technical software for the sizing of reinforced-concrete sections subject to simple bending.\n"
            "• Structural Calculation: Automatic determination of required steel area and verification of minimum reinforcement ratios under current codes.\n"
            "• Development: OOP-based C++ logic ensuring precision in processing bending moments and material properties.\n"
            "• GUI: Interface designed with wxFormBuilder (wxWidgets) inside Zinjai for a technical user experience."
        ),
    },
    "Full-Stack Portfolio: Sistema de Gestión de Contenido Dinámico": {
        "titulo_en": "Full-Stack Portfolio: Dynamic Content Management System",
        "tecnologia_en": "Python, Django, Bootstrap 5, SQLite, Architecture",
        "descripcion_en": (
            "Full web platform for centralizing personal branding and managing professional trajectory.\n"
            "• Architecture: Robust Django backend using the Model-View-Template pattern.\n"
            "• Dynamic Content: Custom CMS through the admin panel for real-time updates of projects and timeline.\n"
            "• Interactivity: Contact form with DB persistence and a responsive, optimized design."
        ),
    },
}


# =============================================================================
# EXPERIENCIAS
# =============================================================================
experiencias_en = {
    ("AI Training Software Engineer / AI Code Specialist", "Outlier AI"): {
        "cargo_en": "AI Training Software Engineer / AI Code Specialist",
        "empresa_en": "Outlier AI",
        "descripcion_en": (
            "Development of scripts and software solutions for generative-AI training projects.\n\n"
            "Design of complex technical \"prompts\" to challenge the model's capabilities in languages such as C++ and Python.\n\n"
            "Code review and QA on technical responses, ensuring that code is functional and secure.\n\n"
            "Detailed documentation of logical and execution errors for the model's feedback loop."
        ),
    },
    ("Proyectista CAD - Redes de Fibra Óptica", "Internet Services SA"): {
        "cargo_en": "CAD Designer — Fiber Optic Networks",
        "empresa_en": "Internet Services SA",
        "descripcion_en": (
            "In this role at Internet Services, I'm responsible for the technical documentation needed to expand the connectivity network across the Santa Fe region. My work combines technical precision with urban-infrastructure analysis:\n\n"
            "Documentation Precision: Development of detailed plans that serve as a critical guide for on-site installation crews.\n\n"
            "Process Optimization: Integration of technical knowledge to streamline the handoff from manual field surveys to digital plans."
        ),
    },
    ("Diplomatura en Data Science", "Coderhouse"): {
        "cargo_en": "Data Science Diploma",
        "empresa_en": "Coderhouse",
        "descripcion_en": (
            "Intensive 15-month program focused on the data lifecycle and predictive models.\n\n"
            "• Technical Stack: Python (Pandas, NumPy), SQL and Advanced Excel.\n"
            "• BI & Visualization: Power BI (DAX), Tableau and Looker Studio for KPI monitoring.\n"
            "• AI & Machine Learning: Exploratory Data Analysis (EDA), Prompt Engineering (OpenAI API) and Natural Language Processing (NLP).\n"
            "• Methodologies: Agile management with Scrum."
        ),
    },
    ("Estudiante de Ingeniería Informática", "UNL – Universidad Nacional del Litoral"): {
        "cargo_en": "Computer Engineering Student",
        "empresa_en": "UNL — Universidad Nacional del Litoral",
        "descripcion_en": (
            "Computer Engineering studies focused on algorithms, OOP and systems design.\n"
            "• Technical Development: Efficient solutions through Object-Oriented Programming and data structures.\n"
            "• Data Management: Design and normalization of relational databases with SQL.\n"
            "• Milestone: Technical cycle completed toward the Applied Computing Analyst degree. Solid knowledge of SDLC, computational logic and requirements engineering."
        ),
    },
    ("Co - Fundador", "Gomitas.sf"): {
        "cargo_en": "Co-Founder",
        "empresa_en": "Gomitas.sf",
        "descripcion_en": (
            "Co-founder responsible for leading business growth from scratch.\n"
            "• Marketing & Growth: Design and execution of Meta Ads campaigns, achieving brand scaling and customer acquisition.\n"
            "• Process Management: Systems implementation for stock control, supplier administration and end-to-end event logistics.\n"
            "• Strategy: Optimization of the sales funnel and customer support through the integration of digital management tools."
        ),
    },
}


# =============================================================================
# APLICAR
# =============================================================================
print("\n=== Cargando traducciones de Proyectos ===")
updated_p = 0
for p in Proyecto.objects.all():
    if p.titulo in proyectos_en:
        data = proyectos_en[p.titulo]
        p.titulo_en = data["titulo_en"]
        p.descripcion_en = data["descripcion_en"]
        p.tecnologia_en = data["tecnologia_en"]
        p.save()
        print(f"  ✓ {p.titulo}")
        updated_p += 1
    else:
        print(f"  ✗ (sin traducción): {p.titulo}")

print(f"\n  Proyectos actualizados: {updated_p}/{Proyecto.objects.count()}")

print("\n=== Cargando traducciones de Experiencias ===")
updated_e = 0
for e in Experiencia.objects.all():
    key = (e.cargo, e.empresa)
    if key in experiencias_en:
        data = experiencias_en[key]
        e.cargo_en = data["cargo_en"]
        e.empresa_en = data["empresa_en"]
        e.descripcion_en = data["descripcion_en"]
        e.save()
        print(f"  ✓ {e.cargo} @ {e.empresa}")
        updated_e += 1
    else:
        print(f"  ✗ (sin traducción): {e.cargo} @ {e.empresa}")

print(f"\n  Experiencias actualizadas: {updated_e}/{Experiencia.objects.count()}")
print("\n✓ Listo.\n")
