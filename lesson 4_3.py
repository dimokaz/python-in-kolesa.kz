#Задание С
#Реализуйте алгоритм поиска простых чисел "Решето Эратосфена" до заданного числа n

def prime_num_seq(num):
    '''
    Функция возвращает простые числа в последовательности от 1 до num
    :param num: верхнее число последовательности
    :return: возвращает список простых чисел
    '''
    X = list(range(num))
    first = 2
    not_prime_list = []
    
    for j in range(len(X)):
        for i in range(len(X)):# находим не простые числа
            if X[i] % first == 0 and X[i] != first:
                not_prime_list.append(X[i])

        for n in range(len(not_prime_list)): #удаляем непростые числа из последовательности
            X.remove(not_prime_list[n])
        not_prime_list = []

        if max(X) == first: # останавливаем цикл на последнем простом числе
            break

        first = X[X.index(first) + 1]#берем следующее число для поиска не простых чисел
        
    print(X)

prime_num_seq(100)
