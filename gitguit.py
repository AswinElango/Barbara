import tkinter as tk
import  os,sys
from tkinter import *
from  tkinter import messagebox
root = Tk()
root.geometry("300x300")
def execute_cmd(cmd):
    y=sys.stdout
    x=os.popen(cmd).read()
    msg= Message(text=x)
    msg.pack()
    # return x

# execute_cmd("echo hello")
def git_add():
    cmd="git add ."
    execute_cmd(cmd)
    add_FLAG=True
    messagebox.showinfo("Added")
    pass
add_btn = Button(root,text="git add .",command = git_add)
add_btn.pack()
l=Label(root,text="Commit message")
T=Text(root,height = 5, width = 52)
l.pack()
T.pack()

def git_commit(*push_call):
    msg=T.get("1.0",'end-1c')
    if(len(msg)>5):
        execute_cmd("git add .")
        cmd="git commit -m "+'"'+msg+'"'
        print(cmd)
        execute_cmd(cmd)
        if(not(push_call)):
            messagebox.showinfo("Commited")
    else:
        messagebox.showerror("enter commit message")
        pass
commit_btn = Button(root,text="git commit",command = git_commit)
commit_btn.pack()
def git_push():
    git_commit(True)
    cmd="git push"
    execute_cmd(cmd)
    messagebox.showinfo("Pushed")
   
push_btn = Button(root,text="git push",command = git_push)
push_btn.pack()
def git_pull():
    cmd="git pull"
    execute_cmd(cmd)
    pass
pull_btn = Button(root,text="git pull",command = git_pull)
pull_btn.pack()
tk.mainloop()
