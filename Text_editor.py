import os
from  tkinter import *
from tkinter import filedialog,colorchooser,font,messagebox
def change_color():
    color=colorchooser.askcolor()
    text_area.config(fg=color[1])
def change_font(*args):
    text_area.config(font=(font_name.get(),font_size.get()))
def new():
    window.title('untitled')
    text_area.delete(0.0,'end')
def open_file():
    file_path=filedialog.askopenfilename(defaultextension=".txt",
                                         filetypes=[("Text Document","*.txt"),
                                                    ("All files","*.*")])
    file=os.path.basename(file_path)
    try:
        text_area.delete(1.0,'end')
        with open (file_path) as file:
         text_area.insert(1.0,file.read())
    except Exception:
        print("file are unable to read")
def save():
    file_path=filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("All files","*.*"),
                                                      ("Html files","*.html"),
                                                      ("Text file","*.txt")])
    if file_path is None:
            return
    try:
        with open(file_path,'w') as file:
            file.write(text_area.get(1.0,'end'))
    except Exception:
        print("Unable to save file")
def cut():
    text_area.event_generate('<<Cut>>')
def copy():
     text_area.event_generate('<<Copy>>')
def paste():
     text_area.event_generate('<<Paste>>')
def about():
    messagebox.showinfo(title="about",message="This is your code")
def bold():
    current_font=font.Font(font=text_area['font'])
    if current_font.actual()['weight']=='bold':
        text_area.config(font=(font_name.get(),font_size.get(),'normal'))
    else:
        text_area.config(font=(font_name.get(),font_size.get(),'bold'))
def italic():
    current_font=font.Font(font=text_area['font'])
    if current_font.actual()['weight']=='italic':
        text_area.config(font=(font_name.get(),font_size.get(),'normal'))
    else:
        text_area.config(font=(font_name.get(),font_size.get(),'italic'))
def underline():
    current_font=font.Font(font=text_area['font'])
    if current_font.actual()['weight']=='underline':
        text_area.config(font=(font_name.get(),font_size.get(),'normal'))
    else:
        text_area.config(font=(font_name.get(),font_size.get(),'underline'))
window=Tk()
menubar=Menu(window)
window.config(menu=menubar)
window.title("Text Editor")
window.grid_rowconfigure(0,weight=1)
window.grid_rowconfigure(1,weight=0)
window.grid_columnconfigure(0,weight=1)
window_width=window_height=500
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
fileMenu=Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='New',command=new)
fileMenu.add_command(label='Open',command=open_file)
fileMenu.add_command(label='Save',command=save)
fileMenu.add_separator()
fileMenu.add_command(label='quit',command=quit)
editMenu=Menu(menubar,font=("MV Boli",10))
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Cut',command=cut)
editMenu.add_command(label='Copy',command=copy)
editMenu.add_command(label='Paste',command=paste)
helpMenu=Menu(menubar,font=("MV Boli",10))
menubar.add_cascade(label='Help',menu=helpMenu)
helpMenu.add_command(label='About',command=about)
font_name=StringVar(window)
font_name.set("arial")
font_size=StringVar(window)
font_size.set(25)
text_area=Text(window,font=(font_name.get(),font_size.get()))
scrollbar=Scrollbar(text_area)
text_area.grid(sticky=N+E+S+W)
scrollbar.pack(side='right',fill='y')
text_area.config(yscrollcommand=scrollbar.set)
frame=Frame(window)
frame.grid()
color_Btn=Button(frame,text='color',command=change_color)
color_Btn.grid(row=0,column=0)
change_font=OptionMenu(frame,font_name, *font.families(),command=change_font)
change_font.grid(row=0,column=1)
size_box=Spinbox(frame,textvariable=font_size,from_=1, to=100)
size_box.grid(row=0,column=2)
bold_btn=Button(frame,text='bold',command=bold)
bold_btn.grid(row=0,column=3)
italic_btn=Button(frame,text='italic',command=italic)
italic_btn.grid(row=0,column=4)
underline_btn=Button(frame,text='underline',command=underline)
underline_btn.grid(row=0,column=5)
window.mainloop()
