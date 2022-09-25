from this import s
import webbrowser
import typer
import pyautogui
import webbrowser
import time

app = typer.Typer()

@app.command()
def doc(space: str, project: str, page: str = 'doc'):
    #abrir o confluence
    
    print('SEB to SEBRAE')
    print('CONSULTING to Consultin Service')

    webbrowser.open('https://neoway.atlassian.net/wiki/spaces/' + f'{space.upper()}')

    time.sleep(3)

    ##clicar nova pagina de doc
    
    #crtl + f para procurar a pasta de documentações
    pyautogui.hotkey('ctrl', 'f', durantion=1)
    pyautogui.typewrite(page)
    time.sleep(0.5)

    #ir na pasta de projetos
    pyautogui.click(115,679, duration=1)
    
    #fechar pesquisa (iniciada com crtl + f)
    pyautogui.click(1072,122, duration=1)

    #cria nova página de documentacao
    pyautogui.click(391,679, duration=1)
    time.sleep(3)

    #clica no titulo e insere o nome do projeto informado
    pyautogui.click(180,301, duration=1)
    pyautogui.typewrite(str(project))
    time.sleep(1)

    #clica e insere campos padrões
    pyautogui.click(174,368, duration=1)
    pyautogui.write('# Contexto Simplificado')
    pyautogui.press('enter')
    pyautogui.write("texto aqui")
    pyautogui.press('enter')
    pyautogui.press('enter')

    pyautogui.write('# Premissas')
    pyautogui.press('enter')
    pyautogui.write("texto aqui")
    pyautogui.press('enter')
    pyautogui.press('enter')

    pyautogui.write('# Testes Realizados')
    pyautogui.press('enter')
    pyautogui.write("texto e imagens aqui")
    pyautogui.press('enter')
    pyautogui.press('enter')


    # -- Exclusao de página após teste --
    time.sleep(3)
    pyautogui.click(1358,149, duration=1)
    time.sleep(1)
    pyautogui.click(1309,157, duration=1)
    time.sleep(1)
    pyautogui.click(1208,511, duration=1)
    time.sleep(1)
    pyautogui.click(864,322, duration=1)



if __name__ == "__main__":
    app()
