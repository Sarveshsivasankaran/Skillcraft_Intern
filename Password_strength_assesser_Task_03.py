import tkinter as tk

root=tk.Tk()
root.title("Password_strength_assesser")
root.geometry("400x200")
tk.Label(text="Enter your Password:",font=('calibre',12,'bold')).pack(pady=10)
string_input=tk.Entry(root,width=40).pack(pady=20)
root.mainloop()