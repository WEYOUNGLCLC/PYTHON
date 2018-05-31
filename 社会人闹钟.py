# -*- coding: UTF-8 -*-
import time,sys,math,_thread
from tkinter import *
from turtle import *

def runnian(a):
    p=""
    if((a%4==0 and a%100!=0) or a%400==0):
        p="闰年 "
    else:
        p = "平年"
    return p

def shuxiang(m):
    p = "今年的生肖是"
    if ((m - 1959) % 12 == 1): p += "鼠"
    if ((m - 1959) % 12 == 2): p += "牛"
    if ((m - 1959) % 12 == 3): p += "虎"
    if ((m - 1959) % 12 == 4): p += "兔"
    if ((m - 1959) % 12 == 5): p += "龙"
    if ((m - 1959) % 12 == 6): p += "蛇"
    if ((m - 1959) % 12 == 7): p += "马"
    if ((m - 1959) % 12 == 8): p += "羊"
    if ((m - 1959) % 12 == 9): p += "猴"
    if ((m - 1959) % 12 == 10): p += "鸡"
    if ((m - 1959) % 12 == 11): p += "狗"
    if ((m - 1959) % 12 == 0): p += "猪"
    return p

def tgdz(year):   #天干地支
    n1=year%10
    n2=year%12
    p=""

    if(n1<=3):
        n1+=7
    else:
        n1-=3
    if(n2<=3):
        n2+=9
    else:
        n2-=3
    if (n1 == 1): p += "甲"
    if (n1 == 2): p += "乙"
    if (n1 == 3): p += "丙"
    if (n1 == 4): p += "丁"
    if (n1 == 5): p += "戊"
    if (n1 == 6): p += "己"
    if (n1 == 7): p += "庚"
    if (n1 == 8): p += "辛"
    if (n1 == 9): p += "壬"
    if (n1 == 10): p += "癸"
    if (n2 == 1): p += "子"
    if (n2 == 2): p += "丑"
    if (n2 == 3): p += "寅"
    if (n2 == 4): p += "卯"
    if (n2 == 5): p += "辰"
    if (n2 == 6): p += "巳"
    if (n2 == 7): p += "午"
    if (n2 == 8): p += "未"
    if (n2 == 9): p += "申"
    if (n2 == 10): p += "酉"
    if (n2 == 11): p += "戌"
    if (n2 == 12): p += "亥"
    p += "年"
    return p

def sett():
    Y = int(u1.get())
    M = int(u2.get())
    D = int(u3.get())
    if(Y>2049 or Y<1970 or M>12 or M<1 or D>31 or D<1):
        print("input error")
    elif(D==31 and (M==4 or M==6 or M==9 or M==11)):
        print("input error")
    elif(D>28 and M==2 and runnian(Y)!=""):
        print("input error")
    else:
        rtime['year']=Y
        rtime['month']=M
        rtime['day']=D
        print("date resetted")
    H = int(u4.get())
    m = int(u5.get())
    S = int(u6.get())
    if(H>23 or H<0 or m>59 or m<0 or S>59 or S<0):
        print("input error")
    else:
        rtime['hour'] = H
        rtime['minute'] = m
        rtime['second'] = S
        print("time resetted")
        print("reset OK")

def reset():
    rtime1["year"] = time.strftime('%Y', time.localtime(time.time()))
    rtime1["month"] = time.strftime('%m', time.localtime(time.time()))
    rtime1["day"] = time.strftime('%d', time.localtime(time.time()))
    rtime1["hour"] = time.strftime('%H', time.localtime(time.time()))
    rtime1["minute"] = time.strftime('%M', time.localtime(time.time()))
    rtime1["second"] = time.strftime('%S', time.localtime(time.time()))
    rtime["year"] = int(rtime1["year"])
    rtime["month"] = int(rtime1["month"])
    rtime["day"] = int(rtime1["day"])
    rtime["hour"] = int(rtime1["hour"])
    rtime["minute"] = int(rtime1["minute"])
    rtime["second"] = int(rtime1["second"])

def drawclock(canvas):
    x = 200  
    y = 200  
    width = 150 + 10 
    for i in range(1, 13):
        arc = 2.0 * math.pi / 12 * i
        new_x = x + width * math.sin(arc)
        new_y = y - width * math.cos(arc)
        canvas.create_text(new_x, new_y, text=str(i))
    for i in range(1,61):
        if(i % 5 != 0):
            arc = 2.0 * math.pi / 60 * i
            new_x = x + width * math.sin(arc)
            new_y = y - width * math.cos(arc)
            canvas.create_text(new_x,new_y,text = "·")

def drawpointer(canvas, hour, minute, second):
    x = 200  
    y = 200  
    hour_width = 70  
    minute_width = 90  
    second_width = 120 
    hour_arc = 2.0 * math.pi * hour / 12
    minute_arc = 2.0 * math.pi * minute / 60
    second_arc = 2.0 * math.pi * second / 60
    canvas.create_line(x,y,x+hour_width * math.sin(hour_arc),y-hour_width*math.cos(hour_arc),width= 6.0,fill='yellow')
    canvas.create_line(x,y,x+minute_width*math.sin(minute_arc),y - minute_width*math.cos(minute_arc),width= 4.0,fill='lightgreen')
    canvas.create_line(x,y,x+second_width*math.sin(second_arc),y - second_width*math.cos(second_arc))
    canvas.create_oval(190, 190, 210, 210, fill='red')

def showtime(app, canvas):
    while 1:
        canvas.create_rectangle(0,0,400,400,fill='white')
        canvas.create_oval(30,30,370,370,fill='lightpink')
        canvas.create_oval(50,50,350,350,fill='lightblue')
        canvas.create_oval(90,90,310,310,fill='white')
        photo = PhotoImage(file='PEGGY.gif')
        canvas.create_image(200,200,image=photo)
        drawclock(canvas)
        drawpointer(canvas, rtime['hour'], rtime['minute'], rtime['second'])
        app.update()
        time.sleep(1)

