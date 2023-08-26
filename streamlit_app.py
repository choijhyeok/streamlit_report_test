import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import streamlit.components.v1 as components
import urllib
import base64
import pdf2jpg
import numpy as np
from PIL import Image
import os

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter


def crop_white_space(arr: np.array) -> np.array:
    FOOTER_ROWS = 300
    WHITE_VALUE = 255
    white_pixels = (arr == WHITE_VALUE)
    white_rows = list(np.all(white_pixels, axis=(1, 2)))
    last_non_white_row_idx = max(loc for loc, val in enumerate(white_rows) if not val)
    merged_arr = arr[:last_non_white_row_idx + FOOTER_ROWS]
    return merged_arr


pdfmetrics.registerFont(TTFont("맑은고딕", st.secrets["font_name"]))
pdf = canvas.Canvas(st.secrets["file_name"], pagesize=letter)
pdf.setFont("맑은고딕", 16)
pdf.drawString(30, 750, "파이썬 PDF 파일 생성")
pdf.save()


result = pdf2jpg.convert_pdf2jpg(st.secrets["file_name"], st.secrets["file_name_jpg"], pages="ALL")
images = []
for image_path in result[0]["output_jpgfiles"]:
    images.append(np.array(Image.open(image_path)))

merged_arr = np.concatenate(images)
merged_arr = crop_white_space(merged_arr)
# merged_path = os.path.join(st.secrets["file_name_jpg"], "merged.jpeg")
Image.fromarray(merged_arr).save(st.secrets["file_name_jpeg"])

# Display the image
st.image(st.secrets["file_name_jpeg"])


# with open(st.secrets["file_name"], "rb") as f:
#     base64_pdf = base64.b64encode(f.read()).decode('utf-8')
# # Embedding PDF in HTML
# pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'

# # Displaying File
# st.markdown(pdf_display, unsafe_allow_html=True)
               






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
