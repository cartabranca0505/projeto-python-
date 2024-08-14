import tkinter as tk
from tkinter import messagebox
import os
from principal import abrir_tela_principal  # Importa a função para abrir a tela principal

# Função para verificar login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if os.path.exists('usuarios.txt'):
        with open('usuarios.txt', 'r') as f:
            for linha in f:
                user, pwd = linha.strip().split(',')
                if user == usuario and pwd == senha:
                    messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                    tela_login.destroy()
                    abrir_tela_principal()  # Chama a função para abrir a tela principal
                    return
    messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para cadastro
def cadastrar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if usuario and senha:
        with open('usuarios.txt', 'a') as f:
            f.write(f"{usuario},{senha}\n")
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

# Tela de Login/Cadastro
tela_login = tk.Tk()
tela_login.title("Login")
tela_login.geometry("300x200")

tk.Label(tela_login, text="Usuário").pack(pady=5)
entrada_usuario = tk.Entry(tela_login)
entrada_usuario.pack(pady=5)

tk.Label(tela_login, text="Senha").pack(pady=5)
entrada_senha = tk.Entry(tela_login, show='*')
entrada_senha.pack(pady=5)

tk.Button(tela_login, text="Login", command=verificar_login).pack(pady=5)
tk.Button(tela_login, text="Cadastrar", command=cadastrar).pack(pady=5)

tela_login.mainloop()
