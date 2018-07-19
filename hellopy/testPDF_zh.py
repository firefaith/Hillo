# -*- coding=utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from reportlab.pdfgen.canvas import Canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
from reportlab.pdfbase.ttfonts import TTFont 
pdfmetrics.registerFont(TTFont('song', 'Songti.ttc'))  


c2 = Canvas('2.pdf')  
c2.setFont('song',12)  
c2.drawString(100, 300, u'雅黑雅黑')  
c2.save()
