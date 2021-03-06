# -*- coding: utf-8 -*-

CYR_CHAR_PAIRS = (
    (u'Й', u'й'),
    (u'Ц', u'ц'),
    (u'У', u'у'),
    (u'К', u'к'),
    (u'Е', u'е'),
    (u'Н', u'н'),
    (u'Г', u'г'),
    (u'Ш', u'ш'),
    (u'Щ', u'щ'),
    (u'З', u'з'),
    (u'Х', u'х'),
    (u'Ъ', u'ъ'),
    (u'Ф', u'ф'),
    (u'Ы', u'ы'),
    (u'В', u'в'),
    (u'А', u'а'),
    (u'П', u'п'),
    (u'Р', u'р'),
    (u'О', u'о'),
    (u'Л', u'л'),
    (u'Д', u'д'),
    (u'Ж', u'ж'),
    (u'Э', u'э'),
    (u'Я', u'я'),
    (u'Ч', u'ч'),
    (u'С', u'с'),
    (u'М', u'м'),
    (u'И', u'и'),
    (u'Т', u'т'),
    (u'Ь', u'ь'),
    (u'Б', u'б'),
    (u'Ю', u'ю'),
    (u'І', u'і'),
    (u'Ї', u'ї'),
    (u'Ґ', u'ґ'),
    (u'Є', u'є'),
    (u'Ё', u'ё'),
)

def low_string(s):
    t = ''
    pairs = dict(CYR_CHAR_PAIRS)
    for c in s:
        try:
            w = pairs[c]
            t += w
        except KeyError:
            t += c
    return t

def up_string(s):
    t = ''
    pairs = dict((reversed(x) for x in CYR_CHAR_PAIRS))
    for c in s:
        try:
            w = pairs[c]
            t += w
        except KeyError:
            t += c
    return t
    
def capitalize(s):
    t = low_string(s)
    words = t.split()
    new_words = []
    for w in words:
        if len(w) > 0:
            new_words.append(up_string(w[0]) + low_string(w[1:]))
    return ' '.join(new_words)
            
