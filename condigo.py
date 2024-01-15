# (logica de programaçao)
# Passo 1: Entrar no sistema da empresa 
 #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de produtos pra cadastrar
# Passo 4: Cadastrar um produto
 # Passo 5: Repetir o processo de cadastro até o fim


#OBS CLICAR -> pyautogui.click
#OBS ESCREVER -> pyautogui.writep.ashtagtreinamentos.com/python/intensivao/login
#OBS APERTA UMA TECLA -> pyautogui.press
#OBS hotkey -> (vc passa a tecla que vc quer aperta e ele aperta)
#OBS pyautogui.pause 10 ->(quando eu quise parar um pouco a operaçao)
#OBS link = -> (e uma abreviçao para qualque link, sem repitir)
#OBS time.sleep -> (e uma pausa em determinada etapa)
#OBS pyautogui.position -> (ele pega a posiçao de um elemento)
#OBS para mim ver a posiçao -> print(pyautogui.position())
#OBS o pandas serve para baixa o banco de dados 
#OBS scroll serve para (rola a pagina) -> pyautogui.scroll
#(numero positivo para cima e negativo para baixo)
#OBS quando eu quise pega informaçao de uma linha e uma coluna -> tabela.loc[linha, coluna]
#OBS como trasforma numero em texto coloca dentro de um -> str
#OBS quando tiver um condiçao e so adiciona o -> if
#OBS comando do pandas para dizer que esta vazil -> pandas.isna 





# Passo 1: Entrar no sistema da empresa 
   #https://dlp.hashtagtreinamentos.com/python/intensivao/login
   #pip intall pyautogui
import pyautogui
import time 
   #aperta a tecla do windows (command + barra de espaço)
pyautogui.press("win")
   #digita o nome do programa (chrome)
pyautogui.write("microsoft edge")
pyautogui.PAUSE = 3 
   #aperta entar
pyautogui.press("enter")
# Passo 1 (segunda fase)
   #digitar o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
   #aperta enter
pyautogui.press("enter")


# Passo 2: Fazer login
pyautogui.click(x=582, y=451)
# Passo 2 (segunda fase)
   #digitar o email
pyautogui.write("fakenere@gmail.com")
   #passa para o campo de senha 
pyautogui.press("tab")
   #digitar senha 
pyautogui.write("senhafake")
pyautogui.click(x=943, y=640)
time.sleep(5)


# Passo 3: Importar a base de produtos pra cadastrar
import pandas 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
     # Passo 4: Cadastrar um produto
     pyautogui.click(x=725, y=323)
     # codigo
     codigo = tabela.loc[linha, "codigo"]
     pyautogui.write(codigo)
     pyautogui.press("tab")
     #marca
     pyautogui.write(tabela.lac[linha, "marca"])
     pyautogui.press("tab")
     #tipo
     pyautogui.write(tabela.lac[linha, "tipo"])
     pyautogui.press("tab")
     #categoria
     pyautogui.write(str(tabela.lac[linha, "categoria"]))
     pyautogui.press("tab")
     #preço
     pyautogui.write(str(tabela.lac[linha, "preco_unitario"]))
     pyautogui.press("tab")
     #custo
     pyautogui.write(str(tabela.lac[linha, "custo"]))
     pyautogui.press("tab")
     #obs
     obs = tabela.lac[linha,"obs"]
     if not pandas.isna(obs):
        pyautogui.write(obs)
        pyautogui.press("tab")
        pyautogui.press("enter")

# Passo 5: Repetir o processo de cadastro até o fim
        pyautogui.scroll(3000)
 
   
     