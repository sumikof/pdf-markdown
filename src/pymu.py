import fitz  # PyMuPDF
import os

# PDFをHTMLに変換
def convert_pdf_to_html(pdf_file, output_html):
    doc = fitz.open(pdf_file)
    html_content = ""
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        # ページをHTML形式で抽出
        html_content += page.get_text("html")
    
    # HTMLファイルに保存
    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

# 使用例
dirpath = os.path.abspath(os.path.dirname(__file__))
convert_pdf_to_html(os.path.join(dirpath,"140120250107547220.pdf"), "pymu.html")