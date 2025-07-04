import tkinter as tk
from tkinter import messagebox
users_db = {
    "admin":{"password":"admin","role":"admin"}
}
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
        
        if username in users_db:
            messagebox.showerror("error", "username sudah di pakai")

        elif username == "" or password == "" :
            messagebox.showwarning("warning", "kolom tidak boleh kosong")

        else:
            users_db[username] = {"password":password, "role":"user"}
            messagebox.showinfo("sukses", "berhasil membuat akun")
            self.show_login()
    
    def login(self):
        username = self.username_login.get()
        password = self.password_login.get()

        global current_user

        if username in users_db and users_db[username]["password"] == password:
            current_user = username
            current_role = users_db[username]["role"]
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