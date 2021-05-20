def detect_language(line):
    maxchar = max(line)
    if '\u0c00' <= maxchar <= '\u0c7f':
        return 'telugu'
    elif '\u0900' <= maxchar <= '\u097f':
        return 'hindi'
    return 'english'
print(detect_language('తెలుు'))

# Check tanges based on https://www.ling.upenn.edu/courses/Spring_2003/ling538/UnicodeRanges.html
# Ref: https://stackoverflow.com/questions/19704317/how-to-detect-unicode-character-range-in-python