""" 2. Da se napravi funkcija koja ke prima broj kako parametar i da pecati dali brojot e paren ili ne paren"""

def check_number(broj):
    if broj%2 == 0:
        print(f'Бројот {broj} е парен')
    else:
        print(f'Бројот {broj} е непарен')

br = int(input('Внесете еден број:'))
check_number(br)
