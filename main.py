#  instalar o playwright
#  pip install playwright
# playwright install

# Abrir um navegador, acessar uma página e imprimir o título da página

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False, slow_mo=500)
    contexto = navegador.new_context()
    # abrir o navegador
    pagina = contexto.new_page()
    # navegar para a uma página
    pagina.goto("https://www.hashtagtreinamentos.com/")
    print(pagina.title())

    #  1° forma de selecionar um elemento e clicar
    # pagina.locator('xpath=//a[text()="Cursos"]').click()

    # Selecionar um elemento e clicar
    # 2° forma de selecionar um elemento e clicar
    botao = pagina.get_by_role("link", name="Quero aprender")
    with contexto.expect_page() as pagina2_info:
        botao.click()

    pagina2 = pagina2_info.value
    pagina2.goto("https://www.hashtagtreinamentos.com/curso-python")
  
    # seleconar vários elementos
    # divisorias = pagina.locator("div")

    # nova página em branco
    # pagina2 = contexto.new_page()

    # nova página -> criar contexto e depois:
    pagina2 = pagina2_info.value
    # pagina2.goto("https://www.hashtagtreinamentos.com/curso-python")

    # preencher formulário
    pagina2.get_by_role("textbox", name="Seu primeiro nome").fill("Eric vasconcellos")
    pagina2.get_by_role("textbox", name="Seu melhor e-mail").fill("eric.vasconcellos@example.com")
    pagina2.get_by_role("textbox", name="Seu WhatsApp com DDD").fill("11999999999")
    pagina2.get_by_role("button", name="Quero acessar as informações").click()

    # esperar um elemento aparecer
    novo_botao = pagina2.get_by_role("link", name="quero garantir uma vaga")
    expect(novo_botao).to_be_visible()
    novo_botao.click()

    pagina.click("text=Cursos")
    navegador.close()