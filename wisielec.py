import random
slowa_plik = open('lista_slow.txt', 'r', encoding = 'utf-8')
slowa = slowa_plik.read().split('\n')
slowo = random.choice(slowa)
slowo = list(slowo)
#print(''.join(slowo))

zagadka = list('*' * len(slowo))
print(''.join(zagadka))

wisielec = ["""






_________ 
""", """

         |
         |
         |
         |
         |
_________|
""", """
_________
         |
         |
         |
         |
         |
_________|
""", """
_________
 |       |
         |
         |
         |
         |
_________|
""", """
_________
 |       |
 O       |
         |
         |
         |
_________|
""", """
_________
 |       |
 O       |
/|\      |
         |
         |
_________|
""", """
_________
 |       |
 O       |
/|\      |
/ \      |
         |
_________|
"""]

szanse = 7
while szanse > 0:
    print('Masz jeszcze %d szans' % szanse)
    litera = input('Podaj literę (wpisz "koniec", jeśli chcesz się poddać): ').lower()
    # Rezygnacja z gry
    if litera == 'koniec':
        break
    # Input dłuższy niż pojedyncza litera
    elif len(litera) > 1:
        print('Wpisz tylko jedną literę!')
        print()
    # Trafienie
    elif litera in slowo:
        print('Trafiony!')
        # Podmiana gwiazki w haśle na odgadniętą literę
        liczydlo = 0
        while liczydlo < len(zagadka):
            if slowo[liczydlo] == litera:
                zagadka[liczydlo] = litera
            liczydlo = liczydlo + 1
        print()
    # Pudło
    elif litera not in slowo:
        print('Pudło!')
        print(wisielec[-szanse])
        print()
        szanse = szanse - 1
    if zagadka == slowo:
        print('Zwycięstwo!')
        break
    print(''.join(zagadka))
print('Koniec gry!')