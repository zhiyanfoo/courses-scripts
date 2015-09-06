import os
import PyPDF2

escape_sequence = "SKIP"
li = [i for i in os.walk(os.getcwd())]

for di in li:
    root = di[0]
    print root
    for fi in di[2]:
        lent = len(fi)
        if fi[lent-4:lent] == ".pdf" and fi[lent-8:lent-4] != escape_sequence:
            fi_path = os.path.join(root, fi)
            print fi_path
            orgpdf = open(fi_path,'rb')
            orgpdf_reader = PyPDF2.PdfFileReader(orgpdf)
            newpdf_writer = PyPDF2.PdfFileWriter()
            for pageNum in range(orgpdf_reader.numPages-1):
                pageObj = orgpdf_reader.getPage(pageNum)
                newpdf_writer.addPage(pageObj)
            temp_path = os.path.join(root, "u_temp")
            newpdf_output = open(temp_path, 'wb')
            newpdf_writer.write(newpdf_output)
            newpdf_output.close()
            orgpdf.close()
            os.remove(fi_path)
            os.rename(temp_path, fi_path)
            

