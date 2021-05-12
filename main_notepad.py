from collections import Counter
import docx2txt

plain_text = docx2txt.process("Urdu.docx")
list_of_words = plain_text.split()
#print(Counter(list_of_words))
counter_list_of_words = Counter(list_of_words)
elements = counter_list_of_words.items()
# for a, b in elements:
#     print(a)
#     print(b)

with open('results.txt', 'w') as fd:
    for word, frequency in sorted(elements, key=lambda x: x[1], reverse=True):
        fd.write(f"{word}: {str(frequency)}\n")