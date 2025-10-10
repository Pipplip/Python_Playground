from docx import Document

path = "C:/Users/Philipp/Desktop/test/"
fileName = "Nutzungsvereinbarungen-TR"

def docx_to_txt(docx_path, txt_path, encoding='utf-8'):
    doc = Document(docx_path)
    with open(txt_path, 'w', encoding=encoding) as f:
        for para in doc.paragraphs:
            f.write(para.text + '\n')

if __name__ == "__main__":
    # Beispiel-Aufruf
    docx_to_txt(path+fileName+".docx", path+"readme.txt", encoding='utf-8')  # oder z. B. 'windows-1252'