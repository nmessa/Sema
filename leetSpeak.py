##leetSpeakSimple.py
##Author: nmessa
##Date: 11/22/2024

translate = {'A':'4', 'B':'13', 'C':'(', 'D':'[)','E':'3', 'F':'|=', 'G':'6', 'H':'|-|',
             'I':'|', 'J':'.]', 'K':'|<', 'L':'|_', 'M':'|\/|', 'N':'/\/', 'O':'0', 'P':'|>',
             'Q':'0,', 'R':'|2', 'S':'5', 'T':'7', 'U':'[_]', 'V':'\/', 'W':'\/\/', 'X':'><',
             'Y':"'/", 'Z':'2', ' ':'  '}

phrase = input("Enter a phrase: ").upper()

for letter in phrase:
    print(translate[letter], end = "")

##Sample run
##Enter a phrase: I am teaching Python to Sema
##|  4|\/|  734(|-||/\/6  |>'/7|-|0/\/  70  53|\/|4
