"""Create the original, downloadable FCC starter notes."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from additions import NOTES

def generate_notes(destination):
    directory = Path(destination) / "assets" / "notes"
    directory.mkdir(parents=True, exist_ok=True)
    fonts = Path("/usr/share/fonts/truetype/dejavu")
    pdfmetrics.registerFont(TTFont("FCCNotes", str(fonts / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("FCCNotesBold", str(fonts / "DejaVuSans-Bold.ttf")))
    styles = {
        "title": ParagraphStyle("Title", fontName="FCCNotesBold", fontSize=22, leading=28, textColor=colors.HexColor("#182c60"), spaceAfter=12),
        "body": ParagraphStyle("Body", fontName="FCCNotes", fontSize=10, leading=15, textColor=colors.HexColor("#35445f"), spaceAfter=7),
        "heading": ParagraphStyle("Heading", fontName="FCCNotesBold", fontSize=11.2, leading=16, textColor=colors.HexColor("#3c51b3"), spaceBefore=11, spaceAfter=6),
        "small": ParagraphStyle("Small", fontName="FCCNotes", fontSize=8.3, leading=12, textColor=colors.HexColor("#56647e"), spaceAfter=5),
    }
    def text(value, style="body"):
        return Paragraph(escape(value), styles[style])
    def frame(canvas, document):
        canvas.saveState()
        w, h = A4
        canvas.setFillColor(colors.HexColor("#eff2ff"))
        canvas.rect(0,h-76,w,76,stroke=0,fill=1)
        canvas.setFont("FCCNotesBold",11)
        canvas.setFillColor(colors.HexColor("#21366d"))
        canvas.drawString(44,h-35,"FUTURE CLOUD CAMPUS")
        canvas.setFont("FCCNotes",8)
        canvas.drawString(44,h-53,"One campus. Endless learning.  |  Free study notes")
        canvas.setStrokeColor(colors.HexColor("#dce3ef"))
        canvas.line(44,53,w-44,53)
        canvas.setFillColor(colors.HexColor("#5c6982"))
        canvas.setFont("FCCNotes",7.5)
        canvas.drawString(44,38,"A topic starter. Use alongside your school syllabus and teacher's guidance.")
        canvas.drawRightString(w-44,38,str(document.page))
        canvas.restoreState()
    for slug,title,subject,level,intro,points,example,questions in NOTES:
        doc=SimpleDocTemplate(str(directory/f"{slug}.pdf"),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=98,bottomMargin=68,title=title,author="Future Cloud Campus",pageCompression=1)
        story=[text(f"{subject}  /  {level}", "small"), text(title,"title"), text(intro)]
        story.append(text("Core ideas","heading"))
        for index,point in enumerate(points,1):
            story.append(text(f"{index}. {point}"))
        story.extend([text("Worked example","heading"),text(example),text("Try it yourself","heading")])
        for index,(question,_) in enumerate(questions,1):
            story.append(text(f"{index}. {question}"))
        story.extend([Spacer(1,6),text("Check your answers","heading")])
        for index,(_,answer) in enumerate(questions,1):
            story.append(text(f"{index}. {answer}","small"))
        doc.build(story,onFirstPage=frame,onLaterPages=frame)

if __name__ == "__main__":
    import sys
    generate_notes(Path(sys.argv[1]) if len(sys.argv)>1 else Path("dist"))
