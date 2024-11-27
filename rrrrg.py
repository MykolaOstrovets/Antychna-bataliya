from tkinter import *
from PIL import Image,ImageTk
import pygame

import threading
import random
pygame.init()
import time
Mus1=pygame.mixer.Sound(file="Musik.mp3")
Mus1_play=pygame.mixer.Channel(5)
Knife=pygame.mixer.Sound(file="Меч.mp3")
Knife_play=pygame.mixer.Channel(0)
Knife_sound=0
Knife_sound_1=0
Rux=pygame.mixer.Sound(file="Рух.mp3")
Rux_play=pygame.mixer.Channel(1)
Rux_sound=0
Rux_sound_1=0
Kin=pygame.mixer.Sound(file="Kin.mp3")
Kin_play=pygame.mixer.Channel(2)
Kin_sound=0
Kin_sound_1=0
# Ініціалізація pygame
Slon=pygame.mixer.Sound(file="Slon.mp3")
Slon_play=pygame.mixer.Channel(3)
Slon_sound=0
Slon_sound_1=0
Knife_play.set_volume(0.06)
Rux_play.set_volume(0.06)
Slon_play.set_volume(0.04)
Kin_play.set_volume(0.06)

# Завантаження звукового файлу
Stril=pygame.mixer.Sound(file="Strila.mp3")
Stril_play=pygame.mixer.Channel(4)
Stril_sound=0
Stril_sound_1=0
Stril_play.set_volume(0.06)
Mus1.set_volume(0.06)
# Функція для відтворення звуку, коли змінна дорівнює 1
       # Затримка, щоб уникнути надмірного навантаження

# Змінна для контролю


# Запуск потоку для контролю відтворення звуку


Romb=None


def Mus():
    while True:
        
       if not Mus1_play.get_busy():
               Mus1_play.play(Mus1) 
       time.sleep(2)



Musik_play=threading.Thread(target=Mus)
Musik_play.start()

# Головне вікно

root = Tk()
ekran_w=root.winfo_screenwidth()
ekran_h=root.winfo_screenheight()
ekran_w=int(ekran_w)
ekran_h=int(ekran_h)
root.geometry(f"500x308+{(ekran_w-500)//2}+{(ekran_h-308)//2}")
root.resizable()
OREL1=PhotoImage(file="Orel1.gif")
OR=Image.open("Orel.png")
OREL=ImageTk.PhotoImage(OR)
monet=Image.open("moneta.png")
moneta=ImageTk.PhotoImage(monet)
Піхота=PhotoImage(file="Піхота.gif")
Кінота=PhotoImage(file="Кінота.gif")
Слони=PhotoImage(file="Слони.gif")
Лучники=PhotoImage(file="Лучники.gif")
Правила=PhotoImage(file="Правила.gif")
# Завантаження зображення
image=Image.open("luk.png")
image1=Image.open("luk1.png")
redluk311=Image.open("luk3.png")
redluk411=Image.open("luk4.png")
redluk41=ImageTk.PhotoImage(redluk411)
redluk31=ImageTk.PhotoImage(redluk311)
redluk11=ImageTk.PhotoImage(image1)
redluk=ImageTk.PhotoImage(image)
m=Image.open("b.png")
Sound_im1=Image.open("Sound-.png")
Sound_im1=Sound_im1.resize((35,35),Image.BICUBIC)
Sound_image1=ImageTk.PhotoImage(Sound_im1)

Sound_im=Image.open("Sound.png")
Sound_im=Sound_im.resize((35,35),Image.BICUBIC)
Sound_image=ImageTk.PhotoImage(Sound_im)
Sound_im2=Image.open("Sound.png")
Sound_im2=Sound_im2.resize((22,22),Image.BICUBIC)
Sound_image3=ImageTk.PhotoImage(Sound_im2)
mg1 =ImageTk.PhotoImage(m)  # Переконайтеся, що файл існує в каталозі
redluk0=PhotoImage(file="redluk0.gif")
redluk1=PhotoImage(file="redluk1.gif")
redluk2=PhotoImage(file="redluk2.gif")
redluk3=PhotoImage(file="redluk3.gif")
redluk4=PhotoImage(file="redluk4.gif")
blueluk0=PhotoImage(file="blueluk0.gif")
blueluk1=PhotoImage(file="blueluk1.gif")
blueluk2=PhotoImage(file="blueluk2.gif")
blueluk3=PhotoImage(file="blueluk3.gif")
blueluk4=PhotoImage(file="blueluk4.gif")
red0=PhotoImage(file="red0.gif")
red1=PhotoImage(file="red1.gif")
red2=PhotoImage(file="red2.gif")
red3=PhotoImage(file="red3.gif")
red4=PhotoImage(file="red4.gif")
blue0=PhotoImage(file="blue0.gif")
blue1=PhotoImage(file="blue1.gif")
blue2=PhotoImage(file="blue2.gif")
blue3=PhotoImage(file="blue3.gif")
blue4=PhotoImage(file="blue4.gif")
redleg0=PhotoImage(file="redleg0.gif")
redleg1=PhotoImage(file="redleg1.gif")
redleg2=PhotoImage(file="redleg2.gif")
redleg3=PhotoImage(file="redleg3.gif")
redleg4=PhotoImage(file="redleg4.gif")
blueleg0=PhotoImage(file="blueleg0.gif")
blueleg1=PhotoImage(file="blueleg1.gif")
blueleg2=PhotoImage(file="blueleg2.gif")
blueleg3=PhotoImage(file="blueleg3.gif")
blueleg4=PhotoImage(file="blueleg4.gif")
redkin0=PhotoImage(file="redkin0.gif")
redkin1=PhotoImage(file="redkin1.gif")
redkin2=PhotoImage(file="redkin2.gif")
redkin3=PhotoImage(file="redkin3.gif")
redkin4=PhotoImage(file="redkin4.gif")
bluekin0=PhotoImage(file="bluekin0.gif")
bluekin1=PhotoImage(file="bluekin1.gif")
bluekin2=PhotoImage(file="bluekin2.gif")
bluekin3=PhotoImage(file="bluekin3.gif")
bluekin4=PhotoImage(file="bluekin4.gif")
blueslon0=PhotoImage(file="blueslon0.gif")
blueslon1=PhotoImage(file="blueslon1.gif")
blueslon2=PhotoImage(file="blueslon2.gif")
blueslon3=PhotoImage(file="blueslon3.gif")
blueslon4=PhotoImage(file="blueslon4.gif")
redslon0=PhotoImage(file="redslon0.gif")
redslon1=PhotoImage(file="redslon1.gif")
redslon2=PhotoImage(file="redslon2.gif")
redslon3=PhotoImage(file="redslon3.gif")
redslon4=PhotoImage(file="redslon4.gif")
Ширма1=PhotoImage(file="Ширма1.gif")
Ширма2=PhotoImage(file="Ширма2.gif")
OREL2=PhotoImage(file="Orel2.gif")
OREL3=PhotoImage(file="Orel3.gif")
# Відображення зображення в інтерфейсі
image_label = Label(root, image=mg1)
image_label.image = mg1  # Зберігаємо посилання на зображення
image_label.place(x=-2, y=100)
image_label.config(bg="#660000")
# Кнопка "Почати"
def sound_up2(a):
    
    a=int(a)/100
    if a==0:
        sound01.config(image=Sound_image1)
    else:
        sound01.config(image=Sound_image)
    Knife_play.set_volume(0.12*a)
    Rux_play.set_volume(0.12*a)
    Slon_play.set_volume(0.08*a)
    Kin_play.set_volume(0.12*a)
    Stril_play.set_volume(0.12*a)
def sound_up1(a):
    a=int(a)
    if a==0:
        sound00.config(image=Sound_image1)
    else:
        sound00.config(image=Sound_image)
    
    Mus1.set_volume(0.12*(a/100))



wind_sound=Toplevel(root,bg="#660000")
wind_sound.geometry(f"500x200+{(ekran_w-500)//2}+{(ekran_h-200)//2}")
l01=Label(wind_sound,text="Музика",bg="#660000", font=("Arial", 20))
l02=Label(wind_sound,text="Звуки гри",bg="#660000", font=("Arial", 20) )
sound00=Label(wind_sound,image=Sound_image,bg="#660000")
sound00.place(x=230,y=90)
l01.place(x=20,y=90)
l02.place(x=20,y=130)
sound01=Label(wind_sound,image=Sound_image,bg="#660000")
sound01.place(x=230,y=130)
orel1=Label(wind_sound,image=OREL,bg="#660000")
orel1.place(x=0,y=-5)
scrol=Scale(wind_sound,width=20,length=200,orient=HORIZONTAL,showvalue=0,command=sound_up1,activebackground="black",bg="black",highlightbackground="#660000",sliderrelief="groove")
scrol.set(50)
scrol1=Scale(wind_sound,width=20,length=200,orient=HORIZONTAL,showvalue=0,command=sound_up2,activebackground="black",bg="black",highlightbackground="#660000",sliderrelief="groove")
scrol1.place(x=270,y=140)
scrol1.set(50)
scrol.place(x=270,y=100)
windov=Toplevel(root)
windov.geometry(f"500x500+{(ekran_w-500)//2}+{(ekran_h-500)//2}")
a=1
l10=Label(windov, text="", font=("Arial", 20), image=Правила)
l10.place(x=0,y=0)
Назад=Button(windov, text="<Назад", font=("Arial", 20,),command=lambda:гортання(1),activebackground="#660000",bg="#660000")
Далі=Button(windov, text=" Далі>", font=("Arial", 20,),command=lambda:гортання(2),activebackground="#660000",bg="#660000")
Назад.place(x=120,y=440)
Далі.place(x=250,y=440)
windov.withdraw()
wind_sound.withdraw()
windov.iconbitmap('icon.ico')
wind_sound.iconbitmap('icon.ico')
wind_sound.title("Антична баталія")
def гортання(ц):
    global a
    
    if ц==1 and a>1:
        a-=1
    elif ц==2 and a<5:
        a+=1
    if a==1:
        l10.config(image=Правила)
    elif a==2:
        l10.config(image=Піхота)
    elif a==3:
        l10.config(image=Кінота)
    elif a==4:
        l10.config(image=Слони)
    elif a==5:
        l10.config(image=Лучники)
