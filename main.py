import pandas as pd

from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)


df = pd.read_csv("topics.csv")

pdf.cell(w=0, h=12, txt="Hello", align="L", ln=1, border=1)
# for index, row in df.iterrows():
#     pass


print(df.head())

pdf.output("output.pdf")