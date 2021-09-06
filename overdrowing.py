def amongusdraw():   
    BODY_COLOR = 'red'
    GLASS_COLOR = 'skyblue'
    t = turtle.Turtle()
    body()
    glass()
    backpack()
    turtle.done()
    
def body():
	t.pensize(30) # Размер кисти

	t.fillcolor(BODY_COLOR) # Цвет заполнения
	t.begin_fill()

	# Сторона справа
	t.right(90)
	t.forward(50)
	t.right(180)
	t.circle(40, -180)
	t.right(180)
	t.forward(200)

	# Голова
	t.right(180)
	t.circle(100, -180)

	# Сторона слева
	t.backward(20)
	t.left(15)
	t.circle(500, -20)
	t.backward(20)

	t.circle(40, -180)
	t.left(7)
	t.backward(50)

	t.up()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.down()

	t.right(240)
	t.circle(50, -70)

	t.end_fill()


# Рисуем очки
def glass():
	# Передвигаем черепашку
	t.up()
	t.right(230)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.right(90)
	t.down()

	# Устанавливаем цвет
	t.fillcolor(GLASS_COLOR)
	t.begin_fill()

	t.right(150)
	t.circle(90, -55)

	t.right(180)
	t.forward(1)
	t.right(180)
	t.circle(10, -65)
	t.right(180)
	t.forward(110)
	t.right(180)

	t.circle(50, -190)
	t.right(170)
	t.forward(80)

	t.right(180)
	t.circle(45, -30)

	t.end_fill()


# Рисуем рюкзак
def backpack():
	t.up()
	t.right(60)
	t.forward(100)
	t.right(90)
	t.forward(75)

	t.fillcolor(GLASS_COLOR)
	t.begin_fill()

	t.down()
	t.forward(30)
	t.right(255)

	t.circle(300, -30)
	t.right(260)
	t.forward(30)
	t.end_fill()


    

def echo(text):
    print(text)

def echoserve(text):
    print('SERVER:', text)

def echodrow(text, color=0, align=0, style=0):
    pass

def draw():
    didgit = turtle.textinput('PRESS TOKEN', 'WRITE YOUR IDANTIFICATION ID')
    TURTLE_SIZE = 20

    screen = Screen()

    yertle = Turtle(shape="turtle", visible=False)
    yertle.ht()
    circle = turtle.Turtle()
    circle.ht()
    yertle.penup()
    yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
    yertle.pendown()
    yertle.showturtle()
    turtle.write('''
    PENTAGON HACKING
    ''')

    screen = turtle.Screen()

    image = r"F:\10им\razuvaev\vzlom\original.gif"

    screen.addshape(image)
    turtle.shape(image)
    

    yertle.left(270)
    yertle.forward(300)
    yertle.right(270)
    yertle.forward(350)


    turtle.title("Turtle Drawing")
    circle.shape("turtle")
    circle.pensize(5)
    circle.pencolor("cyan")

    circle.dot(20)
    circle.penup()
    circle.goto(0, -100)
    circle.pendown()
    circle.circle(100)
    screen = turtle.Screen()
    image2 = r"F:\10им\razuvaev\vzlom\s120.gif"
    
    screen.addshape(image2)
    
    turtle.shape(image2)
    x = turtle.color('red')
    s = '''
        INJECT SUCCESS
        PRESS ANY KEY
    '''
    turtle.write(s, align = 'center', font = (x, 30, 'bold'))
    
    turtle.exitonclick()
