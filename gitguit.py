import tkinter as tk
import  os
from tkinter import *
from  tkinter import messagebox
root = Tk()
root.geometry("300x300")
add_FLAG=False
commit_FLAG=False

def git_add():
    cmd="git add ."
    os.system(cmd)
    add_FLAG=True
    messagebox.showinfo("Added")
    pass
add_btn = Button(root,text="git add .",command = git_add)
add_btn.pack()
l=Label(root,text="Commit message")
T=Text(root,height = 5, width = 52)
l.pack()
T.pack()

def git_commit():
    msg=T.get("1.0",'end-1c')
    if(len(msg)>5):
        git_add()
        
        cmd="git commit -m "+'"'+msg+'"'
        print(cmd)
        os.system(cmd)
        messagebox.showinfo("Commited")
        commit_FLAG=True
    else:
        messagebox.showerror("enter commit message")
        pass
commit_btn = Button(root,text="git commit",command = git_commit)
commit_btn.pack()
def git_push():
    if(commit_FLAG):
        cmd="git push"
        os.system(cmd)
        messagebox.showinfo("Pushed")
    pass
push_btn = Button(root,text="git push",command = git_push)
push_btn.pack()
def git_pull():
    cmd="git pull"
    os.system(cmd)
    pass
pull_btn = Button(root,text="git pull",command = git_pull)
pull_btn.pack()
tk.mainloop()