iad=1
def Sound_windov(w):
    global Paysa
    Paysa=3
    global iad
    iad=w
    wind_sound.deiconify()
    root.withdraw()
    root1.withdraw()
def wind(w):

    global Paysa
    Paysa=3
    l10.config(image=Правила)
    
    global iad
    iad=w
    global a
    a=1
    windov.deiconify()
    root.withdraw()
    root1.withdraw()
def close1():
    global iad
    if iad==1:
        root.deiconify()
    else:
        root1.deiconify()
    windov.withdraw()
    wind_sound.withdraw()
windov.protocol("WM_DELETE_WINDOW",close1)
wind_sound.protocol("WM_DELETE_WINDOW",close1)


label = Label(root, text="", font=("Arial", 20), image=OREL)
label.config(bg="#660000")
label.place(x=0, y=0)
button = Button(root, text="Почати", font=("Arial", 20,))
button.config(bg="#660000",activebackground="#660000")
root["bg"]="#660000"
button.place(y=250, x=190)
# Написи
instruc=Button(root,text=" ? ", font=("Arial", 10,),activebackground="#660000",bg="#660000",command=lambda:wind(1))
instruc.place(x=473,y=0)

root1 = Toplevel(root)  # Створюємо нове вікно
root1.geometry(f"1245x775+{(ekran_w-1245)//2}+10")
root1.withdraw()
root1.iconbitmap("icon.ico")
root1.config(bg="#660000")
sound21=Button(root, image=Sound_image3, font=("Arial", 15,),activebackground="#660000",bg="#660000",command=lambda:Sound_windov(1))
sound21.place(x=445,y=0)
instruc1=Button(root1, text=" ? ", font=("Arial", 15,),activebackground="#660000",bg="#660000",command=lambda:wind(2))
instruc1.place(x=1200,y=5)
c = Canvas(root1, width=1041, height=601,highlightthickness=0)
c.place(x=100, y=100)
c.config(bg="#660000")
L=[[0 for _ in range(15)] for _ in range(26)] 
    # Масив для подальшого використання
orel=Label(root1,image=OREL,bg="#660000")
orel.place(x=350,y=-5)
LUK2=[]
LUK1=[]
LUK3=[]
LUK4=[]
LUK11=[]
LUK12=[]
LUK13=[]
LUK14=[]
A = [[0 for _ in range(15)] for _ in range(26)]  # Створюємо масив A
B = [[0 for _ in range(15)] for _ in range(26)]
C = [[0 for _ in range(15)] for _ in range(26)]
P= [[0 for _ in range(15)] for _ in range(26)]# Завантажуємо зображення для сітки
mg = PhotoImage(file="ПУстота.gif")  # Важливо завантажити зображення ще раз для сітки
c.image = mg  # Зберігаємо посилання на зображення
Peremoga=0
    # Відображення зображення на Canvas
for x in range(26):
    for y in range(15):
        if A[x][y] == 0:
            c.create_image(x * 40 + 22, y * 40 + 22, image=mg, anchor='center')
root.resizable(width=False, height=False)
root1.resizable(width=False, height=False)
windov.resizable(width=False, height=False)
b1=Button(root1, font=("Arial", 20,),image=redleg0, command=lambda:вибор(1),bg="#660000")
b2=Button(root1, font=("Arial", 20,),image=redkin0, command=lambda:вибор(2),bg="#660000")
b3=Button(root1, font=("Arial", 20,),image=redslon0, command=lambda: вибор(3),bg="#660000")
b4=Button(root1, font=("Arial", 20,),image=mg, command=lambda: вибор(0),bg="#660000")
b5=Button(root1, font=("Arial", 20,),image=redluk0, command=lambda: вибор(4),bg="#660000")
l1=Label(root1, text="легіонери", font=("Arial", 15,),bg="#660000")
Money=500

Sound_button=Button(root1, font=("Arial", 20,),activebackground="#660000",image=Sound_image,bg="#660000",command=lambda:Sound_windov(2) )
Sound_button.place(x=1155,y=5)
m=Label(root1,image=moneta,bg="#660000")
plata=Label(root1, text=Money, font=("Arial", 30,),bg="#660000")
l2=Label(root1, text="кінота", font=("Arial", 15,),bg="#660000")
l3=Label(root1, text="бойові слони", font=("Arial", 15,),bg="#660000" )
l4=Label(root1, font=("Arial", 15,),bg="#660000" )
l5=Label(root1, font=("Arial", 15,),bg="#660000" )
def вибор(w):
    global a
    # Скидаємо колір кнопок на початковий (можна вказати будь-який)
    b1.config(bg="SystemButtonFace")  # "SystemButtonFace" - стандартний колір для кнопки
    b2.config(bg="SystemButtonFace")
    b3.config(bg="SystemButtonFace")
    b4.config(bg="SystemButtonFace")
    b5.config(bg="SystemButtonFace")# "SystemButtonFace" - стандартний колір для кнопки
   
    if w == 1:
        b1.config(bg="green")
        a = 1
    elif w == 2:
        b2.config(bg="green")
        a = 2
    elif w == 3:
        b3.config(bg="green")
        a = 3
    elif w==0:
         b4.config(bg="green")
         a=0
    elif w==4:
         b5.config(bg="green")
         a=4
def close():
        root.destroy()
def close2():
    global  Slon_sound
    global Slon_sound_1
    global Stril_sound
    global Stril_sound_1
    Stril_play.stop()
    Stril_sound=0
    Stril_sound_1=0
    Stril_play.stop()
    Stril_sound=0
    Stril_sound_1=0
    global  Knife_sound
    global Knife_sound_1
    global  Kin_sound
    global Kin_sound_1
    
    Kin_play.stop()
    Kin_sound=0
    Kin_sound_1=0
    Knife_play.stop()
    Knife_sound=0
    Knife_sound_1=0
    global  Rux_sound
    global Rux_sound_1
    
    Rux_play.stop()
    Rux_sound=0
    Rux_sound_1=0
    windov.withdraw()
    global Peremoga
    Peremoga=0
    global A
    global B
    global C
    global P
    global L
    root1.withdraw()
    root.deiconify()
    
    L=[[0 for _ in range(15)] for _ in range(26)] 
    A = [[0 for _ in range(15)] for _ in range(26)]  # Створюємо масив A
    B = [[0 for _ in range(15)] for _ in range(26)]
    C = [[0 for _ in range(15)] for _ in range(26)]
    P = [[0 for _ in range(15)] for _ in range(26)]
    
    
        
    label.config(text="", font=("Arial", 20),image=OREL)
    button.config( text="Почати", font=("Arial", 20,))
    
    Button2.config( text="Почати", font=("Arial", 20,),command=lambda:onego(1,0))
    Button2.place(x=570,y=704)
    c.delete("all") 
    for x in range(26):
        for y in range(15):
             c.create_image(x * 40 + 22, y * 40 + 22, image=mg, anchor='center')
        
        

