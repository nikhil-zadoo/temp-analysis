from collections import Counter
import docx2txt


to_lower = lambda x: x.lower()
plain_text = docx2txt.process("kashmiri.docx")
list_of_words = plain_text.split()
list_of_words_lower = list(map(to_lower, list_of_words))
print(Counter(list_of_words_lower))