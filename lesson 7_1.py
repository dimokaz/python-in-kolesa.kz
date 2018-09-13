#программа поиска данных по телефонной книге база пользователей - dict  - имя, фамилия, возраст, др,
# телефон возможность искать только по имени, только по фамилии, только по возрасту

#создаем тестовую базу
n = {'ivan':222123, 'oleg':222222, 'karl':243456, 'ivan':567687, 'olya':222576, 'marina':546789}
t = [222123, 222222, 243456, 567687, 222576, 546789]
n = ['ivan', 'oleg', 'ivan', 'marina', 'ivan', 'olya']
s = ['ivanov', 'karlov', 'sidorov', None, 'petrov', 'karlova']
a = [18,34,45,23,54,25]


b = [t, n, s, a] #тестовая база

def get_tel(base, first_name = None, surname = None, age = None ):

    import numpy as np
    for li in range(len(base)):
        base[li] = np.array(base[li])

    if first_name == None:
        name_bool = True
    else:
        name_bool = base[1] == first_name
    
    if surname == None:
        surname_bool = True
    else:
        surname_bool = base[2] == surname
    
    if age == None:
        age_bool = True
    else:
        age_bool = base[3] == age

    final_bool = name_bool * surname_bool * age_bool

    tel = base[0]

    result = tel[final_bool]
    print(result)

get_tel(base=b, first_name = 'ivan')
