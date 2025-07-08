import tkinter as tk
import mysql.connector
from tkinter import messagebox
database = mysql.connector.connect(host = "localhost",user = "root",password = "", database = "marketplace")
db= database
cursor = db.cursor()
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall() :
    print(row)

current_user = None

class loginPage:
    def __init__(self, root):
        self.root=root
        self.root.title("login app")
        self.root.geometry("300x400")
        self.show_login()

    def show_login(self):
        self.clear_window()
        tk.Label(self.root, text="login",font=("Helfetica",16)).pack(pady=20)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text= "Username").grid(row=0,column=0, padx=5, pady=5, sticky="e")
        self.username_login = tk.Entry(form_frame)
        self.username_login.grid(row=0, column=1, padx=5, pady=5)
       
        tk.Label(form_frame, text="Password").grid(row=1, column=0, padx=5, pady=5, sticky= "e")
        self.password_login = tk.Entry(form_frame)
        self.password_login.grid(row=1, column=1, padx=5, pady=5)
        

        tk.Button(self.root,text="login",command=self.login).pack(pady=10)
        tk.Button(self.root,text="register",command=self.show_register).pack()

    def show_register(self):
        self.clear_window()
        tk.Label(self.root,text="login",font=("Helfetica",16))
        
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Username").grid(row= 0, column= 0, padx=5, pady=5, sticky="e") 
        self.username_reg = tk.Entry(form_frame)
        self.username_reg.grid(row=0, column=1, padx=5,pady=5)
        
        tk.Label(form_frame, text="Password").grid(row=1, column=0,padx=5, pady=5, sticky="e")
        self.password_reg = tk.Entry(form_frame)
        self.password_reg.grid(row=1, column=1, padx=5, pady=5)
        

        tk.Button(self.root, text="register", command= self.register).pack(pady=10)
        tk.Button(self.root, text="back to login", command= self.show_login).pack()

    def show_profil(self):
        self.clear_window()
        tk.Label(self.root, text=f"profil pengguna", font=("Helfetica",16)).pack(pady=20)
        tk.Label(self.root, text= f"Usernam : {current_user}").pack(pady=10)
        tk.Button(self.root, text="kembali ke dasboard", command= self.show_dasboard_user).pack(pady=20)

    def show_dasboard_user(self):
        self.clear_window()
        tk.Label(self.root, text= f"selamat datang, {current_user}", font=("Helfetica",16)).pack(pady=20)
        tk.Button(self.root, text= "log out", command= self.logout).pack(pady=20)
        tk.Button(self.root, text="Profil", command= self.show_profil).pack(pady=10) 
        
    def show_dasboard_admin(self):
        self.clear_window()
        tk.Label(self.root, text= f"admin dasboard, {current_user}", font=("Helfetica",16)).pack(pady=20)
        tk.Button(self.root, text= "log out", command= self.logout).pack(pady=20)
        

    def register(self):
        username = self.username_reg.get()
        password =self.password_reg.get()
        db= database
        cursor = db.cursor()
        cursor.execute("SELECT username FROM users WHERE username = %s",(username,))
        result = cursor.fetchone()

        print(username)
        print(password)
    
        if result:
            messagebox.showerror("error", "username sudah di pakai")

        elif username == "" or password == "" :
            messagebox.showwarning("warning", "kolom tidak boleh kosong")

        else:
            cursor.execute("INSERT INTO users (username,password,role) VALUES (%s,%s,'user')",(username,password,))
            db.commit()
            messagebox.showinfo("sukses", "berhasil membuat akun")
            self.show_login()
    
    def login(self):
        username = self.username_login.get()
        password = self.password_login.get()

        global current_user
        db= database
        cursor = db.cursor()
        cursor.execute("SELECT username, role FROM users WHERE username = %s AND password = %s", (username,password))
        result = cursor.fetchone()

        if result : 
            current_user = result[0]
            current_role = result[1]
            if current_role == "admin":
                self.show_dasboard_admin()
            else:
                self.show_dasboard_user()
           
        
        else:
            messagebox.showerror("error", "username atau password salah")

    def logout(self):
        global current_user
        current_user = None
        self.show_login()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        

        

if __name__ == "__main__" :
    root = tk.Tk()
    app = loginPage(root)
    root.mainloop()