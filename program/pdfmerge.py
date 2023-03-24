import os
from PyPDF2 import PdfMerger

target_path = r'D:\\mergepdf\\'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]
file_merger = PdfMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)     # 合并pdf文件
file_merger.write(target_path + r"merge.pdf")