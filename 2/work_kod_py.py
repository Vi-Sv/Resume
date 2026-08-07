import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Регистрация системных шрифтов с поддержкой кириллицы (Arial)
try:
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arialbd.ttf'))
except:
    pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-Bold', '/usr/share/fonts/truetype/msttcorefonts/Arialbd.ttf'))

# Цветовая палитра из шаблона
COLOR_PRIMARY = colors.HexColor("#1A3636")    # Глубокий темно-серый / антрацит
COLOR_SECONDARY = colors.HexColor("#40A578")  # Яркий бирюзовый / циан
COLOR_TEXT_DARK = colors.HexColor("#333333")  # Основной текст
COLOR_TEXT_LIGHT = colors.HexColor("#FFFFFF") # Светлый текст
COLOR_BG_LIGHT = colors.HexColor("#F9F9F9")   # Фон

class NumberedCanvas(canvas.Canvas):
    """Холст для динамического расчета общего количества страниц"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Arial", 9)
        self.setFillColor(COLOR_TEXT_DARK)
        page_text = f"Страница {self._pageNumber} из {page_count}"
        self.drawRightString(A4[0] - 1.5*cm, 1*cm, page_text)
        self.restoreState()
# Настройка базовых стилей текста
styles = getSampleStyleSheet()

# Модификация существующих или создание уникальных стилей для резюме
style_name = ParagraphStyle(
    'ResumeName',
    fontName='Arial-Bold',
    fontSize=22,
    leading=26,
    textColor=COLOR_PRIMARY,
    spaceAfter=4
)

style_target = ParagraphStyle(
    'ResumeTarget',
    fontName='Arial',
    fontSize=12,
    leading=15,
    textColor=COLOR_SECONDARY,
    spaceAfter=12
)

style_contacts = ParagraphStyle(
    'ResumeContacts',
    fontName='Arial',
    fontSize=10,
    leading=14,
    textColor=COLOR_TEXT_DARK,
    spaceAfter=15
)

style_h1 = ParagraphStyle(
    'ResumeH1',
    fontName='Arial-Bold',
    fontSize=13,
    leading=16,
    textColor=COLOR_PRIMARY,
    spaceBefore=14,
    spaceAfter=6,
    keepWithNext=True
)

style_h2 = ParagraphStyle(
    'ResumeH2',
    fontName='Arial-Bold',
    fontSize=11,
    leading=14,
    textColor=COLOR_TEXT_DARK,
    spaceBefore=8,
    spaceAfter=4,
    keepWithNext=True
)

style_body = ParagraphStyle(
    'ResumeBody',
    fontName='Arial',
    fontSize=10,
    leading=13,
    textColor=COLOR_TEXT_DARK,
    spaceAfter=4
)

style_bullet = ParagraphStyle(
    'ResumeBullet',
    fontName='Arial',
    fontSize=10,
    leading=13,
    textColor=COLOR_TEXT_DARK,
    leftIndent=12,
    firstLineIndent=-8,
    spaceAfter=3
)

style_sidebar_title = ParagraphStyle(
    'SidebarTitle',
    fontName='Arial-Bold',
    fontSize=11,
    leading=14,
    textColor=COLOR_TEXT_LIGHT,
    spaceBefore=10,
    spaceAfter=6,
    keepWithNext=True
)

style_sidebar_text = ParagraphStyle(
    'SidebarText',
    fontName='Arial',
    fontSize=9,
    leading=12,
    textColor=COLOR_TEXT_LIGHT,
    spaceAfter=4
)

def create_section_divider():
    """Функция для создания декоративного разделителя разделов"""
    t = Table([['']], colWidths=[18*cm], rowHeights=[2])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_SECONDARY),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    return t
# Инициализация документа и основного контейнера элементов (story)
pdf_filename = "Resume_ETL_Developer.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=1.5*cm,
    rightMargin=1.5*cm,
    topMargin=1.5*cm,
    bottomMargin=1.5*cm
)
story = []

# --- БЛОК 1: КОНТАКТЫ И ЗАГОЛОВОК ---
story.append(Paragraph("Свистин Виктор Андреевич | 02.01.2001", style_name))
story.append(Paragraph("<b>Целевая должность:</b> Младший ETL-разработчик / Начинающий Дата-инженер / Аналитик данных", style_target))
story.append(Paragraph("<b>Локация:</b> Саратов, Россия (Удаленная работа / Гибрид / Релокация)<br/><b>Контакты:</b> +7-962-625-80-06 | svistin64.v@gmail.com", style_contacts))

# --- БЛОК 2: ТЕХНИЧЕСКИЕ НАВЫКИ ---
story.append(Paragraph("ТЕХНИЧЕСКИЕ НАВЫКИ", style_h1))
story.append(Paragraph("<b>Базы данных и SQL:</b> PostgreSQL, DBeaver, DML, DDL.", style_bullet))
story.append(Paragraph("<b>Языки и библиотеки:</b> Python (Pandas).", style_bullet))
story.append(Paragraph("<b>Инструменты и BI:</b> Microsoft Power BI, Excel.", style_bullet))
story.append(Paragraph("<b>Дополнительно:</b> Понимание концепций ETL/ELT, проектирование реляционных структур данных, трансформация и выгрузка очищенных данных.", style_bullet))
story.append(Spacer(1, 8))

# --- БЛОК 3: ОПЫТ РАЗРАБОТКИ И ПЕТ-ПРОЕКТЫ ---
story.append(Paragraph("ОПЫТ РАЗРАБОТКИ И ПЕТ-ПРОЕКТЫ (Самостоятельное обучение)", style_h1))

project_1 = []
project_1.append(Paragraph("Симуляция локального Финтех ELT-пайплайна (Август 2026 г.)", style_h2))
project_1.append(Paragraph("<b>Стек:</b> Python (Pandas, NumPy), PostgreSQL, Power BI, DBeaver.", style_body))
project_1.append(Paragraph("• <b>Результат:</b> Развернул изолированную девелоперскую среду для симуляции классического ELT/ETL-контура. На Python сгенерировал синтетический массив транзакций с аномалиями для тестирования отказоустойчивости. Спроектировал DDL-структуру таблиц-приемников в PostgreSQL. Написал SQL-скрипты очистки, приведения форматов и агрегации данных. Подключил СУБД к Power BI и настроил интерактивный дашборд.", style_bullet))
story.append(KeepTogether(project_1))

project_2 = []
project_2.append(Paragraph("SQL-практика", style_h2))
project_2.append(Paragraph("• Реализовал и протестировал чистые SQL-запросы для 33 практических бизнес-сценариев.", style_bullet))
story.append(KeepTogether(project_2))
story.append(Spacer(1, 8))

# --- БЛОК 4: ОПЫТ РАБОТЫ ---
story.append(Paragraph("ОПЫТ РАБОТЫ", style_h1))

job_1 = []
job_1.append(Paragraph("ООО «ФракДжет-Строй» (Строительный инжиниринг)", style_h2))
job_1.append(Paragraph("<b>Период:</b> Февраль 2026 г. — по настоящее время | <b>Позиция:</b> Инженер ПЭО (планово-экономический отдел) / Должность: Инженер ПТО II категории", style_body))
job_1.append(Paragraph("<b>Обязанности:</b>", style_body))
job_1.append(Paragraph("• <b>Сбор и обработка данных:</b> Ежедневный сбор, учет и верификация оперативной отчетности о выполнении работ, затратах человек-часов и машино-часов на объекте строительства.", style_bullet))
job_1.append(Paragraph("• <b>Операционное планирование и моделирование:</b> Расчет и актуализация графиков производства работ (ГПР). Краткосрочное и среднесрочное планирование на основе многофакторного анализа: фактического распределения ресурсов, темпов поставки материалов и версий рабочей документации.", style_bullet))
job_1.append(Paragraph("• <b>Коммуникации:</b> Постоянное взаимодействие с производителями работ на участках, проведение аудита входящей отчетности для выявления логических ошибок, расхождений и системных коллизий в первичных данных.", style_bullet))
job_1.append(Paragraph("<b>Достижения:</b>", style_body))
job_1.append(Paragraph("• Разработал алгоритмы автоматического сбора и трансформации технологических данных, преобразовав разрозненные выгрузки в единую реляционную витрину для BI-аналитики.", style_bullet))
story.append(KeepTogether(job_1))
story.append(Spacer(1, 6))

job_2 = []
job_2.append(Paragraph("<b>Период:</b> февраль 2024 г. — февраль 2026 г. | <b>Позиция:</b> Инженер ПТО (производственно-технический отдел) / Должность: Инженер ПТО II категории", style_body))
job_2.append(Paragraph("<b>Обязанности:</b>", style_body))
job_2.append(Paragraph("• <b>Контроль данных:</b> Формировал, проверял и вел сквозные технологические базы данных по части исполнительной документации.", style_bullet))
job_2.append(Paragraph("• <b>Верификация:</b> Осуществлял перекрестную сверку исполнительной документации перед сдачей заказчику; обеспечивал строгую хронологическую и логическую увязку данных между независимыми реестрами.", style_bullet))
job_2.append(Paragraph("• <b>Снижение операционных рисков:</b> Проводил регулярный аудит документации на соответствие жестким требованиям строительного контроля, своевременно выявляя и устраняя расхождения в отчетности.", style_bullet))
job_2.append(Paragraph("<b>Достижения:</b>", style_body))
job_2.append(Paragraph("• На основе продемонстрированных результатов и личных качеств был приглашен руководством на повышение на должность инженера планово-экономического отдела.", style_bullet))
story.append(KeepTogether(job_2))
story.append(Spacer(1, 6))

job_3 = []
job_3.append(Paragraph("<b>Период:</b> Апрель 2023 г. — февраль 2024 г. | <b>Позиция:</b> Координатор ресурсов ПМР (подразделение монтажных работ) | Должность: Стропальщик", style_body))
job_3.append(Paragraph("<b>Обязанности:</b>", style_body))
job_3.append(Paragraph("• Операционный учет: Ежедневный сбор СНЗ (сменно-ночных заданий), учет и табелирование трудозатрат человек-часов/машино-часов в условиях высокой динамики.", style_bullet))
job_3.append(Paragraph("<b>Достижения:</b>", style_body))
job_3.append(Paragraph("• Провел полный аудит унаследованных учетных таблиц Excel. Обнаружил и ликвидировал скрытые формульные ошибки, оптимизировал интерфейс ввода данных для полевых сотрудников, что кардинально сократило трудозатраты на ежедневную рутинную проверку.", style_bullet))
job_3.append(Paragraph("• За счет личной инициативы, ответственности, алгоритмического подхода к задачам и автоматизации рутинных процессов, а также принятия на себя ответственности за ведение важной исполнительной документации, был переведен с линейной рабочей позиции на инженерно-управленческую должность в течение первых 8 месяцев работы.", style_bullet))
story.append(KeepTogether(job_3))
story.append(Spacer(1, 6))

job_4 = []
job_4.append(Paragraph("КЦ «ТЕЛЕКОНТАКТ» (Аутсорсинговый контакт-центр)", style_h2))
job_4.append(Paragraph("<b>Период:</b> Декабрь 2022 г. — Март 2023 г. | <b>Позиция:</b> Менеджер по маршрутизации и валидации данных | Должность: Специалист по продажам", style_body))
job_4.append(Paragraph("<b>Обязанности:</b>", style_body))
job_4.append(Paragraph("• <b>Анализ данных:</b> Проводил аудит неструктурированных запросов, сопоставлял потребности клиентов с техническими параметрами базы данных. Выполнял задачи в условиях высокой интенсивности под непрерывным автоматизированным контролем ключевых метрик эффективности (SLA) и строгого программного регламента учета рабочего времени.", style_bullet))
story.append(KeepTogether(job_4))
story.append(Spacer(1, 8))

# --- БЛОК 5: ОБРАЗОВАНИЕ И СЕРТИФИКАТЫ ---
story.append(Paragraph("ОБРАЗОВАНИЕ И СЕРТИФИКАТЫ", style_h1))
story.append(Paragraph("• <b>ППК СГТУ им. Гагарина Ю.А.</b> (2017 — 2021 гг.) | Специальность: 09.02.02 «Компьютерные сети», Диплом с отличием.", style_bullet))
story.append(Paragraph("• <b>СГТУ им. Гагарина Ю.А.</b> (2023 г. — н.в., в процессе) | Высшее техническое образование.", style_bullet))
story.append(Paragraph("• <b>Сертификат:</b> «SQL» (Stepik, №3270511).", style_bullet))
story.append(Paragraph("• <b>Сертификат:</b> «Python для анализа данных» (Stepik, №3274127).", style_bullet))
story.append(Spacer(1, 8))

# --- БЛОК 6: ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ ---
story.append(Paragraph("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ", style_h1))
story.append(Paragraph("Вооруженные Силы РФ: Срочная служба", style_h2))
story.append(Paragraph("<b>Период:</b> 2021 г. — 2022 г. | <b>Позиция:</b> Служба в подразделении Засекреченной автоматизированной связи (ЗАС)", style_body))

# Сборка документа
doc.build(story, canvasmaker=NumberedCanvas)
