#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 22, 2018 03:03:08 PM EDT  platform: Linux
import sys
import os

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None

class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("863x750+723+112")
        top.title("Simple Editor")

        filesystem = FileSystem()

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.007, relwidth=1.002)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=865)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.035, rely=0.119, relheight=0.864, relwidth=0.932)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=806)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.035, rely=0.04, height=26, width=93)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=filesystem.new_folder)
        self.Button1.configure(text='''New Folder''')

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.185, rely=0.04, height=26, width=76)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(command=filesystem.new_file)
        self.Button2.configure(text='''New File''')

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.312, rely=0.04, height=26, width=86)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(command=filesystem.copy_text)
        self.Button3.configure(text='''Copy Text''')

class FileSystem:
    def __init__(self):
        self.type = None

    def new_file(self):
        self.type = "file"    
        self.new_window(self.create_dir, "New File")

    def new_folder(self):
        self.type = "folder"
        self.new_window(self.create_dir, "New Folder")

    def create_dir(self):
        content = self.Text1.get("1.0", "end-1c")
        os.system("~/Documents/learning/tk/scripts/./filesystem.sh {} {}".format(self.type, content))

        self.window.destroy()

    def copy_text(self):
        print("Copy TExt")

    def new_window(self, fn, title="New window"):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry("200x100")

        self.Frame1 = Frame(self.window)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.007, relwidth=1.002)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=200)

        # Text Input
        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.035, rely=0.119, relheight=0.564, relwidth=0.932)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=200)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.27, rely=.7, height=26, width=93)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=fn)
        self.Button1.configure(text=title)

if __name__ == '__main__':
    vp_start_gui()