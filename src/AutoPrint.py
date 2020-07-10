#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author kitxiao

import os
from pykeyboard import *
import time
import tkinter.filedialog
import tkinter.messagebox
#import threading
#from tkinter import *
import win32gui
import win32con
#import ctypes
import locale



print ("#########This is a python script for printing pictures!")
print ("#########Attention:Print only picture files with the suffix .tif")
print ("#########Start.....")
print('#########Please choose the folder path where the pictures are located:')

#filename=tkinter.filedialog.askopenfilename(title=u"选择文件")
#print (filename)
root = tkinter.Tk()
root.withdraw() #隐藏
path =  tkinter.filedialog.askdirectory() #选择文件夹
print('#########Do nothing while the program is running automatically!')
tkinter.messagebox.showwarning('Attention', 'Do nothing while the program is running automatically!')

       
k = PyKeyboard()
        
def count_num(file_dir):   
    total = 0
    for root, dirs, files in os.walk(file_dir):  
        for s in files:
            if s.endswith('.tif'):
                total += 1
                
    return(total)        
       
def file_name(file_dir,total):   
    a = 0
    attr = []
    for root, dirs, files in os.walk(file_dir):  
        for s in files:
            if s.endswith('.tif'):
                attr.append(s)
                time.sleep(0.7)
                os.startfile(root+"/"+s)
                time.sleep(0.7)
                a += 1
                k.press_key(k.alt_l_key)
                k.tap_key('P')  # 点击p键
                k.release_key(k.alt_l_key)
                time.sleep(0.7)
                k.tap_key('P')  # 点击p键
                time.sleep(0.7)
                k.press_key(k.alt_l_key)
                k.tap_key('F')  # 点击f键
                k.release_key(k.alt_l_key)
                time.sleep(0.7)
                k.press_key(k.alt_l_key)
                k.tap_key('P')  # 点击p键
                k.release_key(k.alt_l_key)
                progress(100*a/total)
                #if a != total:
                    #print (" Printing.....")
    print (" Finished.....")
    return attr

def finish(arrays):      
    
    #dll_handle = ctypes.windll.kernel32
    #sys_lang = hex(dll_handle.GetSystemDefaultUILanguage())
    loc_lang = locale.getdefaultlocale()[0]
    #print(loc_lang)
    
    for s in arrays:
        wndtitle = None
        time.sleep(1)
        if loc_lang == 'zh_CN':
            wndtitle = s+" - Windows 照片查看器"   # 进程名
        elif loc_lang == 'en_US':
            wndtitle = s+" - Windows Photo Viewer"   # 进程名
        wndclass = None
        wnd = win32gui.FindWindow(wndclass, wndtitle)    # 获取窗口句柄
        #print(wnd)
        #win32gui.CloseWindow(wnd)      # 窗口最小化
        #time.sleep(300)
        #wndz = win32gui.FindWindowEx(hwndParent=wnd, hwndChildAfter=0, lpszClass=None, lpszWindow=None);
        win32gui.SendMessage(wnd, win32con.WM_CLOSE)   # 关闭窗口
        #k.press_key(k.alt_l_key)
        #k.tap_key(k.function_keys[4])  # 点击功能键F4
        #k.release_key(k.alt_l_key)
# 
# 
# 
#  
# def update_progress_bar():
#     for percent in range(1, 101):
#         hour = int(percent/3600)
#         minute = int(percent/60) - hour*60
#         second = percent % 60
#         green_length = int(sum_length * percent / 100)
#         canvas_progress_bar.coords(canvas_shape, (0, 0, green_length, 25))
#         canvas_progress_bar.itemconfig(canvas_text, text='%02d:%02d:%02d' % (hour, minute, second))
#         var_progress_bar_percent.set('%0.2f  %%' % percent)
#         time.sleep(1)
#  
#  
# def run():
#     th = threading.Thread(target=update_progress_bar)
#     th.setDaemon(True)
#     th.start()
#  
#  
# top = Tk()
# top.title('Progress Bar')
# top.geometry('800x200+290+100')
# top.resizable(False, False)
# top.config(bg='white')
#  
# # 进度条
# sum_length = 630
# canvas_progress_bar = Canvas(top, width=sum_length, height=20)
# canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
# canvas_text = canvas_progress_bar.create_text(292, 4, anchor=NW)
# canvas_progress_bar.itemconfig(canvas_text, text='00:00:00')
# var_progress_bar_percent = StringVar()
# var_progress_bar_percent.set('00.00  %')
# label_progress_bar_percent = Label(top, textvariable=var_progress_bar_percent, fg='black', bg='white')
# canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=CENTER)
# label_progress_bar_percent.place(relx=0.89, rely=0.4, anchor=CENTER)
# # 按钮
# button_start = Button(top, text='开始', fg='#F5F5F5', bg='#7A7A7A', command=run, height=1, width=15, relief=GROOVE, bd=2, activebackground='#F5F5F5', activeforeground='#535353')
# button_start.place(relx=0.45, rely=0.7, anchor=CENTER)
#  
# top.mainloop()


def progress(percent,width=50):
    '''
                完成总任务的百分比
    '''
    if percent >= 100:
        percent=100
  
    show_str=('[%%-%ds]' %width) %(int(width * percent/100)*">") #字符串拼接的嵌套使用
    print('\r%s %d%%' %(show_str,percent),end='')
    
total = count_num(path)
array = file_name(path,total)
#print(array)
time.sleep(5)
tkinter.messagebox.showinfo('message', 'Please confirm the printing is completed?')
root.destroy()  #销毁
finish(array)

print ("#########End.....")