Paysa=1
def End(r):
    global  Slon_sound
    global Slon_sound_1
    global Stril_sound
    global Stril_sound_1
    Stril_play.stop()
    Stril_sound=0
    Stril_sound_1=0
    Stril_play.stop()
    Stril_sound=0
    Stril_sound_1=0
    global  Knife_sound
    global Knife_sound_1
    global  Kin_sound
    global Kin_sound_1
    
    Kin_play.stop()
    Kin_sound=0
    Kin_sound_1=0
    Knife_play.stop()
    Knife_sound=0
    Knife_sound_1=0
    global  Rux_sound
    global Rux_sound_1
    
    Rux_play.stop()
    Rux_sound=0
    Rux_sound_1=0
    windov.withdraw()
    global Peremoga
    Peremoga=0
    global A
    global B
    global C
    global P
    global L
    root1.withdraw()
    root.deiconify()
    
    L=[[0 for _ in range(15)] for _ in range(26)] 
    A = [[0 for _ in range(15)] for _ in range(26)]  # Створюємо масив A
    B = [[0 for _ in range(15)] for _ in range(26)]
    C = [[0 for _ in range(15)] for _ in range(26)]
    P = [[0 for _ in range(15)] for _ in range(26)]
    
    if r==1:
        
        label.config(text="Нічия", font=("Arial", 20),image=OREL1)
        button.config( text="Заново", font=("Arial", 20,))
    elif r==2:
        label.config(text="Перший гравець переміг", font=("Arial", 20),image=OREL2)
        button.config( text="Заново", font=("Arial", 20,))
    elif r==3:
        label.config(text="Другий  гравець переміг", font=("Arial", 20),image=OREL3)
        button.config( text="Заново", font=("Arial", 20,))
        Peremoga=0
    root.update()
    Button2.config( text="Почати", font=("Arial", 20,),command=lambda:onego(1,0))
    Button2.place(x=570,y=704)
    c.delete("all") 
    for x in range(26):
        for y in range(15):
             c.create_image(x * 40 + 22, y * 40 + 22, image=mg, anchor='center')
X1=None
Y1=None
def run(e):
    c.unbind("<ButtonPress-1>")
    c.unbind("<ButtonRelease-1>")
    c.unbind("<Motion>")
    b1.place(x=-500,y=100)
    b2.place(x=-505,y=200)
    b3.place(x=-505,y=300)
    b4.place(x=-505,y=400)
    b5.place(x=-505,y=400)
    l1.place(x=-505,y=160)
    l2.place(x=-505,y=260)
    l3.place(x=-505,y=360)
    l4.place(x=-505,y=360)
    l5.place(x=-500)
    global  Stril_sound
    global Stril_sound_1       
    global  Slon_sound
    global Slon_sound_1
    global DESTR
    global LUK1
    global LUK2
    global LUK3
    global LUK4
    global LUK11
    global LUK12
    global LUK13
    global LUK14
    global Paysa
    global Knife_sound
    global Knife_sound_1
    global Rux_sound
    global Rux_sound_1
    global Kin_sound
    global Kin_sound_1
    while True:
        try:
            if Paysa==0:
                twogo(0)
            
                root1.update()
                c.update()
            elif Paysa==3:
                Button2.config(text=" У бій  ", font=("Arial", 20,),command= start )
                Knife_play.stop()
                Knife_sound=0
                Knife_sound_1=0
                Rux_play.stop()
                Rux_sound=0
                Rux_sound_1=0
                Kin_play.stop()
                Kin_sound=0
                Kin_sound_1=0
                Slon_play.stop()
                Slon_sound=0
                Slon_sound_1=0
                Stril_play.stop()
                Stril_sound=0
                Stril_sound_1=0
                break
            
            elif Paysa==1:
                onego(3,0)
                Stril_play.stop()
                Stril_sound=0
                Stril_sound_1=0
                Knife_play.stop()
                Knife_sound=0
                Knife_sound_1=0
                Rux_play.stop()
                Rux_sound=0
                Rux_sound_1=0
                Kin_play.stop()
                Kin_sound=0
                Kin_sound_1=0
                Slon_play.stop()
                Slon_sound=0
                Slon_sound_1=0
                break
            if Paysa==2:
                onego(4,1)
                Knife_play.stop()
                Knife_sound=0
                Knife_sound_1=0
                Rux_play.stop()
                Rux_sound=0
                Rux_sound_1=0
                Kin_play.stop()
                Kin_sound=0
                Kin_sound_1=0
                Slon_play.stop()
                Slon_sound=0
                Slon_sound_1=0
                Stril_play.stop()
                Stril_sound=0
                Stril_sound_1=0
                break
        
            if Peremoga==1:
                time.sleep(1)
                End(1)
                
                break
            if Peremoga==2:
                time.sleep(1)
                End(2)
            
                break
            if Peremoga==3:
                time.sleep(1)
                End(3)
            
                break
            if not Knife_play.get_busy():
                Knife_sound_1=0
                
            if Knife_sound==1 and Knife_sound_1==0:
                Knife_sound_1=1
                Knife_play.play(Knife)
            if Knife_sound==0:
                Knife_play.stop()
            Knife_sound=0
            if not Rux_play.get_busy():
                Rux_sound_1=0
                
            if Rux_sound==1 and Rux_sound_1==0:
                Rux_sound_1=1
                Rux_play.play(Rux)
            if Rux_sound==0:
                Rux_play.stop()
            Rux_sound=0

            if not Kin_play.get_busy():
                Kin_sound_1=0
                
            if Kin_sound==1 and Kin_sound_1==0:
                Kin_sound_1=1
                Kin_play.play(Kin)
            if Kin_sound==0:
                Kin_play.stop()
            Kin_sound=0

            if not Slon_play.get_busy():
                Slon_sound_1=0
                
            if Slon_sound==1 and Slon_sound_1==0:
                Slon_sound_1=1
                Slon_play.play(Slon)
            if Slon_sound==0:
                
                Slon_play.stop()
            Slon_sound=0
            if not Stril_play.get_busy():
                Stril_sound_1=0
                
            if Stril_sound==1 and Stril_sound_1==0:
                Stril_sound_1=1
                
                Stril_play.play(Stril)
            if Stril_sound==0:
                
                Stril_play.stop()
            Stril_sound=0   


            
            root1.update()
            c.update()
            for fr in range(1,11):
                time.sleep(0.1)
            
                for i in LUK1:
                
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if y>=0 and x<=25:
                    
                        if P[x][y-1]==2 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,0,-40)
                    else:
                        c.move(i,4000,0)
                    root1.update()
                    c.update()
                for i in LUK3:
                
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if y<14 and x<25:
                        if P[x][y+1]==2 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,0,40)
                    else:
                        c.move(i,4000,0)
                    root1.update()
                    c.update()
                for i in LUK2:
                
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if x<25:
                        if P[x+1][y]==2 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,40,0)
                    else:
                        c.move(i,4000,0)    
                    root1.update()
                    c.update()
                for i in LUK4:
                    root1.update()
                    c.update()
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if x<=25 and x>=0:
                        if P[x-1][y]==2 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,-40,0)
                    else:
                        c.move(i,4000,0)
                    root1.update()
                    c.update()
                for i in LUK11:
                
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if y>0 and x<=25:
                    
                        if P[x][y-1]==1 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,0,-40)
                    else:
                        c.move(i,4000,0)
                    root1.update()
                    c.update()
                for i in LUK13:
                
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if y<14 and x<25:
                        if P[x][y+1]==1 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,0,40)
                    else:
                        c.move(i,4000,0)
                    root1.update()
                    c.update()
                for i in LUK12:
                
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if x<25:
                        if P[x+1][y]==1 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,40,0)
                    else:
                        c.move(i,4000,0)    
                    root1.update()
                    c.update()
                for i in LUK14:
                    root1.update()
                    c.update()
                    i=int(i)
                
                    (dx,dy)=c.coords(i)
                
                    x=dx//40
                    y=dy//40
                    x=int(x)
                    y=int(y)
                    if x<=25 and x>=0:
                        if P[x-1][y]==1 or fr==10:
                            c.move(i,4000,0)
                        c.move(i,-40,0)
                    else:
                        c.move(i,4000,0)
                    root1.update()
                    c.update()
            
            LUK2=[]
            LUK1=[]     
            LUK3=[]
            LUK4=[]
            LUK12=[]
            LUK11=[]     
            LUK13=[]
            LUK14=[]
        except:
            break
            
            
            
       
            
      
        
def stop():
    global Knife_sound
    global Knife_sound_1
    global Paysa
    global  Rux_sound
    global Rux_sound_1
    global  Kin_sound
    global Kin_sound_1
    global Slon_sound
    global Slon_sound_1
    Slon_play.stop()
    Slon_sound=0
    Slon_sound_1=0
    Kin_play.stop()
    Kin_sound=0
    Kin_sound_1=0
    Rux_play.stop()
    Rux_sound=0
    Rux_sound_1=0
    Paysa=3
    Button2.config(text=" У бій  ", font=("Arial", 20,),command= start )
    Knife_play.stop()
    Knife_sound=0
    Knife_sound_1=0
def start():
    Button2.config(text=" Пауза ", font=("Arial", 20,),command= stop )
    global Paysa
    Paysa=0
    run(0)
def tw(event):
    
    
    
    
    global Paysa
    if (event.char=="P" or event.char=="p" or event.char== "З" or event.char=="з"  ) and Paysa==0:
        Paysa=2
        
    elif (event.char=="W" or event.char=="w" or event.char== "ц" or event.char=="Ц"  ) and Paysa==0:
        
        Paysa=1
        
