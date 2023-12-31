import PyPDF2
import sys

def pdf(new):
    #Change the current directory where you will save all assignment files and make sure to write \\ before the file name
    current = r"C:\\"
    pdffileobj=open(current + new + ".pdf",'rb')
    pdfreader=PyPDF2.PdfReader(pdffileobj)
    x=len(pdfreader.pages)
    text = ""

    file1=open(current + new + ".py","w+", encoding="utf-8")
    for ii in range(x):
        pageobj=pdfreader.pages[ii]
        text += pageobj.extract_text()

    file1.write(text + "\n")
    file1.close()

if __name__ == "__main__":
    file = sys.argv[1]
    pdf(file)
