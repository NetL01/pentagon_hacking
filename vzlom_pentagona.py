import time
from turtle import Turtle, Screen
import turtle

def initialization():
    print('Инициализация...')
    time.sleep(1)
    print('1%')
    print('11%')
    print('46%')
    time.sleep(0.3)
    print('72%')
    time.sleep(0.6)
    print('97%')
    time.sleep(0.25)
    print('100%')
    print('Сервер успешно запущен')
    print('\\Подготовка компонентов//')
    print('12%')
    time.sleep(0.16)
    print('15%')
    print('32%')
    time.sleep(0.5)
    print('57%')
    time.sleep(0.25)
    print('89%')
    print('100%')
    print('Конфигурация выполнена')
    print('Синхронизация с BOTNET')
    time.sleep(0.5)
    print('...')
    print('Синхронизация выполнена')
    print('stable build')
    auth()

def auth(gen_pass=0):
    a = input('Команда:')
    if a == '$vzlom_pentagona':
        autorization()
    elif a == '$help':
        print('[$vzlom_pentagona(no param)]')
        print('[$vzlom_fsb(no param)]')
        print('[$exit(no param)]')
        print('[$gen_password]')
        print('[$vzlom_halmetovoi]')
        print('[$vzlom_bobra]')
        auth()
    elif a == '$gen_password':
        gen_password()
    else:
        print('Exception: no command')
        auth()

def gen_password():
    time.sleep(1)
    print('Процесс генерации уникального шифрованного пароля пошёл')
    a = int(input('Выберите стандарт ключа SSH: '))
    print('Подготовка к генерации пароля по ключу SSH:', a)
    time.sleep(2)
    print('11%')
    time.sleep(0.3)
    print('27%')
    time.sleep(0.5)
    print('56%')
    time.sleep(1.2)
    print('98%')
    time.sleep(0.7)
    print('100%')
    time.sleep(0.4)
    gen_pass = '5KJk-rf-03@qtj!I3WH&ltTU-4IA-w04#f'
    print('Your generated password: ', gen_pass)
    auth(gen_pass)
    
def autorization(gen_pass=0):
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
        time.sleep(1)
        print('ЗА ВАМИ УЖЕ ВЫЕХАЛИ!')
        time.sleep(1)
        print('Мы уже поднимаемся!')
        time.sleep(0.7)
        print('На каком вы этаже?')
        a = int(input('Этаж: '))
        if a >= 1:
            print('мы уже спускаемся')
            time.sleep(1)
            print('БЕГИ УЖЕ БЛТБ ДЕБИЛ НАХЕНА ТЫ С КОМПОМ ОБЩАЕШЬСЯ')
        else:
            print('БЕГИ УЖЕ БЛТБ ДЕБИЛ НАХЕНА ТЫ С КОМПОМ ОБЩАЕШЬСЯ')
        time.sleep(1)
        for i in range(100):
            time.sleep(0.5)
            print('бегите')
        auth()
    
    else:
        print('Пароль неверный, самоуничтожение через 10')
        time.sleep(1)
        print('9')
        time.sleep(1)
        print('8')
        time.sleep(1)
        print('7')
        time.sleep(1)
        print('6')
        time.sleep(1)
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('Взрыв!')
        time.sleep(3)
        print('Ха! Шутка! перезапусти программу(пароль от винлокера 123)')
        time.sleep(2)
        print('...')
        autorization()


def main():
    TURTLE_SIZE = 20

    screen = Screen()

    yertle = Turtle(shape="turtle", visible=False)
    yertle.penup()
    yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
    yertle.pendown()
    yertle.showturtle()
    turtle.write('''
    PENTAGON HACKING
    ''')

    screen = turtle.Screen()

    image = r"F:\10им\original.gif"

    screen.addshape(image)
    turtle.shape(image)

    yertle.left(270)
    yertle.forward(300)
    yertle.right(270)
    yertle.forward(350)



    turtle.title("Turtle Drawing")
    circle = turtle.Turtle()
    circle.shape("turtle")
    circle.pensize(5)
    circle.pencolor("cyan")

    circle.dot(20)
    circle.penup()
    circle.goto(0, -100)
    circle.pendown()
    circle.circle(100)
    turtle.exitonclick()
    initialization()    

main()

































