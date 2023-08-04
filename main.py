import pandas as pd

from fpdf import FPDF

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
#
# pdf.add_page()
#
# pdf.set_font(family="Times", style="BU", size=12)
# pdf.cell(w=0, h=12, txt="Hello you!", align="L", ln=1, border=1)
# pdf.set_font(family="Times", size=10)
# pdf.cell(w=0, h=12, txt="Hi There!", align="L", ln=1, border=1)


pdf.set_font(family="Times", style="B", size=24)
pdf.set_text_color(100, 100, 100)
for _, row in df.iterrows():
    for j in range(row["Pages"]):
        pdf.add_page()
        footer_begin = 277
        if j == 0:
            pdf.cell(w=0, h=12, txt=row.Topic, align="L", ln=1)
            # pdf.line(10, 21, 200, 21)
            footer_begin = 265

        for y in range(21, 290, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        footer_text = f"{row['Topic']} / {j+1}"
        pdf.ln(footer_begin)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=footer_text, align="R")

# for _, row in df.iterrows():
#     pdf.add_page()
#     pdf.cell(w=0, h=12, txt=row.Topic, align="L", ln=1)
#     pdf.line(10, 21, 200, 21)
#
#     # Set the footer
#     pdf.ln(260)
#     pdf.set_font(family="Times", style="I", size=8)
#     pdf.set_text_color(180, 180, 180)
#     pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
#     for j in range(row["Pages"]-1):
#         pdf.add_page()
#         # Set the footer
#         pdf.ln(260)
#         pdf.set_font(family="Times", style="I", size=8)
#         pdf.set_text_color(180, 180, 180)
#         pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    print(row[1])
    print("pages: ", row[2])

print(df.head())

pdf.output("output.pdf")
