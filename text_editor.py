from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class TextEditor:
    def __init__(self):
        self.root = Tk()
        self.root.title('Text Editor')
        self.root.iconbitmap('images\\text_editor_icon.ico')
        menu = Menu(self.root)
        self.root.config(menu=menu)
        file_menu = Menu(menu, tearoff=False)
        menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New', command=self.create_new_file)
        file_menu.add_command(label='New Window', command=self.open_new_window)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.destroy)
        edit_menu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Edit', menu=edit_menu)
        self.text_area = Text(self.root, font=('Helvetica', 12), undo=True)
        self.text_area.grid(row=0, column=0)
        edit_menu.add_command(label='Undo', command=self.text_area.edit_undo, accelerator='(Ctrl+z)')
        edit_menu.add_command(label='Redo', command=self.text_area.edit_redo, accelerator='(Ctrl+y)')
        edit_menu.add_separator()
        edit_menu.add_command(label='Cut', command=self.cut)
        edit_menu.add_command(label='Copy', command=self.copy)
        edit_menu.add_command(label='Paste', command=self.paste)
        self.root.mainloop()

    def create_new_file(self):
        save = messagebox.askyesno(title='Notepad', message='Would you like to save your changes?')
        if save == True:
            self.save_file()
        self.text_area.delete(1.0, END)

    def open_new_window(self):
        save = messagebox.askyesno(title='Notepad', message='Would you like to save your changes?')
        if save == True:
            self.save_file()
        self.text_area.delete(1.0, END)
        win2 = TextEditor()

    def open_file(self):
        f = filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
        content = f.read()
        save = messagebox.askyesno(title='Notepad', message='Would you like to save your changes?')
        if save == True:
            self.save_file()
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, content)

    def save_file(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='*.txt')
        text = self.text_area.get(1.0, END)
        f.write(text)
        f.close()

    def cut(self):
        if self.text_area.selection_get():
            self.selected = self.text_area.selection_get()
            self.text_area.delete('sel.first', 'sel.last')

    def copy(self):
        if self.text_area.selection_get():
            self.selected = self.text_area.selection_get()

    def paste(self):
        if self.selected:
            pos = self.text_area.index(INSERT)
            self.text_area.insert(pos, self.selected)


win = TextEditor()