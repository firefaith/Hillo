# -*- coding=utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

pdfmetrics.registerFont(TTFont('hei', 'simhei.ttf'))

doc = SimpleDocTemplate("test_report_lab.pdf", pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30,
                        bottomMargin=18)

doc.pagesize = landscape(A4)
elements = []

data = [["Title:","","","",""],
    ["Letter", "Number", "Stuff", "Long stuff that should be wrapped", u"备注"],
    ["A", "01", "ABCD", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", ""],
    ["B", "02", "CDEF", "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", ""],
    ["C", "03", "SDFSDF", "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC", ""],
    ["D", "04", "SDFSDF", "DDDDDDDDDDDDDDDDDDDDDDDD DDDDDDDDDDDDDDDDDDDDDDDDDDDDDD", ""],
    ["E", "05", "GHJGHJGHJ", "EEEEEEEEEEEEEE EEEEEEEEEEEEEEEEE EEEEEEEEEEEEEEEEEEEE", ""],
]

# SPAN, (sc,sr), (ec,er)
# style ： style name， start column，start row，end column，end row，（style value）
style = TableStyle([('SPAN',(0,0),(-1,0)), # 合并第一行
                    ('ALIGN', (0,0), (-1, 0), 'CENTER'), # 第一行左右居中，
                    ('VALIGN', (0,0), (-1, 0), 'MIDDLE'), # 第一行上下居中
                    ('FACE',(0,0),(-1,-1),'hei'), #字体 也可用FONTNAME
                    ('FONTSIZE',(1,1),(-1,-1),12),

                    ('ALIGN', (1, 1), (-2, 0), 'RIGHT'),
                    ('TEXTCOLOR', (1, 1), (-2, -2), colors.red), # 字体颜色

                    ('VALIGN', (0, 0), (0, -1), 'TOP'),
                    ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),

                    ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                    ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),

                    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                    ])

# Configure style and word wrap
'''
stylesheet = getSampleStyleSheet()
body_style = stylesheet["BodyText"]
body_style.wordWrap = 'CJK'
body_style.fontName = 'hei'
body_style.fontSize = 12
para_data = [[Paragraph(cell, body_style) for cell in row] for row in data]
#table = Table(para_data)
'''

table = Table(data)
table.setStyle(style)

# Send the data and build the file
elements.append(table)
doc.build(elements)