rtime={}
rtime1={}
rtime1["year"]=time.strftime('%Y',time.localtime(time.time()))
rtime1["month"]=time.strftime('%m',time.localtime(time.time()))
rtime1["day"]=time.strftime('%d',time.localtime(time.time()))
rtime1["hour"]=time.strftime('%H',time.localtime(time.time()))
rtime1["minute"]=time.strftime('%M',time.localtime(time.time()))
rtime1["second"]=time.strftime('%S',time.localtime(time.time()))
rtime["year"]=int(rtime1["year"])
rtime["month"]=int(rtime1["month"])
rtime["day"]=int(rtime1["day"])
rtime["hour"]=int(rtime1["hour"])
rtime["minute"]=int(rtime1["minute"])
rtime["second"]=int(rtime1["second"])
print(rtime1['year'],end="")
print("年",end="")
print(rtime1['month'],end="")
print("月",end="")
print(rtime1['day'],end="")
print("日")

window = Tk()  
window.geometry("400x700") 
window.wm_title('社会人时钟')
canvas = Canvas(window,width=400,height=400)
canvas.pack()

Label1=Label(window, text=rtime1['year']+"年"+rtime1['month']+"月"+rtime1['day']+"日", font=('Arial', 15))   
Label1.pack()
Label2=Label(text=rtime1['hour']+":"+rtime1['minute']+":"+rtime1['second'], font=('Arial', 15))    
Label2.pack()


year = runnian(rtime['year']) + " " + tgdz(rtime['year']) + " " + shuxiang(rtime['year'])
print(year)
Label3=Label(window, text=year, font=('Arial', 15))    
Label3.pack()

Label(window, text = "-------------------------------------------------------------------").pack()
Label(window, text = "请在下面输入你所需要修改的时间日期", font=('Arial', 8)).pack()
Label(window, text = "___________________________________________________________________").pack()
u1 = StringVar()
u2 = StringVar()
u3 = StringVar()
u4 = StringVar()
u5 = StringVar()
u6 = StringVar()
E1 = Entry(window,width= 3, textvariable=u1).place(x=120,y=530,width=40,height=20)
E2 = Entry(window,width= 3, textvariable=u2).place(x=160,y=530,width=20,height=20)
E3 = Entry(window,width= 3, textvariable=u3).place(x=180,y=530,width=20,height=20)
E4 = Entry(window,width= 3, textvariable=u4).place(x=200,y=530,width=20,height=20)
E5 = Entry(window,width= 3, textvariable=u5).place(x=220,y=530,width=20,height=20)
E6 = Entry(window,width= 3, textvariable=u6).place(x=240,y=530,width=20,height=20)

B1 = Button(window, text="确认",command=sett).pack()
Label(window, text = "注意输入格式示例：\n“2016 4 2 5 13”\n即为2016年4月2日5时20分13秒",fg = "gray").pack()
B2 = Button(window, text="初始化",command=reset).pack(side = RIGHT)

_thread.start_new_thread(showtime, (window, canvas))

def trickit():   
    if((rtime['second'])<59):
        rtime['second'] += 1
    elif(rtime['minute']<59):
        rtime['minute'] += 1
        rtime['second'] = 0
    elif(rtime['hour']<23):
        rtime['hour'] += 1
        rtime['minute'] = 0
        rtime['second'] = 0
    elif (rtime['day'] < 28):
        rtime['day'] += 1
        rtime['hour'] = 0
        rtime['minute'] = 0
        rtime['second'] = 0
    elif (rtime['month'] < 12):
        if(rtime['month']==1 or rtime['month']==3 or rtime['month']==5 or rtime['month']==7 or rtime['month']==8 or rtime['month']==10):
            if(rtime['day']<31):
                rtime['day']+=1
            else:
                rtime['month'] += 1
                rtime['day'] = 1
                rtime['hour'] = 0
                rtime['minute'] = 0
                rtime['second'] = 0
        if(rtime['month']==4 or rtime['month']==6 or rtime['month']==9 or rtime['month']==11):
            if (rtime['day'] < 30):
                rtime['day'] += 1
            else:
                rtime['month'] += 1
                rtime['day'] = 1
                rtime['hour'] = 0
                rtime['minute'] = 0
                rtime['second'] = 0
        else:  
            if(runnian(rtime['year'])):
                if(rtime['day']<29):
                    rtime['day']+=1
                else:
                    rtime['month'] += 1
                    rtime['day'] = 1
                    rtime['hour'] = 0
                    rtime['minute'] = 0
                    rtime['second'] = 0
    else:
        if(rtime['day']<31):
            rtime['day']+=1
        else:
            rtime['year']+=1
            rtime['month'] = 1
            rtime['day'] = 1
            rtime['hour'] = 0
            rtime['minute'] = 0
            rtime['second'] = 0

    t1 = str(rtime['year']).zfill(4) + "年" + str(rtime['month']).zfill(2) + "月" + str(rtime['day']).zfill(2) + "日"
    Label1.config(text=t1, font=('Arial', 15))
    t = str(rtime['hour']).zfill(2) + ":" + str(rtime['minute']).zfill(2) + ":" + str(rtime['second']).zfill(2)
    Label2.config(text=t, font=('Arial', 15))
    y1 = runnian(rtime['year']) + " " + tgdz(rtime['year']) + " " + shuxiang(rtime['year'])
    Label3.config(text=y1, font=('Arial', 15))
    window.update()
    Label2.after(1000, trickit)

Label2.after(0, trickit)

window.mainloop()
