# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:17:22 2021
@author: RAGNYA
"""

# -*- coding: utf-8 -*-
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = " ".join(text.split())
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("।","!<stop>")
    text = text.replace("|","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

split_sentences = split_into_sentences('''Mr. John Johnson Jr. was born in the U.S.A but 
                           earned his Ph.D. in Israel before joining Nike Inc.
                           as an engineer. He also worked at craigslist.org as
                           a business analyst.में उंʼदे बारे च जानने च उत्सुक हा ,  खासकर जे ओह्‌‌ अपने 
                                                             विवाद किʼयां हल करदे न ।  जे चुनेआ गेआ तां जुगती माउंट करने आस्तै  बाद्धू   प्राधिकरण
                                                             दी लाजमी ऐ | तुस चारागाहें च जानवरें दे रिरियाने दियां आवाज़ें गी सुनी सकदे न .  
                                                             कंसिलिएशन दा लक्श एह्‌‌ होंदा ऐ जे मामले कन्नै जुड़े पक्ख   अपने आप   अपनी समस्याएं 
                                                             दा हल तुप्प निकालां 
                           Hi Babes''')

[(print (sentence)) for sentence in split_sentences]