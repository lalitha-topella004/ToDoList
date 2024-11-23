from tkinter import *
import tkinter.messagebox

def entertask():
    # A new window to pop up to take input
    input_text = ""

    def add():
        nonlocal input_text
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            # close the root1 window
            root1.destroy()

    root1 = Tk()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()

# function to facilitate the delete task from the Listbox
def deletetask():
    # selects the selected item and then deletes it
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

# Executes this to mark completed
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    # store the text of selected item in a string
    temp_marked = listbox_task.get(marked)
    # update it
    temp_marked = temp_marked + " ✔"
    # delete it then insert it
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)

window = Tk()
window.title("To-do List - Make Your Daily Routine")

# frame to display the content
frame_task = Frame(window)
frame_task.pack()
# listbox to store items
listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font="helvetica")
listbox_task.pack(side=tkinter.LEFT)
# scroll bar for more items
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)
# button to enter task
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)
# button to delete task
delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed ", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
