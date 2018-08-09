#Задание 2

#1 Напишите программу которая просит ввести ваши данные имя, фамилию, возраст, адрес, телефон,
# и выводит это все в отформатированной таблице

name = input('Напишите как Вас зовут', )
surname = input('Напишите Вашу фамилию', )
age = input('Напишите Ваш возраст', )
adress = input('Напишите Ваш адрес', )
tel = input('Напишите Ваш телефон', )

template = 'Имя: {name} \n Фамилия: {surname} \n Возраст: {age} \n Адрес: {adress} \n Телефон:{tel}'

print(template.format(name = name, surname = surname, age = age, adress = adress, tel = tel))



