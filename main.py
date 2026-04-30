import os
from config import USUARIO, SENHA, DATA_PATH, PASTA_BASE, CONFIG
from data.loader import carregar_csv
from core.scraper import Scraper
from core.validators import validar_linha
from core.automation import gerar
from core.transformers import preparar_dados
from core.logger import logger
import sys

def menu_interativo():
    print("\n=== SELEÇÃO DE TERMOS ===")
    print("1 - Confidencialidade")
    print("2 - Imagem")
    print("3 - Voluntariado")
    print("4 - Todos")

    escolha = input("\nEscolha: ").strip()

    mapa = {
        "1": "confidencialidade",
        "2": "imagem",
        "3": "voluntariado",
        "4": "todos"
    }

    if escolha not in mapa:
        print("Opção inválida, usando TODOS")
    
    return mapa.get(escolha, "todos")

def obter_modo_execucao():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return menu_interativo()

def main():

    df = carregar_csv(DATA_PATH)
    if df is None:
        return
    
    modo = obter_modo_execucao()
    logger.info(f"Modo selecionado: {modo}")

    os.makedirs(PASTA_BASE, exist_ok=True)

    scraper = Scraper()
    scraper.login(USUARIO, SENHA)

    total = 0
    sucesso = 0
    erros = 0

    for i, linha in df.iterrows():
        total += 1

        try:
            if not validar_linha(linha):
                logger.warning(f"Linha {i} inválida")
                erros += 1
                continue

            dados = preparar_dados(linha)

            modo = modo.strip().lower()

            for termo in CONFIG["termos"]:
                if modo != "todos" and termo["nome"] != modo:
                    continue

                ok = gerar(scraper.page, dados, termo)

                if ok:
                    sucesso += 1
                else:
                    erros += 1
            
        except Exception as e:
            logger.error(f"Erro na linha {i}: {e}")
            erros += 1
            continue

    scraper.close()

    logger.info(f"FINALIZADO | total = {total} sucesso = {sucesso} erros = {erros}")

if __name__ == "__main__":
    main()