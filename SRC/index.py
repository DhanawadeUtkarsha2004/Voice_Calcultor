from tkinter import *
import math
from pygame import mixer
import speech_recognition

mixer.init()


def click(value):
    ex = entryField.get()
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))
        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(ex)

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a + b

def sub(a,b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

def TAN(a, b):
    print("tan fucntion is triggered")
    a = math.tan(a)
    print(a)
    return a

def SIN(a, b):
    print("sin fucntion is triggered")
    a = math.sin(a)
    print(a)
    return a

def COS(a, b):
    print("cos fucntion is triggered")
    a = math.cos(a)
    print(a)
    return a

def LOG(a,b):
    a = math.log(a)
    print(a)
    return a

def Sinh(a,b):
    print("sinh function is triggered")
    a = math.sinh(a)
    print(a)
    return a

def Cosh(a,b):
    print("cosh function is triggered")
    a = math.cosh(a)
    print(a)
    return a

def Tanh(a,b):
    print("tanh function is triggered")
    a = math.tanh(a)
    print(a)
    return a

def Power(a,b):
    print("power  function is triggered ")
    w = math.pow(a,b)
    print(w)
    return a**b

def factorial(a):
    print ("factorial function is triggered")
    a = math.factorial(a)
    print(a)
    return a

def squareroot(a):
    print ("squareroot function is triggered")
    a = math.sqrt(a)
    print(a)
    return a


operations={'TANGENT':TAN , 'T':TAN ,
            'SINE':SIN , 'SIN':SIN , 'SIGN':SIN,
            'COSINE':COS, 'COS':COS,'square root':squareroot,
            'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,'POWER':Power ,
            'LCM':lcm , 'HCF':hcf,'COSH':Cosh ,'TANH':Tanh,'factorial':factorial  ,
            'MOD':mod ,'REMAINDER':mod ,'MODULUS':mod , 'LOG':LOG ,'LOGARITM': LOG ,'SINH':Sinh}

def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.1)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1])
                    entryField.delete(0,END)
                    entryField.insert(END,result)

                else:
                    pass


        except:
            pass



root = Tk()
root.title('TRIO Scientific Voice Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+500+100')

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3' ,command=audio)
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
