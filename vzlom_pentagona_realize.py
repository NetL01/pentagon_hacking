import time
import os
import sys

class Operations():
    def __init__(self):
        self.dict_func = {'help': self.help, 'vzlom_pentagona': self.vzlom_pentagona}

    def additional_func(self):
        # print(locals())
        # print(sys.argv)
        # locals()[sys.argv[1]](sys.argv[2], sys.argv[3])
        # self.dict_func[sys.argv[1]](sys.argv[2], sys.argv[3])
        try:
            res = sys.argv[3]
            self.dict_func[sys.argv[1]](sys.argv[2], sys.argv[3])
        except IndexError:
            self.dict_func[sys.argv[1]](sys.argv[2])

    def echo(self, ech, *kwargs):
        return ech

    def vzlom_pentagona():
        password = input('Введите код доступа: ')
        if password == '123321':
            print('Процесс пошёл!')
            time.sleep(0.7)
            print('Подготовка к скачиванию информации')
            time.sleep(1)
            print('Процесс будет выполненен одновременно с удалением баз!')
            time.sleep(0.3)
            print('Взлом фаервола 1')
            time.sleep(0.8)
            print('Взлом фаервола 2')
            time.sleep(0.8)
            print('Взлом фаервола 3')
            time.sleep(0.8)
            print('Последний фаервол упал')
            time.sleep(0.8)
            print('Защиты нет')
            time.sleep(0.8)
            print('Запуск процесса создания инфляции')
            time.sleep(0.7)
            print('Запущено!')
            print('Крах экономики США: ')
            time.sleep(0.5)
            print('Выполнено')
            time.sleep(0.3)
            print('Великая депрессия v2.0: ')
            time.sleep(3)
            print('Выполнено')
            time.sleep(0.5)
            print('Подготовка к удалению баз Пентагона...')
            time.sleep(0.8)
            print('33%')
            time.sleep(0.8654)
            print('75%')
            time.sleep(0.5)
            print('88%')
            time.sleep(0.7)
            print('97%')
            time.sleep(0.5)
            print('100%')
            time.sleep(1)
            print('Удаление всех данных США')
            time.sleep(0.8)
            print('Детонация ядерного оружия в шахтах')
            time.sleep(2)
            print('БАБАХ')
            time.sleep(1.5)
            print('Программа проработает ещё 10 секунд, после чего удалиться везде и навсегда!')
            time.sleep(5)
            print('Разработано великим NetL01')
            time.sleep(3)
            print('ЗА ВАМИ УЖЕ ВЫЕХАЛИ')
            time.sleep(1)
            print
            exit()

    def help(self):
        print('[$vzlom_pentagona(no param)]')
        print('[$vzlom_fsb(no param)]')
        print('[$exit(no param)]')
        

class InputBox():
    def __init__(self):
        self.smth = Operations()

    def another_func(self): 
        self.smth.additional_func()


if __name__ == '__main__':
    # start = YandexDiskOperations()
    location = InputBox()
    location.another_func()
