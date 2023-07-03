from tkinter import *
from tkinter.font import Font
from tkinter import filedialog, messagebox
import pickle
import Sounds
import sqlite3
import ctypes

conn = sqlite3.connect('todo.db')
cur = conn.cursor()
cur.execute('create table if not exists tasks (title text)')
s = Sounds.Sound()

putIcon = u'CompanyName.ProductName'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(putIcon)

splash_root = Tk()
splash_root.iconbitmap(default="D:/PyCharm_D/PycharmProjectsD/micon.ico")
splash_root.title("To Do List!")
splash_root.geometry("500x400")

# Set Label
bg = PhotoImage(file="D:/PyCharm_D/PycharmProjectsD/splash.png")
splash_label = Label(splash_root, image=bg)
splash_label.pack()


# main window function
def splash():
    # destroy splash window
    splash_root.destroy()


# Set Interval
splash_root.after(3000, splash)

# Execute tkinter
mainloop()


root = Tk()
root.title('To Do List!')
root.iconbitmap(default="D:/PyCharm_D/PycharmProjectsD/micon.ico")
root.geometry("500x400")
root.resizable(False, False)

# we will use task list to keep track of the tasks in the listbox
task = []

bg2 = PhotoImage(file="D:/PyCharm_D/PycharmProjectsD/mbg.png")
bg3 = PhotoImage(file="D:/PyCharm_D/PycharmProjectsD/buttonbackground.png")

# Show image using label
label1 = Label(root, image=bg2)
label1.place(x=0, y=0)

# Define our Font
my_font = Font(
    family="Courier New Italic",
    size=18
)

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=22,
                  height=6,
                  bd=1,
                  bg="#ffe6f3",
                  fg="#464646",
                  # no line around it
                  highlightthickness=0,
                  selectbackground="#ff80b3",
                  # no line under the text
                  activestyle="none"
                  )
# create scrollbars
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_scrollbar2 = Scrollbar(my_frame, orient='horizontal')
my_scrollbar2.pack(side=BOTTOM, fill=X)

# Add scrollbars to Form
my_list.config(yscrollcommand=my_scrollbar.set, xscrollcommand=my_scrollbar2.set)
my_list.pack(side=TOP, fill=BOTH)
my_scrollbar.config(command=my_list.yview)
my_scrollbar2.config(command=my_list.xview)

# create entry box to add items to the list

my_entry = Entry(root, font=("Courier New", 20), width=22, bg="#ffe6f3")
my_entry.pack(pady=10)
my_entry.focus()

# create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)
label2 = Label(button_frame, image=bg3)
label2.place(x=0, y=0)


# ------------------------------------------FUNCTIONS---------------------------------------------------------
# ---------- DB functions ----------


def retrieve_db():
    print('Retrieved from the Database: ')
    while len(task) != 0:
        task.pop()
    for row in cur.execute('select title from tasks'):
        task.append(row[0])


def list_update():
    clear_list()
    for i in task:
        my_list.insert('end', i)
    print(task)


def clear_list():
    my_list.delete(0, END)
# ---------- end of DB functions ----------

# ---------- main functions ----------


def delete_item():
    try:
        # val is used in the database
        val = my_list.get(my_list.curselection())
        if val in task:
            task.remove(val)
            cur.execute('delete from tasks where title = ?', (val,))
        # This will delete the selected item
        my_list.delete(ANCHOR)
        s.play_del()
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected!')
        count = 0
        while count < my_list.size():
            count += 1
        if count == 0:
            messagebox.showinfo('Cannot Delete', 'No Task Items to Delete\nEnter a Task First!')


def add_item():
    if len(my_entry.get()) == 0:
        messagebox.showinfo('Cannot Add', 'Enter a Task in The Entry Bar!')
    else:
        s.play_add()
        my_list.insert(END, my_entry.get())
        task.append(my_entry.get())
        cur.execute('insert into tasks values (?)', (my_entry.get(),))
        my_entry.delete(0, END)


def cross_item():
    try:
        my_list.itemconfig(
            # Cross off item
            my_list.curselection(),
            fg="#dedede",
            selectbackground='#cccccc'
        )
        s.play_cro()
        # get rid of selection bar
        my_list.select_clear(0, END)
    except:
        messagebox.showinfo('Cannot Cross', 'No Task Item Selected')


