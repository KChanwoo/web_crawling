import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# pdf가 있는 경로
path = r'/Users/gwonchan-u/Desktop/project/의학용어사전/medical_Terminology_Language_for_Health.pdf'

# 각각의 pdf를 불러오기
pdf = PdfFileReader(open(path, 'rb'))

# pdf페이지수를 알아내기
numberPages = pdf.getNumPages()

# 페이지 별 텍스트 추출
for page in range(125, 130):
    p = pdf.getPage(page)

    p_text = p.getContents()


    print(page)
    print(p_text)

print('완료')
