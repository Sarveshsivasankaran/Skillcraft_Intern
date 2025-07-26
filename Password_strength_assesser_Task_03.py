import tkinter as tk

common_passwords = [
    "123456", "123456789", "qwerty", "password", "1234567",
    "12345678", "12345", "iloveyou", "111111", "123123",
    "abc123", "qwerty123", "1q2w3e4r", "admin", "letmein",
    "welcome", "monkey", "login", "princess", "dragon",
    "password1", "1234", "sunshine", "000000", "passw0rd",
    "lovely", "football", "batman", "zaq1zaq1", "superman",
    "trustno1", "hello", "whatever", "freedom", "1qaz2wsx",
    "654321", "qazwsx", "master", "mustang", "shadow",
    "michael", "696969", "batman", "baseball", "access",
    "starwars", "flower", "hottie", "donald", "qwertyuiop",
    "charlie", "maggie", "pepper", "secret", "ashley",
    "cheese", "jordan", "jennifer", "hunter", "tigger",
    "ginger", "pokemon", "joshua", "pepper123", "summer",
    "cookie", "test", "love", "biteme", "whatever123",
    "trustme", "matrix", "internet", "letmein123", "merlin",
    "987654321", "zaq12wsx", "1q2w3e", "mypass", "newyork",
    "justin", "killer", "ferrari", "666666", "xxxxxx",
    "donaldtrump", "boomer", "ninja", "computer", "hello123",
    "qwerty1", "iloveyou1", "godzilla", "william", "7777777",
    "password!", "qwerty!@#", "pass123", "abc123456", "welcome1",
    "mypass123", "passw0rd123", "1password", "root", "sql123",
    "love123", "123qwe", "user123", "admin123", "letmein!"
]

root=tk.Tk()
root.title("Password_strength_assesser")
root.geometry("400x200")
tk.Label(root,text="Enter your Password:",font=('calibre',12,'bold')).pack(pady=10)
string_input=tk.Entry(root,width=40,show="*")
string_input.pack(pady=20)
result_label = tk.Label(root, text="", font=('futura', 16, 'bold'))
result_label.pack(pady=20)

def Strength_checker(password):
    checks = [
        lambda p: len(p) >= 8,
        lambda p: any(c.islower() for c in p),
        lambda p: any(c.isupper() for c in p),
        lambda p: any(c.isdigit() for c in p),
        lambda p: any(c in "!@#$%^&*()_+-=[]{}" for c in p),
        lambda p: ' ' not in p,
        lambda p: p not in common_passwords,
        lambda p: len(p) >= 12
    ]
    points = 0
    for check in checks:
        if check(password):
            points += 1
    return points

def main():
    pwd=string_input.get()
    score=Strength_checker(pwd)
    if score<=2:
        result_label.config(text="Very Weak Password!", fg="red")
    elif score<=4:
        result_label.config(text="Weak Password!", fg="orange")
    elif score<=6:
        result_label.config(text="Moderate Password!", fg="yellow")
    elif score==7:
        result_label.config(text="Strong Password!", fg="green")
    elif score==8:
        result_label.config(text="Very Strong Password!", fg="darkgreen")

tk.Button(root,text="Check password strength",command=main).pack()
root.mainloop()