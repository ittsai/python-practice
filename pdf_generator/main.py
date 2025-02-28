from fpdf import FPDF
import pandas

pages = pandas.read_csv("pages.csv",sep=";")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
for index, row in pages.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 100, 0)
    pdf.cell(w=0,h=12, txt=row["Topics"], align="L", ln=1)
    pdf.line(10,21,200,21)

    pdf.ln(265)

    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(189, 189, 189)
    pdf.cell(w=0, h=10, txt=row["Topics"], align="R")

    for i in range(row["Pages"] -1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(189, 189, 189)
        pdf.cell(w=0, h=10, txt=row["Topics"], align="R")
pdf.output("output.pdf")