root1.bind("<Key>",tw)
PTR=[[0 for _ in range(15)] for _ in range(26)] 
def twogo(t):
    
    global Slon_sound
    global Rux_sound
    global Kin_sound
    PTR=[[0 for _ in range(15)] for _ in range(26)] 
    global Peremoga
    global DESTR
    def rux1(x,y):
        if  C[x][y]==1 and y!=0 :
                
                ron=random.choice([1,0])
                ron1=1
                r3=random.choice([1,0])
                if A[x][y-1]==0 and PTR[x][y]==0 :
                    try:
                        if C[x+1][y-1]==4 and r3==0:
                            AA[x][y]=A[x][y]
                            BA[x][y]=B[x][y]
                            CA[x][y]=C[x][y]
                            PA[x][y]=P[x][y]
                            
                        else:
                            Kin_sound=1
                
                            AA[x][y-1]=A[x][y]
                            A[x][y-1]=10
                            BA[x][y-1]=B[x][y]
                            CA[x][y-1]=C[x][y]
                            PA[x][y-1]=P[x][y]
                            PTR[x][y-1]=1
                    except:
                        1+1
                
                    
                
                else:
                    AA[x][y]=A[x][y]
                    BA[x][y]=B[x][y]
                    CA[x][y]=C[x][y]
                    PA[x][y]=P[x][y]
                    

        else:
            AA[x][y]=A[x][y]
            BA[x][y]=B[x][y]
            CA[x][y]=C[x][y]
            PA[x][y]=P[x][y]
            
    def rux4(x,y):
        
        if C[x][y]==4 and x-1!=-1 :
                
                ron=random.choice([1,0])
                ron1=1
                if A[x-1][y]==0 and PTR[x][y]==0:
                    PTR[x-1][y]=1
                    AA[x-1][y]=A[x][y]
                    BA[x-1][y]=B[x][y]
                    CA[x-1][y]=C[x][y]
                    PA[x-1][y]=P[x][y]
                    Kin_sound=1
                elif A[x-1][y]==10 :
                    
                    AA[x][y]=A[x][y]
                    BA[x][y]=B[x][y]
                    CA[x][y]=C[x][y]
                    PA[x][y]=P[x][y]
                        
               
                else:
                    
                    AA[x][y]=A[x][y]
                    BA[x][y]=B[x][y]
                    CA[x][y]=C[x][y]
                    PA[x][y]=P[x][y]
        else:
            
            AA[x][y]=A[x][y]
            BA[x][y]=B[x][y]
            CA[x][y]=C[x][y]
            PA[x][y]=P[x][y]
    def rux3(x,y):
            
            if C[x][y]==3 and y+1!=15 :
                
                
                ron=random.choice([1,0])
                ron1=1
                r1=random.choice([1,0])
                if A[x][y+1]==0 and AA[x][y+1]==0 and PTR[x][y]==0 and y<15:
                    if y+2<=14 and r1==0 :
                        
                        if  C[x][y+2]==1 :
                            AA[x][y]=A[x][y]
                            BA[x][y]=B[x][y]
                            CA[x][y]=C[x][y]
                            PA[x][y]=P[x][y]
                            
                           
                        elif  C[x+1][y+1]==4 :
                            AA[x][y]=A[x][y]
                            BA[x][y]=B[x][y]
                            CA[x][y]=C[x][y]
                            PA[x][y]=P[x][y]
                            
                       
                        else:
                            PTR[x][y+1]=1
                            AA[x][y+1]=A[x][y]
                            BA[x][y+1]=B[x][y]
                            CA[x][y+1]=3
                            A[x][y+1]=10
                            PA[x][y+1]=P[x][y]
                            Kin_sound=1
                            
                
                
                        
                    
                    
                    else:
                        Kin_sound=1
                        PTR[x][y+1]=1
                        AA[x][y+1]=A[x][y]
                        BA[x][y+1]=B[x][y]
                        CA[x][y+1]=C[x][y]
                        A[x][y+1]=10
                        PA[x][y+1]=P[x][y]
                       
               
                    
                else:
                   
                    AA[x][y]=A[x][y]
                    BA[x][y]=B[x][y]
                    CA[x][y]=C[x][y]
                    PA[x][y]=P[x][y]
    
    def rux2(x,y):
        if x+1<=25 :
               
                
                r=random.choice([0,1])
                if A[x+1][y]==0 and AA[x+1][y]==0 and x<26 and PTR[x][y]==0:
                    
                    if y<15:
                        
                        if  C[x+1][y+1]==1  and r==0: 
                            AA[x][y]=A[x][y]
                            BA[x][y]=B[x][y]
                            CA[x][y]=C[x][y]
                            PA[x][y]=P[x][y]
                            
                    if y>0:
                        if  C[x+1][y-1]==1  and r==0: 
                            AA[x][y]=A[x][y]
                            BA[x][y]=B[x][y]
                            CA[x][y]=C[x][y]
                            PA[x][y]=P[x][y]
                            

                            
                        
                    if x+2<=25 and r==0 :
                        
                        if C[x+2][y]==4  and r==0:
                            AA[x][y]=A[x][y]
                            BA[x][y]=B[x][y]
                            CA[x][y]=C[x][y]
                            PA[x][y]=P[x][y]
                           
                            
                            
                        
                        
                        
                            
                            
                    if AA[x][y]==0:
                                Kin_sound=1
                                AA[x+1][y]=A[x][y]
                                BA[x+1][y]=B[x][y]
                                CA[x+1][y]=2
                                A[x+1][y]=10
                                PA[x+1][y]=P[x][y]
                                PTR[x+1][y]=1
                            
                            
                    
                       
                    
            
                
                    
                    
                else:
                    
                    AA[x][y]=A[x][y]
                    BA[x][y]=B[x][y]
                    CA[x][y]=C[x][y]
                    PA[x][y]=P[x][y]
        else:
                     AA[x][y]=A[x][y]
                     BA[x][y]=B[x][y]
                     CA[x][y]=C[x][y]
                     PA[x][y]=P[x][y]
                    

    global A
    global P
    global a
    global Button2
    global A
    global B
    global C
    global P
    global c
    global L
    global LUK4
    global Knife_sound
    global Stril_sound
   
    AA= [[0 for _ in range(15)] for _ in range(26)]  # Створюємо масив A
    BA= [[0 for _ in range(15)] for _ in range(26)]
    CA = [[0 for _ in range(15)] for _ in range(26)]
    PA= [[0 for _ in range(15)] for _ in range(26)]
    for x in range(26):
        for y in range(15):
            if A[x][y]==4:
                
                
                if C[x][y]==2:
                    sl=0
                    lo=0
                    Stril_sound=1
                    for redfs in range(1,11):
                        
                        luk=x+redfs
                        if L[x][y]==0:
                                
                                A[x][y]=1
                                lo=1
                        if luk<25 and lo==0:
                            
                               
                            if  P[luk][y]!=0 and P[luk][y]!=P[x][y] and L[x][y]>0 and lo==0:
                                B[luk][y]=B[luk][y]-1
                                
                                L[x][y]=L[x][y]-1
                                lo=1
                                sl=1
                                
                                
                            elif redfs==10 and L[x][y]>0 and sl==0:
                                L[x][y]=L[x][y]-1
                                B[luk][y]=B[luk][y]-1
                                sl=1
                        elif sl==0 and lo==0:
                            L[x][y]=L[x][y]-1
                            lo=1
                            sl=1
                                

                       
                            
                            
                        
                            
                        
                if C[x][y]==1:
                    sl1=0
                    lo=0
                    Stril_sound=1
                    for redfs1 in range(1,11):
                        
                        
                        luk=y-redfs1
                        if L[x][y]==0:
                                
                                A[x][y]=1
                                lo=1
                        if luk>=0 and lo==0:
                            
                               
                            if P[x][luk]!=0 and P[x][luk]!=P[x][y]  and L[x][y]>0:
                                B[x][luk]=B[x][luk]-1
                                
                                L[x][y]=L[x][y]-1
                                lo=1
                                sl1=1
                                
                            elif redfs1==10 and L[x][y]>0 and sl1==0:
                                B[x][luk]=B[x][luk]-1
                                L[x][y]=L[x][y]-1
                                sl1=1
                            
                        elif sl1==0 and lo==0 :
                            L[x][y]=L[x][y]-1
                            lo=1
                            sl=1
                if C[x][y]==3:
                    sl1=0
                    lo=0
                    Stril_sound=1
                    for redfs1 in range(1,11):
                        
                        
                        luk=y+redfs1
                        if L[x][y]==0:
                                
                                A[x][y]=1
                                lo=1
                        if luk<15 and lo==0:
                            
                               
                            if  P[x][luk]!=0 and P[x][luk]!=P[x][y] and L[x][y]>0:
                                B[x][luk]=B[x][luk]-1
                                L[x][y]=L[x][y]-1
                                lo=1
                                sl1=1
                                
                            elif redfs1==10 and L[x][y]>0 and sl1==0:
                                B[x][luk]=B[x][luk]-1
                                L[x][y]=L[x][y]-1
                                sl1=1
                        elif sl1==0 and lo==0:
                            L[x][y]=L[x][y]-1
                            lo=1
                            sl=1
                if C[x][y]==4:
                    sl1=0
                    sl=0
                    lo=0
                    Stril_sound=1
                    for redfs in range(1,11):
                        
                        luk=x-redfs
                        if L[x][y]==0:
                                
                                A[x][y]=1
                                lo=1
                        if luk>0 and lo==0:
                            
                               
                            if  P[luk][y]!=0 and P[luk][y]!=P[x][y]and L[x][y]>0:
                                B[luk][y]=B[luk][y]-1
                                L[x][y]=L[x][y]-1
                                lo=1
                                sl=1
                                
                            elif redfs==10 and L[x][y]>0 and sl==0:
                                L[x][y]=L[x][y]-1
                                B[luk][y]=B[luk][y]-1
                                sl=1
                            
                        elif sl==0 and lo==0:
                            L[x][y]=L[x][y]-1
                            lo=1
                            sl=1     
                    

                
              
            if A[x][y]==1 or A[x][y]==2:
                    
                   ron=random.choice([1,0])
                   ron1=1
            else:
                    
                    ron=random.choice([2,0])
                    ron1=2
            if A[x][y]!=0 and A[x][y]!=4 and C[x][y]==1 and y-1!=-1:
                
                if P[x][y]!=P[x][y-1] and P[x][y-1]!=0:
                  
                    Knife_sound=1
                    if B[x][y-1]<=2:
                        B[x][y-1]=B[x][y-1]-ron
                    else:
                        B[x][y-1]=B[x][y-1]-ron1
           
            if  A[x][y]!=0 and C[x][y]==4 and A[x][y]!=4 and x-1!=-1:
                if P[x-1][y]!=P[x][y] and P[x-1][y]!=0:
                    Knife_sound=1
                    if B[x-1][y]<=2:
                        B[x-1][y]=B[x-1][y]-ron
                    else:
                        B[x-1][y]=B[x-1][y]-ron1
            
            if A[x][y]!=0 and C[x][y]==3 and A[x][y]!=4 and y+1!=15 :         
                if P[x][y]!=P[x][y+1] and P[x][y+1]!=0:
                    
                    Knife_sound=1
                    if B[x][y+1]<=2:
                        B[x][y+1]=B[x][y+1]-ron
                    else:
                        B[x][y+1]=B[x][y+1]-ron1
            
            if A[x][y]!=0 and C[x][y]==2 and A[x][y]!=4 and x+1!=26:         
                    
                if P[x][y]!=P[x+1][y] and P[x+1][y]!=0:
                    
                    Knife_sound=1
                    
                    if B[x+1][y]<=2:
                        B[x+1][y]=B[x+1][y]-ron
                    else:
                        B[x+1][y]=B[x+1][y]-ron1
            




                
    for t in range(25):
        PTR1=PTR
        for x in range(26):
            for y in range(15):
                if(A[x][y]==1 or A[x][y]==3 )and C[x][y]==1 and y-1!=-1  :
              
                
                
                    
                    r3=random.choice([1,0])
                    if A[x][y-1]==0 and PTR[x][y]==0 :
                        if C[x+1][y-1]==4 and r3==0:
                            AA[x][y]=A[x][y]
                            BA[x][y]=B[x][y]
                            CA[x][y]=C[x][y]
                            PA[x][y]=P[x][y]
                            
                        else:
                            
                
                            AA[x][y-1]=A[x][y]
                            A[x][y-1]=10
                            
                            Rux_sound=1
                            BA[x][y-1]=B[x][y]
                            CA[x][y-1]=C[x][y]
                            PA[x][y-1]=P[x][y]
                            A[x][y]=0
                            B[x][y]=0
                            P[x][y]=0
                            C[x][y]=0
                            PTR[x][y-1]=1
                        
                
                    
                
                    
                    else:
                        AA[x][y]=A[x][y]
                        BA[x][y]=B[x][y]
                        CA[x][y]=C[x][y]
                        PA[x][y]=P[x][y]
                       

            
                if (A[x][y]==1 or A[x][y]==3 )and C[x][y]==4 and x-1!=-1:
               
                    if A[x-1][y]==0 and PTR[x][y]==0 :
                     
                        AA[x-1][y]=A[x][y]
                        BA[x-1][y]=B[x][y]
                        CA[x-1][y]=C[x][y]
                        PA[x-1][y]=P[x][y]
                        PTR[x-1][y]=1
                        A[x][y]=0
                        B[x][y]=0
                        P[x][y]=0
                        C[x][y]=0
                        Rux_sound=1
                    elif A[x-1][y]==10:
                        AA[x][y]=A[x][y]
                        BA[x][y]=B[x][y]
                        CA[x][y]=C[x][y]
                        PA[x][y]=P[x][y]
                        
                        
              
                
               
                    else:
                    
                        AA[x][y]=A[x][y]
                        BA[x][y]=B[x][y]
                        CA[x][y]=C[x][y]
                        PA[x][y]=P[x][y]
                        
                elif (A[x][y]==1 or A[x][y]==3) and C[x][y]==2 and x+1!=26:
                    
                  
                    r=random.choice([0,1])
                    if A[x+1][y]==0 and x<26 and PTR[x][y]==0:
                        if y<14:
                        
                            if  C[x+1][y+1]==1  and r==0: 
                                AA[x][y]=A[x][y]
                                BA[x][y]=B[x][y]
                                CA[x][y]=C[x][y]
                                PA[x][y]=P[x][y]
                              
                        if y>0:
                            if  C[x+1][y-1]==1  and r==0: 
                                AA[x][y]=A[x][y]
                                BA[x][y]=B[x][y]
                                CA[x][y]=C[x][y]
                                PA[x][y]=P[x][y]
                     

                            
                        
                        if x+2<=25 and r==0 :
                        
                            if C[x+2][y]==4  and r==0:
                                AA[x][y]=A[x][y]
                                BA[x][y]=B[x][y]
                                CA[x][y]=C[x][y]
                                PA[x][y]=P[x][y]
                          
                            
                            
                        
                        
                        
                            
                            
                        if AA[x][y]==0:
                                Rux_sound=1
                                AA[x+1][y]=A[x][y]
                                BA[x+1][y]=B[x][y]
                                CA[x+1][y]=2
                                A[x+1][y]=10
                                PA[x+1][y]=P[x][y]
                                PTR[x+1][y]=1
                               
                               
                            










                      
              
                    
                
                
                    
                        
                    else:
                        AA[x][y]=A[x][y]
                        BA[x][y]=B[x][y]
                        CA[x][y]=C[x][y]
                        PA[x][y]=P[x][y]
                        
                elif( A[x][y]==1 or A[x][y]==3 )and C[x][y]==3 and y+1!=15 :
              
                    r1=random.choice([1,0])
                    if A[x][y+1]==0 and AA[x][y+1]==0 and y<15 and PTR[x][y]==0 :
                        if y+2<=14 and r1==0 :
                        
                            if  C[x][y+2]==1 :
                                AA[x][y]=A[x][y]
                                BA[x][y]=B[x][y]
                                CA[x][y]=C[x][y]
                                PA[x][y]=P[x][y]
                                
                           
                            try:
                                if  C[x+1][y+1]==4 :
                                    AA[x][y]=A[x][y]
                                    BA[x][y]=B[x][y]
                                    CA[x][y]=C[x][y]
                                    PA[x][y]=P[x][y]
                                   
                                elif AA[x][y]==0:
                                    Rux_sound=1
                                    AA[x][y+1]=A[x][y]
                                    BA[x][y+1]=B[x][y]
                                    CA[x][y+1]=3
                                    A[x][y+1]=10
                                    PA[x][y+1]=P[x][y]
                                    PTR[x][y+1]=1
                                    
                                    A[x][y]=0
                                    B[x][y]=0
                                    P[x][y]=0
                                    C[x][y]=0
                           
                            except:
                                if AA[x][y]==0:
                                    Rux_sound=1
                                    AA[x][y+1]=A[x][y]
                                    BA[x][y+1]=B[x][y]
                                    CA[x][y+1]=3
                                    A[x][y+1]=10
                                    PA[x][y+1]=P[x][y]
                                    PTR[x][y+1]=1
                                    A[x][y]=0
                                    B[x][y]=0
                                    P[x][y]=0
                                    C[x][y]=0
                       
                        
                            
                
                
                        
                    
                    
                        else:
                            Rux_sound=1
                            AA[x][y+1]=A[x][y]
                            BA[x][y+1]=B[x][y]
                            CA[x][y+1]=C[x][y]
                            A[x][y+1]=10
                            PA[x][y+1]=P[x][y]
                            PTR[x][y+1]=1
                            A[x][y]=0
                            B[x][y]=0
                            P[x][y]=0
                            C[x][y]=0
                
                    
                    
                
                
                    
                    
                    else:
                        AA[x][y]=A[x][y]
                        BA[x][y]=B[x][y]
                        CA[x][y]=C[x][y]
                        PA[x][y]=P[x][y]
                     
                elif A[x][y]==2 :
                    d=1
                    d1=1
                    if C[x][y]==2 and A[x][y]==2 and x<26 and PTR[x][y]==0:
                        try:
                            if A[x+1][y]==0 and A[x+2][y]==0 and x+2<=25:
                                try:
                                    if  (A[x+2][y+1]!=0 and A[x+2][y+1]!=10  and C[x+2][y+1]==1) or (A[x+1][y+1]!=0 and A[x+1][y+1]!=10  and C[x+1][y+1]==1) :
                                        d=0
                                except:
                                  d=d  
                                try:
                                    if y>0:
                                        if  (A[x+2][y-1]!=0 and A[x+2][y-1]!=10  and C[x+2][y-1]==3) or (A[x+1][y-1]!=0 and A[x+1][y-1]!=10  and C[x+1][y-1]==3) :
                                            d=0
                                except:
                                    d=d   
                                try:
                                    if x+3<=26:
                                        if  (A[x+3][y]!=0 and A[x+3][y]!=10  and C[x+3][y]==4):
                                            d=0
                            
                                except:
                                   d=d
                            else:
                                d=0
                        except:
                            d=0
                        
                    
                        if d==0:
                            
                            rux2(x,y)
                        else:
                            Kin_sound=1
                            PTR[x+2][y]=1
                            AA[x+2][y]=A[x][y]
                            BA[x+2][y]=B[x][y]
                            CA[x+2][y]=C[x][y]
                            PA[x+2][y]=P[x][y]
                            A[x+2][y]=10
                            A[x][y]=0
                            B[x][y]=0
                            P[x][y]=0
                            C[x][y]=0
                            
                    elif C[x][y]==3 and A[x][y]==2 and y<15 and  PTR[x][y]==0:
                        d1=1
                        try:
                            if A[x][y+1]==0 and A[x][y+2]==0 and y<=14:
                            
                                try:
                                    if  (A[x+1][y+2]!=0 and A[x+1][y+2]!=10  and C[x+1][y+2]==4) or (A[x+1][y+1]!=0 and A[x+1][y+1]!=10  and C[x+1][y+1]==4) :
                                        d1=0
                                    
                                except:
                                    d1=d1 
                                try:
                                    if x>0:
                                        if  (A[x-1][y+2]!=0 and A[x-1][y+2]!=10  and C[x-1][y+2]==2) or (A[x-1][y+1]!=0 and A[x-1][y+1]!=10  and C[x-1][y+1]==2) :
                                            d1=0
                                        
                                except:
                                    d1=d1   
                            
                                if Y+3<=15:
                                    if  (A[x][y+3]!=0 and A[x][y+3]!=10  and C[x][y+3]==1):
                                        
                                        d1=0
                            
                        
                            else:
                                d1=0
                            
                        except:
                            d1=d1
                        if d1==0:
                            rux3(x,y)
                            d1=d1
                        
                        else:
                            Kin_sound=1
                            PTR[x][y+2]=1
                            AA[x][y+2]=A[x][y]
                            BA[x][y+2]=B[x][y]
                            CA[x][y+2]=C[x][y]
                            PA[x][y+2]=P[x][y]
                            A[x][y+2]=10
                            A[x][y]=0
                            B[x][y]=0
                            P[x][y]=0
                            C[x][y]=0
                    
                    elif C[x][y]==4 and A[x][y]==2 and x>0 and PTR[x][y]==0:
                        d2=1
                        try:
                            if x-2>0:
                                if A[x-1][y]==0 and A[x-2][y]==0 and AA[x-1][y]==0 and AA[x-2][y]==0 and x<=25:
                                    try:
                                        if  (A[x-2][y+1]!=0 and A[x-2][y+1]!=10  and C[x-2][y+1]==3) or (A[x-1][y+1]!=0 and A[x-1][y+1]!=10  and C[x-1][y+1]==3) and ((A[x-2][y+1]!=0 and A[x-2][y+1]!=10  and C[x-2][y+1]==3) or (AA[x-1][y+1]!=0 and A[x-1][y+1]!=10  and CA[x-1][y+1]==3)) :
                                            d2=0
                                    except:
                                        d2=d2
                                    try:
                                        if y>0:
                                            if (A[x-2][y-1]!=0 and A[x-2][y-1]!=10  and C[x-2][y-1]==3) or (A[x-1][y-1]!=0 and A[x-1][y-1]!=10  and C[x-1][y-1]==3)  :
                                                d2=0
                                    except:
                                        d2=d2   
                                    try:
                                        if x-3>=0:
                                            if  (A[x-3][y]!=0 and A[x-3][y]!=10  and C[x-3][y]==2):
                                                d1=0
                                    except:
                                       d2=d2
                                else:
                                    d2=0
                            else:
                                d2=0
                            
                        except:
                            d2=0
                        if d2==0:
                            rux4(x,y)
                        
                        else:
                            PTR[x-2][y]=1
                            AA[x-2][y]=A[x][y]
                            BA[x-2][y]=B[x][y]
                            CA[x-2][y]=C[x][y]
                            PA[x-2][y]=P[x][y]
                            A[x-2][y]=10
                            Kin_sound=1
                            A[x][y]=0
                            B[x][y]=0
                            P[x][y]=0
                            C[x][y]=0               
                    elif C[x][y]==1 and A[x][y]==2 and PTR[x][y]==0 and y>0:
                        d1=1
                        try:
                            if y-2>0:
                                if A[x][y-1]==0 and A[x][y-2]==0 :
                                    try:
                                        if  ((A[x+1][y-2]!=0 and A[x+1][y-2]!=10  and C[x+1][y-2]==4) or (A[x+1][y-1]!=0 and A[x+1][y-1]!=10  and C[x+1][y-1]==4) )or( (AA[x+1][y-2]!=0   and CA[x+1][y-2]==4) or (AA[x+1][y-1]!=0   and CA[x+1][y-1]==4)) :
                                            d1=0
                                    except:
                                        d1=d1 
                                    try:
                                        if x>0:
                                            if  ((A[x-1][y-2]!=0 and A[x-1][y-2]!=10  and C[x-1][y-2]==2) or (A[x-1][y-1]!=0 and A[x-1][y-1]!=10  and C[x-1][y-1]==2)) or ((AA[x-1][y-2]!=0   and CA[x-1][y-2]==2) or (AA[x-1][y-1]!=0   and CA[x-1][y-1]==2)) :
                                                d1=0
                                    except:
                                        d1=d1   
                                    try:
                                        if Y-3>=0:
                                            if  (A[x][y-3]!=0 and A[x][y-3]!=10  and C[x][y-3]==1):
                                                d1=0
                                    except:
                                       d1=d1
                                else:
                                        d1=0
                        
                            else:
                                d1=0
                            
                        except:
                            d1=0
                        if d1==0:
                            rux1(x,y)
                        
                        else:
                            Kin_sound=1
                            PTR[x][y-2]=1
                            AA[x][y-2]=A[x][y]
                            BA[x][y-2]=B[x][y]
                            CA[x][y-2]=C[x][y]
                            PA[x][y-2]=P[x][y]
                            A[x][y-2]=10         
                                
                        
                    elif PTR[x][y]==1:
                    
                        AA[x][y]=A[x][y]
                        BA[x][y]=B[x][y]
                        CA[x][y]=C[x][y]
                        PA[x][y]=P[x][y]        
                    
                if ((A[x][y]!=0 and A[x][y]!=10 and C[x][y]==0)or A[x][y]==4):
                    
                    AA[x][y]=A[x][y]
                    BA[x][y]=B[x][y]
                    CA[x][y]=C[x][y]
                    PA[x][y]=P[x][y]
                if (C[x][y]==3 and y+1==15) or( C[x][y]==1 and y-1==-1 )or (C[x][y]==2 and x==25) or( C[x][y]==4 and x==0):
                    AA[x][y]=A[x][y]
                    BA[x][y]=B[x][y]
                    CA[x][y]=C[x][y]
                    PA[x][y]=P[x][y]
                
       
        A=AA
        B=BA
        C=CA
        P=PA          
        AA= [[0 for _ in range(15)] for _ in range(26)]  # Створюємо масив A
        BA= [[0 for _ in range(15)] for _ in range(26)]
        CA = [[0 for _ in range(15)] for _ in range(26)]
        PA= [[0 for _ in range(15)] for _ in range(26)]
        
            
               
        
            
                   
            
        
            
    
        
        

    
    
    for x in range(26):
        for y in range(15):
            if B[x][y]<=0:
                A[x][y]=0
                P[x][y]=0
                B[x][y]=0
                C[x][y]=0
          
    
    try:
        c.delete("all")
        # Створення словника для зберігання відповідних зображень
        images = {
    (0, None, None): mg,
    (4,1,0):redluk0, (4,1,1):redluk1,(4,1,2):redluk2,(4,1,3):redluk3,(4,1,4):redluk4,
    (4,2,0):blueluk0, (4,2,1):blueluk1,(4,2,2):blueluk2,(4,2,3):blueluk3,(4,2,4):blueluk4,
    (1, 1, 0): redleg0, (2, 1, 0): redkin0, (3, 1, 0): redslon0,
    (1, 2, 0): blueleg0, (2, 2, 0): bluekin0, (3, 2, 0): blueslon0,
    (1, 1, 1): redleg1, (2, 1, 1): redkin1, (3, 1, 1): redslon1,
    (1, 2, 1): blueleg1, (2, 2, 1): bluekin1, (3, 2, 1): blueslon1,
    (1, 1, 2): redleg2, (2, 1, 2): redkin2, (3, 1, 2): redslon2,
    (1, 2, 2): blueleg2, (2, 2, 2): bluekin2, (3, 2, 2): blueslon2,
    (1, 1, 3): redleg3, (2, 1, 3): redkin3, (3, 1, 3): redslon3,
    (1, 2, 3): blueleg3, (2, 2, 3): bluekin3, (3, 2, 3): blueslon3,
    (1, 1, 4): redleg4, (2, 1, 4): redkin4, (3, 1, 4): redslon4,
    (1, 2, 4): blueleg4, (2, 2, 4): bluekin4, (3, 2, 4): blueslon4,
}
    
