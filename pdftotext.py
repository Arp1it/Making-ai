from pypdf import PdfReader

reader = PdfReader("leph101.pdf")
number_of_pages = len(reader.pages)

with open("da.txt", "w", encoding="utf-8") as f:
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        print(text)

        f.write(text)
