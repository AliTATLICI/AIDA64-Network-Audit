from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))

def pdfkaydedici(gelenveri): 
   doc = SimpleDocTemplate("nmapsi_scan.pdf", pagesize=letter)
   # container for the 'Flowable' objects
   elements = []
    
   styleSheet = getSampleStyleSheet()
    
   
   data=[]
   for i in range(len(gelenveri)):
      data.append([gelenveri[i], 'B', 'C', 'E', 'D'])
    
   t=Table(data,style=[('GRID',(1,1),(-2,-2),1,colors.green),
                       ('BOX',(0,0),(1,-1),2,colors.red),
                       ('LINEABOVE',(1,2),(-2,2),1,colors.blue),
                       ('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
                       ('BACKGROUND', (0, 0), (0, 1), colors.pink),
                       ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
                       ('BACKGROUND', (2, 2), (2, 3), colors.orange),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('GRID',(0,0),(-1,-1),0.5,colors.black),
                       ('VALIGN',(3,0),(3,0),'BOTTOM'),
                       ('BACKGROUND',(3,0),(3,0),colors.limegreen),
                       ('BACKGROUND',(3,1),(3,1),colors.khaki),
                       ('ALIGN',(3,1),(3,1),'CENTER'),
                       ('BACKGROUND',(3,2),(3,2),colors.beige),
                       ('ALIGN',(3,2),(3,2),'LEFT'),
                       ('FONTNAME', (0,0), (1,0), 'VeraBd'),
                       ('FONTNAME', (0,1), (2,(len(gelenveri)-1)), 'Vera')
   ])
   t._argW[3]=1.5*inch
    
   elements.append(t)
   # write the document to disk
   doc.build(elements)
   print("pdf dosyası oluşturuldu")

