import os
from pdf2docx import Converter
from docx import Document

# PDFをWordに変換し、HTML形式に変換
def convert_pdf_to_html_via_word(pdf_file, output_html):
    word_file = "temp.docx"
    cv = Converter(pdf_file)
    cv.convert(word_file, start=0, end=None)
    cv.close()
    
    # WordをHTMLに変換
    doc = Document(word_file)
    html_content = ""
    for paragraph in doc.paragraphs:
        html_content += f"<p>{paragraph.text}</p>\n"
    
    # HTMLファイルに保存
    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

# 使用例
dirpath = os.path.abspath(os.path.dirname(__file__))
convert_pdf_to_html_via_word(os.path.join(dirpath,"140120250107547220.pdf"),"doc.html")