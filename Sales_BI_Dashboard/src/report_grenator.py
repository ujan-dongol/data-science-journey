from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(kpis):
    doc = SimpleDocTemplate("outputs/sales_report.pdf")
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Sales KPI Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    for key, value in kpis.items():
        elements.append(Paragraph(f"{key}: {value}", styles["Normal"]))
        elements.append(Spacer(1, 12))

    doc.build(elements)
