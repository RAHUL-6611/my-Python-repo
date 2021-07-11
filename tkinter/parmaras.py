from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
ide = Tk()
ide.title("Parmaras")
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def run():
    try:
        if file_path == '':
            warning = Toplevel(highlightcolor='red', width=500, height=500)
            text = Label(warning, text="please save your code first", padx=25, pady=25)
            text.pack()
            return
        # code = editor.get('1.0', END)
        # exec(code)
        # print(code)
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()     # variable storing the process serial wise
        code_output.insert('1.0', output)
        code_output.insert('1.0', error)
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)
    except Exception as d:
        print(d)


def New_project():
    pass


def open_file():
    try:
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            editor.delete(('1.0', END))
            editor.insert('1.0', code)
            set_file_path(path)
    except Exception as d:
        print(d)


def Save_As():
    try:
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)
    except Exception as d:
        print(d)


def Scratch_file():
    try:
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            editor.delete(('1.0', END))
            editor.insert('1.0', code)
            set_file_path(path)
    except Exception as d:
        print(d)


def Rename_project():
    pass


def Settings():
    pass


mainmenu = Menu(ide)

file_menu = Menu(mainmenu, tearoff=0)
file_menu.add_cascade(label='New Project', command=New_project)
file_menu.add_cascade(label='Open New', command=open_file)
file_menu.add_cascade(label='New Scratch file', command=open_file)
file_menu.add_cascade(label='Save', command=Save_As)
file_menu.add_cascade(label='Save As', command=Save_As)
file_menu.add_cascade(label='Rename Project', command=Rename_project)
file_menu.add_cascade(label='Settings', command=Settings)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
# file_menu.add_cascade(label='', command=)
file_menu.add_cascade(label='Exit', command=exit)

mainmenu.add_cascade(label='file', menu=file_menu)

runbar = Menu(mainmenu, tearoff=0)
runbar.add_command(label="Run", command=run)

mainmenu.add_cascade(label="Run", menu=runbar)
ide.config(menu=mainmenu)

editor = Text(bg='lightgrey')
editor.pack()

code_output = Text(height=10)
code_output.pack()
ide.mainloop()
