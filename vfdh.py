### ^ - начало строки, $ - конец стр. * - вхождение пред симв от 0 до люб числа, + - от 1 до люб числа раз.
### {5} - предыд выре должно повториться 5 раз, {3, 5} - от 3 до 5 раз,  {,5} - до 5 раз, ? - 0 или 1 раз
###### классы символов:
# \w - любой буквенный символ
# \d - любая цифра
# \s - любой пробелообразный символ (пробелы, таб, ентер)
# \W - любая не буква
# \D - любая не цифра
# \b - бордеры ( как s. но эти симвыолы в резт не вклся)
# m= re.search (regex, string) ищет совпадения в любом месте строки
# m= re.match (re, str) ицет совп в начале строки
# findall ищет все вхождения
# в m хранятся резты поиска, с пом атрибутов можно достать инфу
# группа - часть выря зключенаая в скобки напр abc(def)ge
# группы нумеруются по открывающей скобке
# m.group(0) - находит все выражение, вместо 0 номер строки - часть строки
# чтобы группа не нумеровалась, нужно поставить в начале вырадения ?:
#пример r'(12)(?:w+)(12)' средняя группа не считается
# функц findall() : a=re.findall(u'[^;]+', s) находит все совпадения
#
#
#
#
import re
def open_html('xenokeryx.html'):
    with open ('xenokeryx.html', 'r', encoding='utf-8') as f:
        content=f.read()
    return content
def find_links (content):
    reg=r'<a\s+href="(.*?)">(.*?)</a>'
    links=re.findall (reg, content)
    return links
text=open_html ('xenokeryx.html')
links=find_links(text)
for link in links [:20]:
    print (link[1], '-->', link[0])


    