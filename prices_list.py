# Список с ценами на товары

price = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
         70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
         8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

for i in price:
    if type(i) == float:
        i = str(i)
        r, k = i.split('.')
        k = k.replace('0', '')
        if len(k) == 1:
            k = f'{k}0'
        print(f'{r}.{k} руб.')
    else:
        i = str(i)
        print(f'{i} руб.')
