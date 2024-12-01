import PyPDF2

pdf_file1 = PyPDF2.PdfFileReader("file1.pdf")
pdf_file2 = PyPDF2.PdfFileReader("file2.pdf")

output = PyPDF2.PdfFileMerger()

output.append(pdf_file1)
output.append(pdf_file2)

output.write("merged.pdf")