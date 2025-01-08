from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
import io
import os

# PDFをHTMLに変換
def convert_pdf_to_html(pdf_file, output_html):
    with open(pdf_file, "rb") as pdf:
        output = io.StringIO()
        laparams = LAParams()
        extract_text_to_fp(pdf, output, laparams=laparams, output_type='html', codec=None)
        html_content = output.getvalue()
        with open(output_html, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

# 使用例
dirpath = os.path.abspath(os.path.dirname(__file__))
convert_pdf_to_html(os.path.join(dirpath,"140120250107547220.pdf"), "miner.html")
