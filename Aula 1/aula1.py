"""
INSIGHTS:
1. Ao invés de buscar a posição do mouse na tela,
    fazer com que o mouse clique em um determindado elemento,
    independente da sua posição.
2. Trabalhar mais com a tecla tab.
3. Executar Código em Python Automaticamente (Diariamente, Semanalmente)
    https://www.youtube.com/watch?v=SxEjHAlCqmo
4. Como Transformar Arquivo Python em Executável - [Arquivo Executável]
    https://www.youtube.com/watch?v=cGSerUmK0CE
"""


""" 
1. Faça o passo a passo de como resolveria o problema
2. Traduza para código

----------------------------------------------------------------

Passo 1 - Entrar no sistema da empresa
    Site: https://dlp.hashtagtreinamentos.com/python/intensivao/login
    Biblioteca: pyautogui
        Recomendada para RPA (Robotic Process Automation)
        Link da documentação: https://pyautogui.readthedocs.io/en/latest/
        Prompt: pip install pyautogui
    Comando mais usados:
        clicar -> pyautogui.click()
            pyautogui.click(x=649, y=570, button="right", clicks=2)
        escrever -> pyautogui.write("text")
        pressionar tecla -> pyautogui.press("enter")
        atalhos -> pyautogui.hotkey("ctrl", "c")
        scroll -> pyautogui.scroll(1000)
            Número positivo: scroll para cima
            Número negativo: scroll para baixo
            O número dependo do quanto você precisa rolar a página.

        Obs.: Use `write` para escrever frase, por exemplo, um email/senha.
            Use `press` para pressionar teclas, como enter, win (tecla windows), delete
    Caso queira parar a automação, por exemplo, o código entrou em um loop:
        Leve o mouse para o canto superior esquedo da tela e aguarde alguns segundos.

Passo 2 - Fazer login
    Criar um arquivo auxiliar para pegar a posição do mouse.

Passo 3 - Importar a base de dados
    Bibliotecas: pandas, numpy, openpyxl
            Recomendada para trabalahr com base de dados
            Link da documentação - pandas: https://pandas.pydata.org/docs/user_guide/index.html#user-guide
            Link da documentação - numpy: https://numpy.org/doc/
            Prompt: pip install pandas numpy openpyxl

Passo 4 - Cadastrar um produto

Passo 5 - Repetir até acabar a base de dados
"""

## PASSO 1

import pyautogui # Importar a biblioteca de automação
import time # Para fazer pausas em pontos específicos do código

# Pausa entre os comandos. Ajuda a observar o código quando está construindo.
pyautogui.PAUSE = 1

# Pressionar tecla do windows
pyautogui.press("win")

# Digita o nome do programa
pyautogui.write("edge")

### Obs.: Se o texto tiver aspas(', ") coloque um contrabarra(\) antes das aspas. pyautogui.write("edge\"")

# Pressionar o enter
pyautogui.press("enter")

# Digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# Pressionar o enter
pyautogui.press("enter")

# Espera 5 segundos
time.sleep(5)


## PASSO 2

# Clicar no campo de email
pyautogui.click(x=1168, y=384)

# Escrever o email
email = "meuemail@gmail.com"
pyautogui.write(email)

# Passar par o campo de senha pressionando a tecla tab
pyautogui.press("tab")

# Digitar a senha
senha = "minha_senha123"
pyautogui.write(senha)

# Clicar no botão logar
pyautogui.click(x=1260, y=552)

# Espera 3 segundos
time.sleep(3)


## PASSO 3

# Importar biblioteca pandas
import pandas

# Caminho do arquivo CSV
path = "E:/Usuários/Isadora Picoli/Documents/Desenvolvimento Pessoal/Jornada Python/JornadaPython/Aula 1/produtos.csv"

# Ler o CSV
tabela = pandas.read_csv(path)

# Mostrar as 5 primeiras linhas do CSV
print(tabela.head())

# Para cada linha (tabela.index). Para cada coluna (tabela.columns).
for linha in tabela.index:
    ## PASSO 4

    # Clica no primeiro input text
    pyautogui.click(x=1070, y=275)

    # Inserir código
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    # Inserir marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Inserir tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Inserir categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Inserir preço unitário
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Inserir custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Inserir observação
    obs = tabela.loc[linha, "obs"]

    # Se o valor não for um NaN, então escreve a observação.
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Enviar o produto
    pyautogui.press("enter")
    pyautogui.scroll(5000) # Ou pyautogui.press("pageup"). Ou pyautogui.press("pgup").