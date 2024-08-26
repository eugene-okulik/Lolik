my_dict = {"tuple": (1, 3, 6, 7, None, 'text', False, 2.42),
           "list": [567, 'hello', 56.67, 'мир-труд-май', False],
           "dict": {'1': 'Lenny Kravitz', '2d': 'Olya', '3,14568': '5.66564', 'False': 'True', 'пять': 'hfp ldf nhb'},
           "set": {1, 7, None, 'text', False, 2.42, 7}}

print(my_dict["tuple"][-1])
my_dict["list"].append(42)
my_dict["list"].pop(1)
my_dict["dict"]['i am a tuple'] = 'good morning'
print(my_dict)
my_dict['set'].add('руки вверх')
print(my_dict)
