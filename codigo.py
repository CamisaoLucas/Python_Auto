# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da empresa
import pyautogui
import time
import pandas as pd
    # pyautogui.write -> escreve um texto
    # pyautogui.press -> apertar uma Tecla
    # pyautogui.click -> clicar em algum lugar da tela
    # pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# Abrir o navegador (Chrome)
pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')

# Entrar no Link do sistema (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# Passo 2: Fazer Login
pyautogui.click(x=826, y=357)
pyautogui.write('falso@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.click(x=956, y=530)
time.sleep(3)
# Passo 3: Importar a base de produtos a cadastrar
tabela = pd.read_csv('produto.csv')
print(tabela)
# Passo 4: Cadastrar um produto e Passo 5: Repetir o processo de cadastro até o fim da base
for linha in tabela.index:
    # pegar o valor do campo e depois preencher
    pyautogui.click(x=980, y=243)
    # preencher o campo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    # Verificando se obs está preenchido ou não
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
        
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Scrollar totalmente para cima
    pyautogui.scroll(5000)
