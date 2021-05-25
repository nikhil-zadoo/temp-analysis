from collections import Counter
import docx2txt

plain_text = docx2txt.process("trial_file.docx")
list_of_words = plain_text.split()
#print(Counter(list_of_words))
counter_list_of_words = Counter(list_of_words)
elements = counter_list_of_words.keys()
#print(type(elements))

ele = counter_list_of_words.items()
with open('results_trial1', 'a+', encoding='utf-8') as f:
    f.write("WORD: FREQUENCY\n")
    for word, frequency in sorted(ele, key=lambda x: x[1], reverse=True):
        f.write(f"{word}: {str(frequency)}\n")

with open('tokens_Urdu.txt', 'r', encoding='utf-8') as file_1:
    tokens_Urdu_text = file_1.read()

with open('tokens_koshur.txt', 'r', encoding='utf-8') as file_2:
    tokens_koshur_text = file_2.read()

with open('tagged_result','w',encoding='utf-8') as fd:        
    for key in elements:
        if '\u0900' <= key <= '\u097f':
            fd.write(f"{key}: dogri\n")
        elif '\u0030' <= key <= '\u0039':
            fd.write(f"{key}: numbers\n")    
        elif '\u0041' <= key <= '\u005A' or '\u0061' <= key <= '\u007A':
            fd.write(f"{key}: english\n")
        elif key in tokens_Urdu_text:
            fd.write(f"{key}: urdu\n")
        elif key in tokens_koshur_text:
            fd.write(f"{key}: koshur\n")
        else:
            fd.write(f"{key}: unknown\n")