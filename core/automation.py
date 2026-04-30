import os
from core.logger import logger
from core.utils import sanitize_filename
from config import PASTA_BASE

# CORE (função base)
def preencher_form(page, dados, url, botao, pasta, tipo):

    try:
        page.goto(url)

        page.fill('input[name="name"]', dados['nome'])
        page.fill('input[name="cpf"]', dados['cpf'])
        page.fill('input[name="role"]', dados['profissao'])
        page.fill('input[name="nationality"]', dados['nacionalidade'])
        page.fill('input[name="zipCode"]', dados['cep'])
        page.fill('input[name="address"]', dados['endereco'])
        
        page.click('button[role="combobox"]', timeout=15000)
        opcao_site = dados["estado_civil"].split("(")[0]
        logger.info(f"Estado civil selecionado: {opcao_site}")
        page.get_by_role("option", name=opcao_site, exact=True).click(timeout=15000)

        # Gerar termo
        page.get_by_role("button", name=botao).click()

        download_button = page.locator("button:has-text('Download')")

        download_button.wait_for(state="visible", timeout=15000)

        with page.expect_download(timeout=15000) as download_info:
            download_button.click(force=True, timeout=15000)
        
        download = download_info.value

        extensao = os.path.splitext(download.suggested_filename)[1]
        nome = sanitize_filename(dados['nome'])

        arquivo = f"{tipo}_{nome}{extensao}"

        path = os.path.join(pasta, arquivo)
        download.save_as(path)

        logger.info(f"Arquivo gerado: {arquivo}")

        return True

    except Exception as e:
        logger.error(f"Erro ao gerar {tipo}: {e}")
        return False

# WRAPPERS (abstração limpa)
def get_pasta(base, tipo):
    path = os.path.join(base, tipo)
    os.makedirs(path, exist_ok=True)
    return path

def gerar(page, dados, termo):
    return preencher_form(
        page,
        dados,
        termo["url"],
        termo["botao"],
        get_pasta(PASTA_BASE, termo["nome"]),
        termo["nome"]
    )