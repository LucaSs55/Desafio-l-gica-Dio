print(20*'+=')
print('Classificador de nível de Herói')
print(20*'+=')

nome = str(print('Digite o nome do héroi:'))
xp = int(input('Digite a experiência do herói: (XP)'))
if xp < 1000:
    print('Classificação: Ferro')
elif xp >= 1001 and xp <= 2000:
    print('Classificação: Bronze')
elif xp >= 2001 and xp <= 5000:
    print('Classificação: Prata')
elif xp >= 6001 and xp <= 7000:
    print('Classificação: Ouro')
elif xp >= 7001 and xp <= 8000:
    print('Classificação: Platina')
elif xp >= 8001 and xp <= 9000:
    print('Classificação: ascendente')
elif xp >= 9001 and xp <= 10000:
    print('Classificação: Imortal')
else:
    print('Classificação: Radiante, parabéns!')

