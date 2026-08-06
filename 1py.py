import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_resume():
    pdf_filename = "Resume_Svistin_Victor.pdf"
    
    # Настройка документа со сбалансированными отступами
    doc = SimpleDocTemplate(
        pdf_filename, 
        pagesize=letter,
        rightMargin=45, leftMargin=45, 
        topMargin=40, bottomMargin=40
    )
    
    # --- НАСТРОЙКА КИРИЛЛИЦЫ (Windows Arial) ---
    font_path = "C:\\Windows\\Fonts\\arial.ttf"
    if os.path.exists(font_path):
        pdfmetrics.registerFont(TTFont('Arial', font_path))
        font_name = 'Arial'
    else:
        font_name = 'Helvetica'
        print("Внимание: Системный шрифт Arial не найден. Проверьте путь.")

    styles = getSampleStyleSheet()
    
    # Цветовая схема Tech & Corporate
    PRIMARY_COLOR = colors.HexColor("#1A365D")  # Глубокий синий
    TEXT_COLOR = colors.HexColor("#2D3748")     # Графитовый серый
    ACCENT_COLOR = colors.HexColor("#4A5568")   # Стальной серый
    
    # Стили текста
    name_style = ParagraphStyle(
        'CV_Name', parent=styles['Normal'], fontName=font_name, fontSize=20,
        leading=24, textColor=PRIMARY_COLOR
    )
    
    dob_style = ParagraphStyle(
        'CV_Dob', parent=styles['Normal'], fontName=font_name, fontSize=10,
        leading=14, textColor=ACCENT_COLOR, spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'CV_SubTitle', parent=styles['Normal'], fontName=font_name, fontSize=11,
        leading=15, textColor=PRIMARY_COLOR, spaceAfter=12
    )
    
    h1_style = ParagraphStyle(
        'CV_H1', parent=styles['Normal'], fontName=font_name, fontSize=12,
        leading=15, textColor=PRIMARY_COLOR, spaceBefore=10, spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'CV_Body', parent=styles['Normal'], fontName=font_name, fontSize=9.5,
        leading=14, textColor=TEXT_COLOR, spaceAfter=3
    )
    
    right_body_style = ParagraphStyle(
        'CV_RightBody', parent=body_style, alignment=2, textColor=ACCENT_COLOR
    )

    story = []

    def add_section_header(title):
        """Инженерный разделитель блоков с линией"""
        t = Table([[Paragraph(f"<b>{title.upper()}</b>", h1_style)]], colWidths=[522])
        t.setStyle(TableStyle([
            ('LINEBELOW', (0,0), (-1,-1), 1, PRIMARY_COLOR),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('TOPPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t)
        story.append(Spacer(1, 4))
    # --- ЧАСТЬ 1: ШАПКА И КОНТАКТЫ ---
    story.append(Paragraph("<b>Свистин Виктор Андреевич</b>", name_style))
    story.append(Paragraph("Дата рождения: 02.01.2001", dob_style))
    story.append(Paragraph("<b>ЦЕЛЕВАЯ ДОЛЖНОСТЬ:</b> Младший ETL-разработчик / Начинающий Дата-инженер / Аналитик данных / Операционный аналитик", subtitle_style))
    
    contact_data = [
        [Paragraph("<b>Номер телефона/ telegram:</b> 8(962)625-80-06", body_style)],
        [Paragraph("<b>Почта:</b> Svistin64.v@gmail.com", body_style), 
         Paragraph("<b>Местоположение:</b> Саратов, Россия (Готов к удаленной работе / гибриду)", body_style)]
    ]
    contact_table = Table(contact_data, colWidths=[260, 260])
    contact_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(contact_table)
    story.append(Spacer(1, 10))

    # --- ТЕХНИЧЕСКИЙ АРСЕНАЛ ---
    add_section_header("Технический арсенал")
    tech_items = [
        "• <b>Базы данных и SQL (PostgreSQL):</b> Сложные аналитические запросы, агрегация данных, оконные функции, опыт работы через СУБД DBeaver.",
        "• <b>Python & Pandas:</b> Базовая векторизованная обработка данных, работа с DataFrame (merge, groupby, fillna), среда VS Code / Jupyter Notebooks.",
        "• <b>Автоматизация:</b> Разработка скриптов автоматизации (VBA) для очистки, рефакторинга и сборки сводной отчетности в Excel.",
        "• <b>Использование AI (Prompt Engineering):</b> Использование LLM-моделей как инструмента для ускорения написания кода, автоматизации рутинных задач и генерации синтетических данных. Навык чёткой декомпозиции задач, составления структурированных промптов и обязательный личный аудит/верификация результатов генерации (Zero Trust подход к ИИ)."
    ]
    for item in tech_items:
        story.append(Paragraph(item, body_style))

    # --- ОПЫТ РАБОТЫ ---
    add_section_header("Опыт работы")

    # ООО «ФракДжет-Строй» (Текущее место)
    exp1_header = [
        [Paragraph("<b>ООО «ФракДжет-Строй»</b> (Строительный инжиниринг, производство)", body_style),
         Paragraph("<b>Февраль 2026 г. — по настоящее время</b>", right_body_style)]
    ]
    t_exp1 = Table(exp1_header, colWidths=[340, 180])
    t_exp1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    story.append(t_exp1)
    story.append(Paragraph("<i>Позиция: Инженер ПЭО (аналитический отдел) / Должность: инженер ПТО II категории</i>", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>Ключевые обязанности:</b>", body_style))
    story.append(Paragraph("• <b>Сбор и обработка оперативных данных:</b> Ежедневный сбор, сквозной учет и верификация оперативной отчетности о выполнении работ, затратах человек-часов и машино-часов на объекте строительства.", body_style))
    story.append(Paragraph("• <b>Операционное планирование и моделирование:</b> Расчет и актуализация графиков производства работ (ГПР). Краткосрочное и среднесрочное планирование на основе многофакторного анализа: фактического распределения ресурсов, темпов поставки материалов и версий рабочей документации (РД).", body_style))
    story.append(Paragraph("• <b>Управление архитектурой внутренних отчетов:</b> Поддержка актуальных табличных структур, обработка, аналитики, ввод и вывода данных в формате отчетов; организация интерфейсов ввода/вывода для смежных отделов.", body_style))
    story.append(Paragraph("• <b>Data Quality & Коммуникации:</b> Постоянное взаимодействие с производителями работ на участках, проведение аудита входящей отчетности для выявления логических ошибок, расхождений и системных коллизий в первичных данных.", body_style))
    
    story.append(Paragraph("<b>Достижения:</b>", body_style))
    story.append(Paragraph("• <b>Сбор и очистка данных (ETL):</b> Проектировал и реализовывал алгоритмы оптимизированного автоматического сбора, валидации и трансформации технологических данных, переводя разрозненные оффлайн-выгрузки в структурированные плоские таблицы для дальнейшей аналитики и выгрузки отчетности.", body_style))
    story.append(Paragraph("• <b>Автоматизация отчетности:</b> Разработал комплекс скриптов (VBA) для автоматизации сводной отчетности холдинга, исключающий ручной ввод данных и минимизировавший время формирования итоговых документов.", body_style))
    story.append(Spacer(1, 6))
    # --- ОПЫТ РАБОТЫ (ПРОДОЛЖЕНИЕ) ---
    exp2_header = [
        [Paragraph("<b>ООО «ФракДжет-Строй»</b>", body_style),
         Paragraph("<b>Август 2024 г. — Февраль 2026 г.</b>", right_body_style)]
    ]
    t_exp2 = Table(exp2_header, colWidths=[350, 170])
    t_exp2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    story.append(t_exp2)
    story.append(Paragraph("<i>Позиция: Инженер ПТО/ Должность: инженер ПТО II категории</i>", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("• <b>Контроль данных:</b> Формировал, проверял и вел сквозные технологические базы данных (журналы сварочных работ, заключения ПИЛ, общий журнал работ).", body_style))
    story.append(Paragraph("• <b>Валидация и верификация:</b> Осуществлял перекрестную сверку исполнительной документации (ИД) перед сдачей заказчику; обеспечивал строгую хронологическую и логическую увязку данных между независимыми реестрами.", body_style))
    story.append(Paragraph("• <b>Снижение операционных рисков:</b> Проводил регулярный аудит документации на соответствие жестким требованиям строительного контроля (СКК), своевременно выявляя и устраняя расхождения в отчетности.", body_style))
    story.append(Spacer(1, 6))

    # ООО «ФракДжет-Строй» (Стропальщик / Координатор)
    exp3_header = [
        [Paragraph("<b>ООО «ФракДжет-Строй»</b>", body_style),
         Paragraph("<b>Апрель 2023 г. — Август 2024 г.</b>", right_body_style)]
    ]
    t_exp3 = Table(exp3_header, colWidths=[350, 170])
    t_exp3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    story.append(t_exp3)
    story.append(Paragraph("<i>Позиция: Линейный координатор ресурсов / Должность: стропальщик</i>", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("• <b>Операционный учет:</b> Ежедневный сбор СНЗ (сменно-ночных заданий), учет и табелирование трудозатрат человек-часов/машино-часов в условиях высокой динамики.", body_style))
    story.append(Paragraph("<b>Ключевые достижения на позиции:</b>", body_style))
    story.append(Paragraph("• <b>Успешный переход в ИТР:</b> За счет личной инициативы, алгоритмического подхода к задачам и автоматизации рутинных процессов переведен с линейной рабочей позиции (стропальщик) на инженерно-управленческую должность в течение первых 8 месяцев работы.", body_style))
    story.append(Paragraph("• <b>Глубокий рефакторинг систем учета:</b> Самостоятельно провел полный аудит унаследованных учетных таблиц Excel. Обнаружил и ликвидировал скрытые формульные ошибки, оптимизировал интерфейс ввода данных для полевых сотрудников, что кардинально сократило трудозатраты на ежедневную рутинную проверку.", body_style))
    story.append(Spacer(1, 6))

    # КЦ Телеконтакт
    exp4_header = [
        [Paragraph("<b>КЦ «ТЕЛЕКОНТАКТ»</b> (Аутсорсинговый контакт-центр)", body_style),
         Paragraph("<b>Декабрь 2022 г. — Март 2023 г.</b>", right_body_style)]
    ]
    t_exp4 = Table(exp4_header, colWidths=[350, 170])
    t_exp4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    story.append(t_exp4)
    story.append(Paragraph("<i>Позиция: Менеджер по маршрутизации и валидации звонков (проект «АВТО.РУ»)</i>", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("• <b>Анализ требований и сопоставление данных:</b> Проводил аудит неструктурированных запросов клиентов, выявлял ключевые критерии выбора и сопоставлял потребности покупателя с техническими параметрами и условиями доступных автомобилей в базе данных.", body_style))
    story.append(Paragraph("• <b>Минимизация потерь данных (отказов):</b> Отрабатывал возражения и сложные случаи отказов на линии, удерживая клиентов в воронке продаж.", body_style))
    story.append(Paragraph("• <b>Работа в рамках автоматического SLA:</b> Выполнял задачи в условиях высокой интенсивности под непрерывным автоматизированным контролем ключевых метрик эффективности (SLA) и строгого программного регламента учета рабочего времени.", body_style))
    story.append(Spacer(1, 6))
    # Срочная служба в ВС РФ
    exp5_header = [
        [Paragraph("<b>Срочная служба в ВС РФ</b>", body_style),
         Paragraph("<b>2021 г. — 2022 г.</b>", right_body_style)]
    ]
    t_exp5 = Table(exp5_header, colWidths=[400, 120])
    t_exp5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(t_exp5)
    story.append(Spacer(1, 6))

    # --- ЧАСТЬ 3: ПЕТ-ПРОЕКТЫ ---
    add_section_header("Пет-проекты / Лабораторная практика (Самостоятельное обучение)")
    story.append(Paragraph("• <b>Интенсивная SQL-практика:</b> Самостоятельно написал чистые SQL-запросы для 33 практических бизнес-сценариев.", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Симуляция локального Финтех ELT-пайплайна | Август 2026</b>", body_style))
    story.append(Paragraph("<i>Стек: Python (Pandas, NumPy), PostgreSQL, Power BI, VS Code, DBeaver.</i>", body_style))
    story.append(Paragraph("• <b>Развертывание среды:</b> Развернул изолированную девелоперскую среду для симуляции классического ELT/ETL-контура (Jupyter Notebooks в VS Code, PostgreSQL, DBeaver).", body_style))
    story.append(Paragraph("• <b>Моделирование данных:</b> Сгенерировал синтетический массив транзакций на Python с искусственным внедрением аномалий для тестирования отказоустойчивости.", body_style))
    story.append(Paragraph("• <b>Инженерия данных (DDL):</b> Разработал DDL-структуру таблиц-приемников (VARCHAR Staging) в PostgreSQL, настроил импорт CSV-файлов через DBeaver.", body_style))
    story.append(Paragraph("• <b>Трансформация (Т):</b> Написал очистной SQL-скрипт для фильтрации, принудительного приведения форматов и фиксации логики в витрине данных (CREATE VIEW).", body_style))
    story.append(Paragraph("• <b>Визуализация:</b> Подключил базу данных и вывел итоговый результат на интерактивный дашборд Microsoft Power BI.", body_style))

    # --- ЧАСТЬ 4: О СЕБЕ ---
    add_section_header("О себе (Особенности мышления и подход к данным)")
    story.append(Paragraph("• <b>Алгоритмическая логика и декомпозиция:</b> Воспринимаю рабочие процессы и массивы данных через строгую бинарную логику. Любую комплексную бизнес-задачу последовательно декомпозирую на изолированные, пошагово связанные этапы. Стремлюсь к полному исключению «серых зон» и хаоса в процессах.", body_style))
    story.append(Paragraph("• <b>Контроль качества данных и логирование (Audit Logs):</b> К любым входящим данным, чужим расчетным формулам или сгенерированному ИИ коду применяю принцип строгой верификации и нулевого доверия (Zero Trust). Любой промежуточный результат подвергаю входному и выходному контролю для обеспечения точности.", body_style))
    story.append(Paragraph("• <b>Рефакторинг Legacy-систем:</b> Обладаю навыком поиска внутренней логики в чужих неструктурированных массивах данных. Выявляю скрытые формульные уязвимости и перестраиваю учетные формы по принципу разделения слоев: надежное хранение первоисточников и автоматические витрины вывода отчетности.", body_style))
    story.append(Paragraph("• <b>Стремление к оптимизации:</b> Нацелен на автоматизацию рутины, оптимизацию сложных процессов и минимизацию человеческого фактора.", body_style))
    story.append(Paragraph("• <b>Практическое понимание ETL/ELT:</b> Четко понимаю физический цикл движения данных. От извлечения из разрозненных первоисточников (Extract) и их глубокой очистки/нормализации (Transform) до упорядоченной загрузки в базу данных на постоянное хранение (Load).", body_style))
    story.append(Paragraph("• <b>Быстрая адаптация к инструментам:</b> Отношусь к синтаксису и языкам (VBA, SQL, Python) как к инструментам решения прикладных бизнес-задач. Быстро вникаю в логику работы новых ИТ-систем и платформ.", body_style))

    # --- ОБРАЗОВАНИЕ ---
    add_section_header("Образование")
    edu_data = [
        [Paragraph("<b>ИТ-Образование: среднее профессиональное (Диплом с отличием)</b><br/>ППК СГТУ им. Гагарина Ю.А., специальность 09.02.02 «Компьютерные сети»", body_style),
         Paragraph("<b>2017 - 2021 гг.</b>", right_body_style)],
        [Paragraph("<b>Высшее образование (в процессе)</b><br/>СГТУ им. Гагарина Ю.А., институт машиностроения и материаловедения: (23.05.01) Наземные транспортно-технологические средства", body_style),
         Paragraph("<b>с 2023 г. — н.в.</b>", right_body_style)]
    ]
    t_edu = Table(edu_data, colWidths=[400, 120])
    t_edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
    story.append(t_edu)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Сертификаты:</b>", body_style))
    story.append(Paragraph("• Сертификат SQL (Stepik, №3270511).", body_style))
    story.append(Paragraph("• Сертификат Python для анализа данных (Stepik, №3274127).", body_style))

    # Сборка итогового документа
    doc.build(story)
    print(f"Успешно сгенерировано! Файл: {pdf_filename}")

if __name__ == "__main__":
    create_resume()
