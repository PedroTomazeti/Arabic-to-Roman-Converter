import os
import roman


def clear_screen():
    input('\nAperte Enter para continuar...')
    os.system("cls")


def end_screen():
    print('\nFim da aplicação.')
    input('Aperte Enter para finalizar...')


def menu():
    print('-----MENU DE ESCOLHA-----')
    print('1 - Arábico para romano.\n2 - Romano para arábico.')
    option = int(input('Insira a sua escolha: '))
    clear_screen()
    return option


def condicional(parametro):
    if parametro <= 0 or parametro > 2:
        print('\nInsira um valor válido!')
        clear_screen()
        condicional(menu())
    elif parametro == 1:
        arabic = str(input('Insira um número Arábico qualquer: '))
        try:
            arabic = float(arabic)
            arabic = round(arabic)
            arabic = int(arabic)
            numero_arabico_convertido = roman.toRoman(arabic)
        except ValueError:
            print('\nInsira um número válido!')
            clear_screen()
            condicional(menu())
        except roman.OutOfRangeError:
            print('\nInsira um número válido!')
            clear_screen()
            condicional(menu())
        else:
            print(f'O número arábico {arabic} em romano é {numero_arabico_convertido}')
            end_screen()
    else:
        try:
            romano = str(input('Insira um número romano qualquer: '))
            romano = romano.upper()
            numero_romano_convertido = roman.fromRoman(romano)
        except roman.InvalidRomanNumeralError:
            print('\nInsira um número válido!')
            clear_screen()
            condicional(menu())
        else:
            print(f'O número romano {romano} em arábico é {numero_romano_convertido}')
            end_screen()


condicional(menu())
