from tkinter import *  
import time  
import math  
import _thread
import os

def judge(m):
    p = "今年是"
    if (m % 4 == 0 and m % 400 != 0):
        p += "闰年"
    else:
        p += "平年"
    return p

def ganzhi(m):
    p = ""
    n1 = m % 10
    n2 = m % 12
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

def animal(m):
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

def drawclock(canvas):  
    x = 200  
    y = 200  
    width = 150 + 10  
    for i in range(1,13):  
        arc = 2.0 * math.pi / 12 * i  
        new_x = x + width * math.sin(arc)  
        new_y = y - width * math.cos(arc)  
        canvas.create_text(new_x,new_y,text = str(i))
    for i in range(1,61):
        if(i % 5 != 0):
            arc = 2.0 * math.pi / 60 * i
            new_x = x + width * math.sin(arc)
            new_y = y - width * math.cos(arc)
            canvas.create_text(new_x,new_y,text = "·")

def drawpointer(canvas,hour,minute,second):  
    x = 200  
    y = 200  
    hour_width = 70  
    minute_width = 90  
    second_width = 120  
    hour_arc = 2.0 * math.pi * hour / 12  
    minute_arc = 2.0 * math.pi * minute / 60  
    second_arc = 2.0 * math.pi * second / 60  
    canvas.create_line(x,y,x+hour_width * math.sin(hour_arc),y-hour_width*math.cos(hour_arc),width= 6.0,fill='yellow')
    canvas.create_line(x,y,x+minute_width*math.sin(minute_arc),y - minute_width*math.cos(minute_arc),width= 4.0,fill='green')
    canvas.create_line(x,y,x+second_width*math.sin(second_arc),y - second_width*math.cos(second_arc))
    canvas.create_oval(190, 190, 210, 210, fill='red')
    
def showtime(window,canvas):
    while 1:  
        mytime = ''
        mydate = ''
        localtime = time.localtime()
        year = localtime[0]
        month = localtime[1]
        day = localtime[2]
        hour = localtime[3]  
        minute = localtime[4]  
        second = localtime[5]  
        mydate = "日期：  " + str(year) + "年" + str(month) + "月" + str(day) + "日"
        mytime = "时间：  " + str(hour) + " : " + str(minute) + " : " + str(second)
        
        
        canvas.create_rectangle(0,0,400,600,fill='white')
        canvas.create_oval(30,30,370,370,fill='lightpink')
        canvas.create_oval(50,50,350,350,fill='lightblue')
        photo = PhotoImage(file='PEGGY.gif')
        canvas.create_image(200,200,image=photo)
        canvas.create_text(200,390,text=mydate,fill='black')
        canvas.create_text(200,410,text=mytime,fill='black')
        canvas.create_text(200,440,text=judge(year),fill='black')
        canvas.create_text(200,460,text=ganzhi(year),fill='black')
        canvas.create_text(200,480,text=animal(year),fill='black')
        drawpointer(canvas,hour,minute,second)
        drawclock(canvas)
        window.update()  
        time.sleep(1)
    
def main():  
    window = Tk()  
    window.geometry("800x800") 
    window.wm_title('社会人时钟')
    canvas = Canvas(window,width=400,height=600)
    canvas.pack()
    _thread.start_new_thread(showtime,(window,canvas))  
    window.mainloop()  
  
if __name__ == "__main__":  
        main()
