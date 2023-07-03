# to-do-list
### This application starts with a splash screen: It will keep running for 3 seconds and then the main interface will appear.
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/f3b8701c-bd40-469f-bef0-68645c46d7da)

### The main interface looks empty for the first time, just like this:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/e4ecbc53-f903-4b53-9284-f542edf4c0e2)

### The main interface looks like this when it contains tasks:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/74ed692d-a0d9-42b6-a7f3-f2b512e31e36)

### The focus will be on the Entry Bar which makes the adding operation easier:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/a94b8abd-e9db-4d9f-acb9-774b0df85132)

### After adding a task, the user can use scrollbars to move (up/down) if the list contains more than 6 tasks, and (right/left) if the task is long like task number 2:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/f98bfc32-214c-40cb-a31f-ba33f2e88c74)

### When the user completes a task, he can cross it by selecting the task and pressing the ‘Cross-Off Task’ button:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/0a6b3e30-83b7-4761-a8bd-df73a13fab91)

### If the user wants to uncross a task, he can do this by selecting the task and pressing the ‘Uncross Task’ button: here task 6 is crossed, which is obvious because the select-background is different from uncrossed tasks.
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/f38775ec-84a7-463a-9d06-c6d3311eaa22)

#### After pressing ‘Uncross Task’ task 6 will be uncrossed:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/9464d6a5-2d53-4f6e-9d61-72ce3961d45c)

### The user can also delete all the crossed tasks by pressing the ‘Delete Crossed’ button: here tasks 4 and 7 are crossed
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/3f882cf1-beb9-42a3-8bf2-eb929290b428)

#### After pressing the ‘Delete-Crossed’ button tasks 4 and 7 will be deleted:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/4549e633-72f7-4c7a-8653-0a79ab8788d1)

### The user can also delete a task even if it is not crossed by selecting the task and pressing the ‘Delete Task’ button: here task 3 is selected:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/7282c160-a66c-48e7-b224-c42292e0f2a3)

#### Task 3 will be deleted after pressing the ‘Delete Task’ button:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/a650cb82-5c51-41e0-a850-609d3267c0f2)

## In the file menu there is three choices: 
### The first choice is ‘Save List’, which allows the user to save his tasks in a .dat file.
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/fa4aca56-0566-448a-bbb5-e1bd4d495745)

### The second choice is ‘Open List’, which allows the user to upload any .dat file he has in the disk memory to the To-Do List application:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/0d8ea35e-18ef-4d7d-a99d-09e90e619626)

### The third choice is ‘Clear List ’, which allows the user to delete all the tasks whether they are crossed or not, which empties the list:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/ec0d2c8c-98ec-4415-b91c-9a6b847a9779)
And the list will become empty as the first time.

## This application is interactive and will not allow the user to do mistakes, such as:
#### If the user tried to enter an empty task, he will get a message error:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/2dfd2963-6761-4694-810d-34cebb878e13)

#### If the user tried to Delete/Cross/Uncross without selecting a task he will get message errors:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/bffc3fe8-9811-438b-a2f2-28583fa40e77)

![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/666fbab8-c6a6-4c64-a321-c4b40a9c0a4c)

![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/151d91d9-21c9-4020-99d6-af87147bb5ee)

#### If the user tried to delete from an empty list this error message will be shown:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/0eb1a570-8cc9-431b-a7e0-2bfcef960b31)

#### If the user wants to exit the app a confirming message will be shown that all crossed items will be deleted:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/599a8efe-bace-4ea6-af5f-8e6240068ad4)

## If the user presses ‘No’ the application will keep running, but if he presses ‘Yes’, the crossed tasks will be deleted, the application will be closed, and a close screen will be shown to the user.
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/f4275361-59d8-4c21-8a60-68f9db6976c6)

## The user will be able to open and close the application without losing his tasks because I used SQLite3 as a database to save the data locally. I have a todo.db file that contains a table called tasks which contains one attribute named title type ‘text ’:
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/d941584b-dec5-4cc3-8eef-a930f12c23a5)

### I used some operations to interact with the database, such as
>1.	for row in cur.execute('select title from tasks'):
>2.	cur.execute('insert into tasks values (?)', (my_entry.get(),))
>3.	cur.execute('delete from tasks where title = ?', (val,))
>4.	cur.execute('delete from tasks')
>5.	conn.commit()

### In the application, I added tones to the buttons to make the application more attractive, these tones are separated in the Sounds.py file that I have imported into our main ToDoList.py file and created an object of the Sound class to use these tones.
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/26240308-e571-4f7f-8fee-2c1de30ce0e9)
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/c30da888-f583-4706-9c91-3e9f3c9a2ba6)

### I also attached some keyboard buttons (enter/delete) to function in place of (Add Task/Delete Task) respectively using these lines:
>root.bind('<Return>', lambda event=None: add_button.invoke())
>root.bind('<Delete>', lambda event=None: delete_button.invoke())

### I was able to show the icon in the taskbar using these two lines:
>putIcon = u'CompanyName.ProductName'
>ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(putIcon)
![image](https://github.com/Lady-aouto/to-do-list/assets/95139153/39272fd2-8206-4fbe-9bc0-33bb5b2f3956)

### Also, I was able to change the color of the buttons when you hover over them by creating two methods:
>def on_enter(e):
>    e.widget['background'] = '#ff4d94'
>    e.widget['foreground'] = 'white'
>
>
>def on_leave(e):
>    e.widget['background'] = '#ffb3d1'
>    e.widget['foreground'] = '#400080'

### And binding the buttons with these methods using the following lines for each button:
>delete_button.bind("<Enter>", on_enter)
>delete_button.bind("<Leave>", on_leave)

##### Click [here](https://drive.google.com/file/d/1xbbJxgh5VV-q5iLqqPz0wgwv6L55FqU7/view) to watch a video demo of our application.
