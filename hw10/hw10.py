import re
def main():
    with open ('lemon.html', 'r', encoding='utf-8') as f:
        text=f.read()
    a='<class="infobox vcard"(?:.|\>+?</table>'
    if re.search (a, text):
        card = re.search(a, text).group()
        b='Семейство(?:.|\n)*?<p>(.+?)'
        if re.search(b, a):
            с = re.search(b, a).group(1)
            with open ('family.txt', 'a', encoding = 'utf-8') as f:
                f.write(с)
        else:
            print('Family type not found.')
            with open ('family.txt', 'a', encoding = 'utf-8') as f:
                f.write('Family type not found.')
    else:
        print('Error!')
        with open ('family.txt', 'a', encoding = 'utf-8') as f:
                f.write('Error!')

    
