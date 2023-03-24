from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_name, start_page, end_page, output_pdf):
    input_file = PdfReader(open(file_name, 'rb'))
    output_file = PdfWriter()
    for i in range(start_page, end_page):
        output_file.add_page(input_file.pages[i])
    with open(output_pdf, 'wb') as f:
        output_file.write(f)
if __name__ == '__main__':
    split_pdf("D:\\mergepdf\\3-7.pdf", 1, 3, "D:\\mergepdf\\1-2.pdf")