def uncross_item():
    try:
        my_list.itemconfig(
            # Uncross off item
            my_list.curselection(),
            fg="#464646",
            selectbackground="#ff80b3"
        )
        # get rid of selection bar
        my_list.select_clear(0, END)
        s.play_unc()
    except:
        messagebox.showinfo('Cannot Uncross', 'No Task Item Selected, \nFirst, Enter a Task '
                                              'Then cross a Task to Uncross!')


def delete_crossed():
    count = 0
    crossed = 0
    while count < my_list.size():
        # cget defines the information of the item
        if my_list.itemcget(count, "fg") == "#dedede":
            crossed += 1
            print(my_list.get(my_list.index(count)))
            print(my_list.index(count))
            del task[my_list.index(count)]
            cur.execute('delete from tasks where title = ?', (my_list.get(count),))
            my_list.delete(my_list.index(count))
            s.play_del()
        else:
            count += 1
    if crossed == 0:
        messagebox.showinfo('Cannot Delete', 'No Task Item Crossed,\nFinish & Cross Some Tasks!')
    list_update()
# ---------- end of main functions ----------

# ---------- menu functions ----------


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C://Users",
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        # we need it to ensure we have selected a file name
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        # delete crossed off items before saving
        delete_crossed()
        # grab all the stuff from the list
        stuff = my_list.get(0, END)

        # Open the file
        output_file = open(file_name, 'wb')

        # Actually add the stuff to the file
        pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C://Users",
        title="Open File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        # Delete currently open list
        my_list.delete(0, END)

        # Open the file
        input_file = open(file_name, 'rb')

        # Load the data from the file
        stuff = pickle.load(input_file)

        # output stuff to the screen
        for item in stuff:
            my_list.insert(END, item)
            task.append(item)
            cur.execute('insert into tasks values (?)', (item,))


def delete_all():
    mb = messagebox.askyesno('Delete All?', 'Are you sure?')
    if mb:
        while len(task) != 0:
            task.pop()
        cur.execute('delete from tasks')
        list_update()
# ---------- end of menu functions ----------


def bye():
    close_root = Tk()
    close_root.iconbitmap(default="D:/PyCharm_D/PycharmProjectsD/micon.ico")
    close_root.title("To Do List!")
    close_root.geometry("500x400")
    # Set Label
    bg4 = PhotoImage(file="D:/PyCharm_D/PycharmProjectsD/CloseScreen.png")
    close_label = Label(close_root, image=bg4)
    close_label.pack()

    # main window function
    def close():
        # destroy splash window
        close_root.destroy()
    # Set Interval
    close_root.after(3000, close)
    # Execute tkinter
    mainloop()


def display_msg():
    dw = messagebox.askyesno(title='Exit?', message='All the crossed tasks will be deleted. '
                                                    ' Are you sure you want to exit?')
    if dw:
        if len(task) != 0:
            delete_crossed()
        root.destroy()
        bye()


root.protocol('WM_DELETE_WINDOW', display_msg)
# design functions


def on_enter(e):
    e.widget['background'] = '#ff4d94'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#ffb3d1'
    e.widget['foreground'] = '#400080'

# ------------------------------------------END OF FUNCTIONS---------------------------------------------------------

# Create Menu


my_menu = Menu(root)
root.config(menu=my_menu)
# Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
# Add dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_all)

# Add some buttons
delete_button = Button(button_frame, text="Delete Task", command=delete_item, bg="#ffb3d1", fg='#400080')
add_button = Button(button_frame, text="Add Task", command=add_item, cursor='plus', bg="#ffb3d1", fg='#400080')
cross_button = Button(button_frame, text="Cross-Off Task", command=cross_item, bg="#ffb3d1", fg='#400080')
uncross_button = Button(button_frame, text="Uncross  Task", command=uncross_item, bg="#ffb3d1", fg='#400080')
delete_crossed_button = Button(button_frame, text="Delete-Crossed", command=delete_crossed, bg="#ffb3d1", fg='#400080')

root.bind('<Return>', lambda event=None: add_button.invoke())
root.bind('<Delete>', lambda event=None: delete_button.invoke())
delete_button.bind("<Enter>", on_enter)
delete_button.bind("<Leave>", on_leave)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)
cross_button.bind("<Enter>", on_enter)
cross_button.bind("<Leave>", on_leave)
uncross_button.bind("<Enter>", on_enter)
uncross_button.bind("<Leave>", on_leave)
delete_crossed_button.bind("<Enter>", on_enter)
delete_crossed_button.bind("<Leave>", on_leave)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

retrieve_db()
list_update()

root.mainloop()

conn.commit()
cur.close()
