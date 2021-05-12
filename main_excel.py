from collections import Counter
import docx2txt
import xlsxwriter

plain_text = docx2txt.process("Urdu.docx")
list_of_words = plain_text.split()
#print(Counter(list_of_words))
counter_list_of_words = Counter(list_of_words)
elements = counter_list_of_words.items()
# for a, b in elements:
#     print(a)
#     print(b)

workbook = xlsxwriter.Workbook('results_urdu.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "WORD")
worksheet.write(0, 1, "FREQUENCY")

#Iterate over collection elements and append to table craeted
itr = 1
for word, frequency in sorted(elements, key=lambda x: x[1], reverse=True):
    worksheet.write(itr, 0, word)
    worksheet.write(itr, 1, frequency)
    itr+=1

workbook.close()