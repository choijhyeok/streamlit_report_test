import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import streamlit.components.v1 as components
import urllib
import base64

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

pdfmetrics.registerFont(TTFont("맑은고딕", st.secrets["font_name"]))
pdf = canvas.Canvas(st.secrets["file_name"], pagesize=letter)
pdf.setFont("맑은고딕", 16)
pdf.drawString(30, 750, "파이썬 PDF 파일 생성")
pdf.save()


with open(st.secrets["file_name"], "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
# Embedding PDF in HTML
pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'

# Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)
               
# st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
# st.title("🎓 Diploma PDF Generator")

# st.write(
#     "This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!"
# )

# left, right = st.columns(2)

# right.write("Here's the template we'll be using:")

# right.image("template.png", width=300)

# env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.get_template("template.html")


# left.write("Fill in the data:")
# form = left.form("template_form")
# student = form.text_input("Student name")
# course = form.selectbox(
#     "Choose course",
#     ["Report Generation in Streamlit", "Advanced Cryptography"],
#     index=0,
# )
# grade = form.slider("Grade", 1, 100, 60)
# submit = form.form_submit_button("Generate PDF")

# if submit:
#     html = template.render(
#         student=student,
#         course=course,
#         grade=f"{grade}/100",
#         date=date.today().strftime("%B %d, %Y"),
#     )

#     pdf = pdfkit.from_string(html, False)
#     st.balloons()

#     right.success("🎉 Your diploma was generated!")
#     # st.write(html, unsafe_allow_html=True)
#     # st.write("")
#     right.download_button(
#         "⬇️ Download PDF",
#         data=pdf,
#         file_name="diploma.pdf",
#         mime="application/octet-stream",
#     )
