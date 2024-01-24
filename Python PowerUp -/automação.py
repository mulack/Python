# passo a passo do projeto

    # pyautogui.write -> escrever um texto
    # pyautogui.press -> apertar 1 tecla
    # pyautogui.click -> clicar em algum lugar da tela
    # pyautogui.hotkey -> combinação de teclas
import time
import pyautogui
import pandas as pd

pyautogui.PAUSE = 0.3 

# passo 1: Entrar no sistema da empresa
    # Abrir o navegador (Google)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(4)
pyautogui.hotkey("win", "up")

    # Entrar no link
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2) #temporiza so o ultimo comando 

# passo 2: Fazer login 
    # selecionar campo email
pyautogui.click(x=427, y=392)
pyautogui.write("malvadão@gmail.com")

    # passar a senha 
pyautogui.press("tab") # passa para o proximo campo
pyautogui.write("senhakk")

    # logar
pyautogui.click(x=661, y=547) #ou pyautogui.press("enter")
time.sleep(2)

# passo 3: Importar a base de produtos para cadastro
dados = pd.read_csv("produtos.csv")

# passo 5: Repetir o processo até cadastrar tudo
    # passo 4: Cadastrar um produto
    # tabela.index linhas da tabela e tabela.columns da as colunas
for linha in dados.index:

        # clicar no campo de codigo
    pyautogui.click(x=433, y=279)

        # pegar da tabela o campo que eu quero preencher
    codigo = dados.loc[linha, "codigo"]
    marca = dados.loc[linha, "marca"]
    tipo = dados.loc[linha, "tipo"]
    categoria = dados.loc[linha, "categoria"]
    preco_unitario = dados.loc[linha, "preco_unitario"]
    custo = dados.loc[linha, "custo"] 

        # preencher o campo
    pyautogui.write(str(codigo)) # obriga que codigo seja um texto para preenchimento dos dados 
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    if not pd.isna(dados.loc[linha, "obs"]):
        pyautogui.write(str(dados.loc[linha, "obs"])) #outro jeito de fazer
        
        # Confirmar a adção do produto
    pyautogui.click(x=594, y=586)
        # dar scroll do tudo para cima
    pyautogui.scroll(100000)


