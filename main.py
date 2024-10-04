from tkinter import *
import tkinter.messagebox


window = Tk()
window.title('To-do app')

# widget to hold listbox and scrolbar
frame = Frame(window)
frame.pack()

# listbox holder widget
listbox = Listbox(frame, bg='black', fg='white',height=30,width=100,font = "Helvetica")  
listbox.pack(side=tkinter.LEFT)

# scrollbar if the list exceeds 
scrollbar = Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)


#sync the scrollbar and listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


def entertask():
    
   
    input_todos = ''
    def add():
        input_todos = task_entry.get(1.0, 'end-1c')
        if input_todos == "":
            tkinter.messagebox.showwarning(title='Warning', message='Enter some todos')
        else:
            listbox.insert(END, input_todos)
            root.destroy()
            
            
    root = Tk()
    root.title('Add Task')
    task_entry= Text(root, width=40, height=4)
    task_entry.pack()
    temp_button = Button(root, text='Add task', command=add)
    temp_button.pack()   
    root.mainloop()


def delete_task():
    select = listbox.curselection()
    listbox.delete(select[0])
    
    
def mark_completed():
    marked = listbox.curselection()
    temp = marked[0]
    
    temp_marked = listbox.get(marked)
    temp_marked=temp_marked+" ✔"
    
    listbox.delete(temp)
    listbox.insert(temp,temp_marked)
    
    
#buttons widget
entry = Button(window, text="Add task",width=50,command=entertask)
entry.pack(pady=4)

delete=Button(window,text="Delete selected task",width=50,command=delete_task)
delete.pack(pady=3)
mark=Button(window,text="Mark as completed ",width=50,command=mark_completed)
mark.pack(pady=3)





window.mainloop()