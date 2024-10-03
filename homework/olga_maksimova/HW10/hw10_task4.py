# List comprehension
# Дан такой кусок прайс листа:

# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# В выполнении не должно быть циклов.
#
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

items = PRICE_LIST.split("\n")
data = [(item.split(' ')[0].strip(), int(item.split(' ')[1][:-1])) for item in items]
new_dict = {key: value for key, value in data}
new_dict = dict(data)

print(new_dict)
