from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    pagina.goto("https://www.facebook.com/")
    print(pagina.title())

    pagina.get_by_role("textbox", name="Email ou número de celular").fill("vasconcelloseric23@gmail.com")
    pagina.get_by_role("textbox", name="Senha").fill("Ericv@concellos23")
    pagina.get_by_role("button", name="Entrar").click()



    time.sleep(10)
    navegador.close()

