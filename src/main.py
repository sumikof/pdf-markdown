import os
from markitdown import MarkItDown

markitdown = MarkItDown()
dirpath = os.path.abspath(os.path.dirname(__file__))
result = markitdown.convert(os.path.join(dirpath,"miner.html"))
# result = markitdown.convert("https://www.release.tdnet.info/inbs/140120250107547220.pdf")
print(result.text_content)