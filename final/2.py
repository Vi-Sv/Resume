import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_PATH = "arial.ttf" 

if not os.path.exists(FONT_PATH):
    win_font = "C:\\Windows\\Fonts\\arial.ttf"
    if os.path.exists(win_font):
        FONT_PATH = win_font
    else:
        raise FileNotFoundError(f"Файл шрифта {FONT_PATH} не найден. Поместите arial.ttf в папку со скриптом.")

pdfmetrics.registerFont(TTFont('Arial', FONT_PATH))

def create_resume(output_filename="resume.pdf"):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    name_style = ParagraphStyle(
        'NameStyle',
        fontName='Arial',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A2B4C"),
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        fontName='Arial',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2E5B88"),
        spaceAfter=4
    )
    
    contacts_style = ParagraphStyle(
        'ContactsStyle',
        fontName='Arial',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#555555"),
        spaceAfter=2
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitleStyle',
        fontName='Arial',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#1A2B4C"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    
    job_title_style = ParagraphStyle(
        'JobTitleStyle',
        fontName='Arial',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#222222"),
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        fontName='Arial',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#333333"),
        spaceAfter=3
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )

    story = []

    # Заголовок и контакты
    story.append(Paragraph("Свистин Виктор Андреевич", name_style))
    story.append(Paragraph("<b>Целевая должность:</b> Младший ETL-разработчик / Начинающий Дата-инженер / Аналитик данных / Операционный аналитик", subtitle_style))
    story.append(Paragraph("<b>Локация:</b> Саратов, Россия (Удаленная работа / Гибрид / Релокация)", contacts_style))
    story.append(Paragraph("<b>Контакты:</b> +7 (962) 625-80-06 | svistin64.v@gmail.com", contacts_style))
    
    def add_section_divider(title):
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2E5B88"), spaceBefore=4, spaceAfter=4))
        story.append(Paragraph(f"<b>{title.upper()}</b>", section_title_style))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCCC"), spaceBefore=2, spaceAfter=6))

    # Технические навыки
    add_section_divider("Технические навыки")
    story.append(Paragraph("<b>Базы данных и SQL:</b> PostgreSQL, DBeaver, DDL, DML.", body_style))
    story.append(Paragraph("<b>Языки и библиотеки:</b> Python (Pandas, NumPy), VBA.", body_style))
    story.append(Paragraph("<b>Инструменты и BI:</b> Microsoft Power BI, Excel.", body_style))
    story.append(Paragraph("<b>Дополнительно:</b> Понимание концепций ETL/ELT, проектирование реляционных структур данных, валидация и очистка данных.", body_style))
    
    # Опыт разработки и пет-проекты
    add_section_divider("Опыт разработки и пет-проекты")
    story.append(Paragraph("<b>Развернул изолированную девелоперскую среду для симуляции классического ELT/ETL-контура (Jupyter Notebooks в VS Code, PostgreSQL, DBeaver) . (Август 2026 г.)</b>", job_title_style))
    story.append(Paragraph("<b>Стек:</b> Python (Pandas, NumPy), PostgreSQL, Power BI, DBeaver.", body_style))
    story.append(Paragraph("• Разработал девелоперский ETL/ELT-контур. На Python сгенерировал синтетический массив транзакций с аномалиями для тестирования отказоустойчивости.", bullet_style))
    story.append(Paragraph("• Спроектировал DDL-структуру таблиц-приемников в PostgreSQL. Написал SQL-скрипты очистки, приведения форматов и агрегации данных в витринах .", bullet_style))
    story.append(Paragraph("• Подключил СУБД к Power BI и настроил интерактивный дашборд.", bullet_style))
    
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>SQL-практика (Самостоятельное обучение)</b>", job_title_style))
    story.append(Paragraph("• Реализовал и протестировал чистые SQL-запросы для 33 практических бизнес-сценариев.", bullet_style))

    # Опыт работы
    add_section_divider("Опыт работы")
    
    story.append(Paragraph("<b>ООО «ФракДжет-Строй» (Строительный инжиниринг)</b>", job_title_style))
    story.append(Paragraph("<b>Период:</b> Февраль 2026 г. — по настоящее время", body_style))
    story.append(Paragraph("<b>Позиция:</b> Инженер ПЭО (аналитический отдел) / Должность: Инженер ПТО II категории", body_style))
    add_section_divider("Обязанности:")
    story.append(Paragraph("• Расчет и актуализация графиков производства работ (ГПР). Краткосрочное и среднесрочное планирование на основе многофакторного анализа: фактического распределения ресурсов, темпов поставки материалов и версий рабочей документации (РД).", bullet_style))
    story.append(Paragraph("• Ежедневный сбор, учет и верификация оперативной отчетности о выполнении работ, затратах человек-часов и машино-часов на объекте строительства.", bullet_style))
    story.append(Paragraph("• Аудит входящей отчетности, выявлял логические ошибки, расхождения и системные коллизии в первичных данных.", bullet_style))
    add_section_divider("Достижения:")
    story.append(Paragraph("• <b>Проектирование ETL:</b> Разработал алгоритмы автоматического сбора, валидации и трансформации технологических данных, преобразовав разрозненные выгрузки в структурированные плоские таблицы для аналитики.", bullet_style))
    story.append(Paragraph("• <b>Автоматизация:</b> Написал комплекс VBA-скриптов для автоматизации сводной отчетности, исключив ручной ввод и сократив время формирования документов.", bullet_style))
    story.append(Paragraph("• <b>Управление данными:</b> Проектировал и поддерживал реляционные структуры данных для оперативной отчетности, оптимизировал схемы приемки и хранения данных.", bullet_style))


    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Период:</b> Февраль 2024 г. — февраль 2026 г.", body_style))
    story.append(Paragraph("<b>Позиция:</b> Инженер ПТО / Должность: Инженер ПТО II категории", body_style))
    add_section_divider("Обязанности:")
    story.append(Paragraph("• <b>Контроль данных:</b> Вел и верифицировал сквозные технологические базы данных и реестры.", bullet_style))
    story.append(Paragraph("• <b>Валидация:</b> Осуществлял перекрестную сверку и обеспечивал логическую увязку данных между независимыми информационными источниками.", bullet_style))

    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Период:</b> Апрель 2023 г. — февраль 2024 г.", body_style))
    story.append(Paragraph("<b>Позиция:</b> Координатор ресурсов", body_style))
    add_section_divider("Достижения:")
    story.append(Paragraph("• <b>Оптимизация:</b> Провел аудит унаследованных учетных таблиц Excel, ликвидировал формульные ошибки и оптимизировал интерфейс ввода данных. За счет личной инициативы, алгоритмического подхода к задачам и автоматизации рутинных процессов, был переведен с линейной рабочей позиции (стропальщик) на инженерно-управленческую должность в течение первых 8 месяцев работы.", bullet_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>КЦ «ТЕЛЕКОНТАКТ» (Аутсорсинговый контакт-центр)</b>", job_title_style))
    story.append(Paragraph("<b>Период:</b> Декабрь 2022 г. — Март 2023 г. | <b>Позиция:</b> Менеджер по маршрутизации и валидации данных", body_style))
    story.append(Paragraph("• <b>Анализ данных:</b> Проводил аудит неструктурированных запросов, сопоставлял потребности клиентов с техническими параметрами базы данных. Выполнял задачи в условиях высокой интенсивности под непрерывным автоматизированным контролем ключевых метрик эффективности (SLA) и строгого программного регламента учета рабочего времени.", bullet_style))

    # Образование и сертификаты
    add_section_divider("Образование и сертификаты")
    story.append(Paragraph("• <b>ППК СГТУ им. Гагарина Ю.А. (2017 — 2021 гг.)</b> | Специальность: 09.02.02 «Компьютерные сети», Диплом с отличием.", bullet_style))
    story.append(Paragraph("• <b>СГТУ им. Гагарина Ю.А. (2023 г. — н.в., в процессе)</b> | Высшее техническое образование.", bullet_style))
    story.append(Paragraph("• <b>Сертификат:</b> «SQL» (Stepik, №3270511).", bullet_style))
    story.append(Paragraph("• <b>Сертификат:</b> «Python для анализа данных» (Stepik, №3274127).", bullet_style))

    # Дополнительная информация
    add_section_divider("Дополнительная информация")
    story.append(Paragraph("• <b>Военная служба:</b> Срочная служба в ВС РФ (2021 — 2022 гг.).", bullet_style))

    doc.build(story)

if __name__ == "__main__":
    create_resume("Svistin_Victor_Full_Resume.pdf")
