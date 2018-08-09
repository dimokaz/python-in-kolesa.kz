#Задание 2_2

#1 Напишите программу которая просит ввести ваши данные имя, фамилию, возраст, адрес, телефон,
# и выводит это все в отформатированной таблице

def clean_name(x): #функция очищающая имена и фамилии
    x = x.strip('1234567890.,!@#$%^&*()\'\"+-_[]= ')
    x = x.capitalize()
    return x

def clean_num(x): #функция очищающая номера
    x = x.lower()
    x = x.strip('abcdefghjklmnpqrstuvwxyzяюэьыъщшчцхфутсрпонмлкйизжёедгвба.,!@#$%^&*()[]=-_ \'\" ')
    return x

def clean_adress(x): #функция очищающая адреса
    x = x.strip('.!@#$%^&*()\'\"+_[]= ')
    return x

name = clean_name(input('Напишите как Вас зовут', ))
surname = clean_name(input('Напишите Вашу фамилию', ))
age = int(clean_num(input('Сколько Вам полных лет', )))
adress = clean_adress(input('Напишите Ваш адрес', ))
tel = clean_num(input('Напишите Ваш телефон', ))
sex = input('Укажите свой пол.\n1 - Муж, 2 - Жен')

if age > 18 and age < 28 and sex == '1':
    temp = "Дорогой {name}, военком сегодня приходил адресу {adress}. Ты лучше пока не ходи на улицу."
    print(temp.format(name=name, adress=adress))
elif age > 28 and sex == '1':
    temp = "Дорогой {name} {surname}, военком приходил. Но ушел грустный."
    print(temp.format(name=name, surname=surname))
elif age < 18 and sex == '1':
    temp = "Дорогой {name} родители на даже. Доставай приставку. Звони друзьям.)))"
    print(temp.format(name=name))
elif sex == '2':
    temp = "Дорогая {name} в твой любимый магазин завезли новую коллекцию. Пора...)))"
    print(temp.format(name=name))