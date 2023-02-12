# 07.02.23 - 1 урок

# passw = input('Vvedite pass: ')
# if len(passw) < 6:
#     print('Slishkom korotkii pass')
# else:
#     print('ok')

# passw = input('Vvedite pass: ')
# if len(passw) < 6:
#     print('Slishkom korotkii pass')
# elif passw[:6] == 'qwerty':
#     print('Nenadejnii pass')
# else:
#     print('ok')

# ras = input('Vvedite ras: ')
# if ras[-3:] == 'htm' or ras[-4:] == 'html' or ras[-3:] == 'php':
#     print('Eto web')
# elif ras[-4:] == 'doc' or ras[-4:] == 'docs':
#     print('Eto WORD')
# elif ras[-4:] == 'xls' or ras[-4:] == 'xlsx':
#     print('Eto EXEL')
# elif ras[-4:] == 'zip' or ras[-4:] == 'rar' or ras[-2:] == '7z':
#     print('Eto ARHIV')
# elif ras[-3:] == 'exe':
#     print('Eto PROGA')
# else:
#     print('CHTOTO DRUGOE')

stroka = input('Vvedite stroku: ')
simvol = int(input('Vvedite nomer simvola: '))
za = int(input('Vvedite za: ')) # 12345678

print(stroka[:simvol-1] + stroka[simvol:za] + stroka[simvol-1]+stroka[za:])
# print(stroka[simvol:za])

