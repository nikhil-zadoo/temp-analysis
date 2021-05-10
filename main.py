from collections import Counter
import docx2txt

plain_text = docx2txt.process("kashmiri.docx")
print(plain_text)

print("Splitting")
list_of_words = plain_text.split()
print(Counter(list_of_words))