# Основний цикл
        red=0
        blue=0
        for x in range(26):
            for y in range(15):
                key = (A[x][y], P[x][y] if A[x][y] != 0 else None, C[x][y] if A[x][y] != 0 else None)
                image = images.get(key, mg)  # mg - зображення за замовчуванням
                c.create_image(x * 40 + 22, y * 40 + 22, image=image, anchor='center')
        for x in range(26):
            for y in range(15):
                if A[x][y]==4 and L[x][y]>0 and P[x][y]==2:
                    if C[x][y]==1:
                        if y>0 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk11, anchor='center')
                            l=c.find_all()
                            
                            LUK11.append(l[-1])
                    if C[x][y]==2:
                        if x<26 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk, anchor='center')
                            l=c.find_all()
                            
                            LUK12.append(l[-1])
                    if C[x][y]==3:
                        if y<15 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk31, anchor='center')
                            l=c.find_all()
                            
                            LUK13.append(l[-1])
                    if C[x][y]==4:
                        if x>0 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk41, anchor='center')
                            l=c.find_all()
                            LUK14.append(l[-1])
                if A[x][y]==4 and L[x][y]>0 and P[x][y]==1:
                    if C[x][y]==1:
                        if y>0 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk11, anchor='center')
                            l=c.find_all()
                            
                            LUK1.append(l[-1])
                    if C[x][y]==2:
                        if x<26 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk, anchor='center')
                            l=c.find_all()
                            
                            LUK2.append(l[-1])
                    if C[x][y]==3:
                        if y<15 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk31, anchor='center')
                            l=c.find_all()
                            
                            LUK3.append(l[-1])
                    if C[x][y]==4:
                        if x>0 :
                            c.create_image((x)* 40 + 22, y * 40 + 22, image=redluk41, anchor='center')
                            l=c.find_all()
                            LUK4.append(l[-1])
                if  P[x][y]==1:
                    red=+1
                elif P[x][y]==2:
                    blue=+1
                if A[x][y]==3:
                    Slon_sound=1
                
        if blue==0 and red==0:
            Peremoga=1
        
        elif blue==0:
            Peremoga=2
        elif red==0:
            Peremoga=3    
    except:
        1+1
