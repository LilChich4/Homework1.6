from os import remove

my_dict = {'Ананас': 'фрукт', 'Баклажан': 'овощ'}
print(my_dict)
print(my_dict['Ананас'])
my_dict['Картофель']='корнеплод'
print(my_dict['Картофель'])
my_dict.update({'Малина': 'ягода',
                          'Фундук': 'орех'})
print(my_dict)
pop = my_dict.pop('Фундук')
print(pop)
print(my_dict)
my_set = {1,3,4,7,7,1,3,2,5,4,6,6}
print(my_set)
my_set.update([11,22,33])
my_set.remove(1)
print(my_set)




