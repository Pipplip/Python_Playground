"""
PDF's zusammenfügen, trennen und Text auslesen

Install:
pip install pypdf2

"""

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

def get_meta(path):
    """ lese meta infos aus pdf"""
    with open(path, 'rb') as f: # bytes lesen (rb = read Bytes)
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        nop = pdf.getNumPages
    print(info)
    print(nop)

def extract_text(path):
    with open(path, 'rb') as f: # bytes lesen (rb = read Bytes)
        pdf = PdfFileReader(f)
        page_one = pdf.getPage(0) # erste Seite
        #print(page_one)
        #print(type(page_one))
        text = page_one.extractText() # extrahiere Text aus der ersten Seite
        print(text)

def split_pdf(path):
    """ splitted eine pdf in einzelne pdfs pro Seite"""
    with open(path, 'rb') as f: # bytes lesen (rb = read Bytes)
        pdf = PdfFileReader(f)
        for page in range(pdf.getNumPages()): # für jede Seite der Pdf
            writer = PdfFileWriter()
            writer.addPage(pdf.getPage(page))
            with open(f"{page}.pdf", "wb") as f_out: # Seitenzahl als einzel-pdf Name
                writer.write(f_out)

def merge_pdf(input_paths, output_path):
    writer = PdfFileWriter()
    for i in input_paths:
        pdf_reader = PdfFileReader(i)
        for page in range(pdf_reader.getNumPages()):
            writer.addPage(pdf_reader.getPage(page))
        with open(output_path, "wb") as f_out:
            writer.write(f_out)

def lazy_merge(input_paths, output_path):
    pdf_merger = PdfFileMerger()
    for i in input_paths:
        pdf_merger.append(i)
    with open(output_path, "wb") as f_out:
        pdf_merger.write(f_out)

# main
if __name__ == '__main__':
    path = r"C:\Users\Philipp Becker\Desktop\Einführung in P\Code\Projekte\PDFs\testPdf.pdf"
    #get_meta(path)
    #extract_text(path)
    #split_pdf(path)
    #merge_pdf(["0.pdf", "1.pdf"], "out.pdf")
    lazy_merge(["0.pdf", "1.pdf"], "out2.pdf")