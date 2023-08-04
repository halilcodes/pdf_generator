import pandas as pd

from fpdf import FPDF

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="BU", size=12)
pdf.cell(w=0, h=12, txt="Hello you!", align="L", ln=1, border=1)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hi There!", align="L", ln=1, border=1)


pdf.set_font(family="Times", style="B", size=24)
pdf.set_text_color(100, 100, 100)
for _, row in df.iterrows():
    for j in range(row["Pages"]):
        pdf.add_page()
        if j == 0:
            pdf.cell(w=0, h=12, txt=row.Topic, align="L", ln=1)
            pdf.line(10, 21, 200, 21)

    print(row[1])
    print("pages: ", row[2])

print(df.head())

pdf.output("output.pdf")