def romb(event):
        global Romb
        
        
        global X1
        global Y1
        x,y=event.x,event.y
        c.delete(Romb)
        if X1!=None and Y1!=None:
            
            c.create_rectangle(x, y, X1, Y1,outline='black',width=6)
            
            w=c.find("all")
            Romb=w[-1]
            c.update()
            
            

        
            
            
                
def onego(s,f):
    global Money
    global a
    global Button2
    global A
    global B
    global C
    global P
    global c
    a=0
    if s==1:
        Money=500
        plata.config(text=Money)
        plata.place(x=5,y=47)
        m.place(x=70,y=45)
        b1.config(bg="SystemButtonFace")  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(bg="SystemButtonFace")
        b3.config(bg="SystemButtonFace")
        b4.config(bg="SystemButtonFace")
        b5.config(bg="SystemButtonFace")
        b1.config(image=redleg0)  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(image=redkin0)
        b3.config(image=redslon0)
        b5.config(image=redluk0)
        b4.config(image=mg)
        b1.place(x=5,y=100)
        b2.place(x=5,y=200)
        b3.place(x=5,y=320)
        b4.place(x=5,y=550)
        l1.place(x=5,y=160)
        l2.place(x=5,y=260)
        l3.place(x=5,y=380)
        l1.config(text="піхотинці")
        l2.config(text="кінота")
        l3.config(text="бойові \nслони")
        l4.config(text="лучники")
        l4.place(x=5,y=500)
        l5.config(text="Cтійте")
        b5.place(x=5,y=450)
    if s==2:
        plata.place(x=1120,y=47)
        Money=500
        m.place(x=1190,y=45)
        l4.config(text="лучники")
        l4.place(x=1150,y=460)
        plata.config(text=Money)
        b1.config(bg="SystemButtonFace")  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(bg="SystemButtonFace")
        b3.config(bg="SystemButtonFace")
        b4.config(bg="SystemButtonFace")
        b5.config(bg="SystemButtonFace")
        b1.config(image=blueleg0)  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(image=bluekin0)
        b3.config(image=blueslon0)
        b5.config(image=blueluk0)
        b1.place(x=1150,y=100)
        b2.place(x=1150,y=200)
        b3.place(x=1150,y=320)
        b4.place(x=1150,y=540)
        b5.place(x=1150,y=450)
        l1.place(x=1150,y=160)
        l2.place(x=1150,y=260)
        l3.place(x=1150,y=380)
        l4.place(x=1150,y=500)
    def click1(event):
        global X1
        global Y1
        
        X1,Y1=event.x,event.y
   
    def click(event):
        global Romb
        c.delete(Romb)
        global Money
        global X1
        global Y1
        x1,y1=event.x,event.y
        x1=x1//40
        y1=y1//40
        X1=X1//40
        Y1=Y1//40
        if x1>=X1:
            X_1=1
        else:
            X_1=-1
        if y1>=Y1:
            Y_1=1
        else:
            Y_1=-1
        if 0<=x1<26 and 0<=x1<26 and 0<=y1<15 and 0<=Y1<15:
            for i in range(abs(x1-X1)+1):
                for e in range(abs(y1-Y1)+1):
                    x=X1+(i*X_1)
                    y=Y1+(e*Y_1)
                    
                    if s==3:
                        
                        if P[x][y]==1:
                            
                            if a==1:
                                C[x][y]=1
                            elif a==2:
                                C[x][y]=2
                            elif a==3:
                                C[x][y]=3
                            elif a==4:
                                C[x][y]=4
                            elif a==0:
                                C[x][y]=0
                        
                    if s==4:
                        
                        if P[x][y]==2:
                            
                            if a==1:
                                C[x][y]=1
                            elif a==2:
                                C[x][y]=2
                            elif a==3:
                                C[x][y]=3
                            elif a==4:
                                C[x][y]=4
                            elif a==0:
                                C[x][y]=0
                    if x<13 and s==1 or x>=13 and s==2:
                        
                     
                        
                        if a==0:
                            if A[x][y]==1:
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4:
                                Money+=20
                            A[x][y]=0
                            B[x][y]=0
                            P[x][y]=0
                            L[x][y]=0
                            plata.config(text=Money)
                        if a==1 and s==1 and Money>=10:
                            if A[x][y]==1 :
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4:
                                Money+=20
                            Money=Money-10
                            A[x][y]=1
                            B[x][y]=10
                            P[x][y]=1
                            plata.config(text=Money)
                        elif a==2 and s==1 and Money>=10:
                            if A[x][y]==1  :
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4:
                                Money+=20
                            Money=Money-10
                            A[x][y]=2
                            B[x][y]=10
                            P[x][y]=1
                            plata.config(text=Money)
                        elif a==3 and s==1 and Money>=20:
                            if A[x][y]==1 :
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4:
                                Money+=20
                            Money=Money-20
                            A[x][y]=3
                            B[x][y]=20
                            P[x][y]=1
                            plata.config(text=Money)
                        elif a==4 and s==1 and Money>=20:
                            if A[x][y]==1 :
                                Money+=10
                            if A[x][y]==2 :
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4:
                                Money+=20
                            Money=Money-20
                            A[x][y]=4
                            B[x][y]=10
                            P[x][y]=1
                            L[x][y]=10
                            plata.config(text=Money)
                        elif a==1 and s==2 and Money>=10:
                            if A[x][y]==1 :
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4 :
                                Money+=20
                            Money=Money-10
                            A[x][y]=1
                            B[x][y]=10
                            P[x][y]=2
                            plata.config(text=Money)
                        elif a==2 and s==2  and Money>=10:
                            if A[x][y]==1:
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4:
                                Money+=20
                            Money=Money-10
                            A[x][y]=2
                            B[x][y]=10
                            P[x][y]=2
                            plata.config(text=Money)
                        elif a==3 and s==2  and Money>=20:
                            if A[x][y]==1:
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4 :
                                Money+=20
                            Money=Money-20
                            A[x][y]=3
                            B[x][y]=20
                            P[x][y]=2
                            plata.config(text=Money)
                        elif a==4 and s==2  and Money>=20:
                            if A[x][y]==1:
                                Money+=10
                            if A[x][y]==2:
                                Money+=10
                            if A[x][y]==3 or A[x][y]==4 :
                                Money+=20
                            Money=Money-20
                            A[x][y]=4
                            B[x][y]=10
                            P[x][y]=2
                            L[x][y]=10
                            plata.config(text=Money)
                    c.delete("all")
                   
                    for x in range(26):
                        for y in range(15):
                            if A[x][y] == 0:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=mg, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==1 and C[x][y]==0:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redluk0, anchor='center')
                            elif A[x][y]==1 and P[x][y]==1 and C[x][y]==0:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redleg0, anchor='center')
                            elif A[x][y]==2 and P[x][y]==1 and C[x][y]==0 :
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redkin0, anchor='center')
                            elif A[x][y]==3 and P[x][y]==1 and C[x][y]==0:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redslon0, anchor='center')
            
                            
                            elif A[x][y]==4 and P[x][y]==2 and C[x][y]==0:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueluk0, anchor='center')    
                            elif A[x][y]==1 and P[x][y]==2 and C[x][y]==0:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueleg0, anchor='center')
                            elif A[x][y]==2 and P[x][y]==2 and C[x][y]==0:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=bluekin0, anchor='center')
                            elif A[x][y]==3 and P[x][y]==2 and C[x][y]==0 :
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueslon0, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==2 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueluk1, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==2 and C[x][y]==2:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueluk2, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==2 and C[x][y]==3:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueluk3, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==2 and C[x][y]==4:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueluk4, anchor='center')    
            
            
                            
            
                            elif A[x][y] == 4 and P[x][y]==1 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redluk1, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==1 and C[x][y]==2:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redluk2, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==1 and C[x][y]==3:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redluk3, anchor='center')
                            elif A[x][y] == 4 and P[x][y]==1 and C[x][y]==4:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redluk4, anchor='center')    
                            elif A[x][y]==1 and P[x][y]==1 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redleg1, anchor='center')
                            elif A[x][y]==2 and P[x][y]==1 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redkin1, anchor='center')
                            elif A[x][y]==3 and P[x][y]==1 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redslon1, anchor='center')
            
            
                                
                            elif A[x][y]==1 and P[x][y]==2 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueleg1, anchor='center')
                            elif A[x][y]==2 and P[x][y]==2 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=bluekin1, anchor='center')
                            elif A[x][y]==3 and P[x][y]==2 and C[x][y]==1:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueslon1, anchor='center')
            
            
                                
                            elif A[x][y]==1 and P[x][y]==1 and C[x][y]==2:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redleg2, anchor='center')
                            elif A[x][y]==2 and P[x][y]==1 and C[x][y]==2 :
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redkin2, anchor='center')
                            elif A[x][y]==3 and P[x][y]==1 and C[x][y]==2:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redslon2, anchor='center')
            
            
                                
                            elif A[x][y]==1 and P[x][y]==2 and C[x][y]==2:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueleg2, anchor='center')
                            elif A[x][y]==2 and P[x][y]==2 and C[x][y]==2:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=bluekin2, anchor='center')
                            elif A[x][y]==3 and P[x][y]==2 and C[x][y]==2 :
                                 c.create_image(x * 40 + 22, y * 40 + 22, image=blueslon2, anchor='center')
            
            
                                 
                            elif A[x][y]==1 and P[x][y]==1 and C[x][y]==3:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redleg3, anchor='center')
                            elif A[x][y]==2 and P[x][y]==1 and C[x][y]==3:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redkin3, anchor='center')
                            elif A[x][y]==3 and P[x][y]==1 and C[x][y]==3:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redslon3, anchor='center')
            
            
                                
                            elif A[x][y]==1 and P[x][y]==2 and C[x][y]==3:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueleg3, anchor='center')
                            elif A[x][y]==2 and P[x][y]==2 and C[x][y]==3:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=bluekin3, anchor='center')
                            elif A[x][y]==3 and P[x][y]==2 and C[x][y]==3:
                                 c.create_image(x * 40 + 22, y * 40 + 22, image=blueslon3, anchor='center')
            
            
                                 
                            elif A[x][y]==1 and P[x][y]==1 and C[x][y]==4:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redleg4, anchor='center')
                            elif A[x][y]==2 and P[x][y]==1 and C[x][y]==4:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redkin4, anchor='center')
                            elif A[x][y]==3 and P[x][y]==1 and C[x][y]==4:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=redslon4, anchor='center')
            
            
                                
                            elif A[x][y]==1 and P[x][y]==2 and C[x][y]==4:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=blueleg4, anchor='center')
                            elif A[x][y]==2 and P[x][y]==2 and C[x][y]==4:
                                c.create_image(x * 40 + 22, y * 40 + 22, image=bluekin4, anchor='center')
                            elif A[x][y]==3 and P[x][y]==2 and C[x][y]==4:
                                 c.create_image(x * 40 + 22, y * 40 + 22, image=blueslon4, anchor='center')
                    if s==1:
                        
                        c.create_image(780, 304, image=Ширма2, anchor='center')
                    if s==2:
                         c.create_image(260, 304, image=Ширма1, anchor='center')
        X1=None
        Y1=None

 
    
        
    if  s==3:
        m.place(x=-1250,y=45)
        plata.place(x=-1000)
        Button2.place(x=570,y=704)
        b1.config(bg="SystemButtonFace")  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(bg="SystemButtonFace")
        b3.config(bg="SystemButtonFace")
        b4.config(bg="SystemButtonFace")
        b5.config(bg="SystemButtonFace")
        ws=c.find_all()
        try:
           c.delete(ws[390])
        except:
            s=s
        b1.config(image=red1)  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(image=red2)
        b3.config(image=red3)
        b4.config(image=red0)
        b5.config(image=red4)
        b1.place(x=5,y=100)
        b2.place(x=5,y=220)
        b3.place(x=5,y=350)
        b4.place(x=5,y=580)
        b5.place(x=5,y=460)
        l1.place(x=5,y=160)
        l1.config(text="Ідіть \nв верх")
        l2.config(text="Ідіть \nв вправо")
        l3.config(text="Ідіть \nв вниз")
        l4.config(text="Ідіть \nу ліво")
        l5.config(text="Cтійте")
        l2.place(x=5,y=280)
        l3.place(x=5,y=400)
        l4.place(x=5,y=520)
        l5.place(x=5,y=640)
        if f==1:
            Button2.config(text=" У бій  ", command=start)
        else:
            Button2.config(text="Готово", command=lambda:onego(4,0))
    if s==1:
        
        c.create_image(780, 304, image=Ширма2, anchor='center')
        Button2.config(text="Готово", font=("Arial", 20,),command=lambda:onego(2,0))
    elif s==2:
        ws=c.find_all()
        c.delete(ws[-1])
        c.create_image(260, 304, image=Ширма1, anchor='center')
        Button2.config(text="Готово", font=("Arial", 20,),command=lambda:onego(3,0))
    if  s==4:
        
        m.place(x=-1250,y=45)
        plata.place(x=-1000)
        Button2.place(x=570,y=704)
        b1.config(bg="SystemButtonFace")  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(bg="SystemButtonFace")
        b3.config(bg="SystemButtonFace")
        b4.config(bg="SystemButtonFace")
        b5.config(bg="SystemButtonFace")
        b1.config(image=blue1)  # "SystemButtonFace" - стандартний колір для кнопки
        b2.config(image=blue2)
        b3.config(image=blue3)
        b4.config(image=blue0)
        b5.config(image=blue4)
        b1.place(x=1150,y=100)
        b2.place(x=1150,y=220)
        b3.place(x=1150,y=350)
        b4.place(x=1150,y=580)
        b5.place(x=1150,y=460)
        l1.place(x=1150,y=160)
        l1.config(text="Ідіть \nв верх")
        l2.config(text="Ідіть \nв вправо")
        l3.config(text="Ідіть \nв вниз")
        l4.config(text="Ідіть \nу ліво")
        l5.config(text="Cтійте")
        l2.place(x=1150,y=280)
        l3.place(x=1150,y=400)
        l4.place(x=1150,y=520)
        l5.place(x=1150,y=640)
        if f==1:
            Button2.config(text="Готово", font=("Arial", 20,),command=lambda:onego(3,1 ))
        else:
            Button2.config(text=" У бій  ", font=("Arial", 20,),command= start )

    c.bind("<ButtonPress-1>",click1)
    c.bind("<ButtonRelease-1>",click)
    c.bind("<Motion>",romb)


    
# Відображаємо зображення


Button2=Button(root1, text="Почати", font=("Arial", 20,),command=lambda:onego(1,0),bg="#660000",activebackground="#660000")
Button2.place(x=570,y=704)
root1.withdraw()
# Створення другого вікна для сітки
def почати():
    root1.deiconify()
    root.withdraw()
    

root.iconbitmap("icon.ico")
root.title("Антична баталія")
root1.title("Антична баталія")
windov.title('Антична баталія')
button.config(command=почати)
root.protocol("WM_DELETE_WINDOW",close)
root1.protocol("WM_DELETE_WINDOW",close2)
root.mainloop
