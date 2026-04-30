import re
import pandas as pd

ESTADO_CIVIL_MAP = {
    "solteir@": "solteiro",
    "solteiro": "solteiro",
    "solteira": "solteiro",

    "casad@": "casado",
    "casado": "casado",
    "casada": "casado",

    "divorciad@": "divorciado",
    "divorciado": "divorciado",
    "divorciada": "divorciado",

    "separad@": "separado",
    "separado": "separado",
    "separada": "separado",

    "viúv@": "viúvo",
    "viúvo": "viúvo",
    "viúva": "viúvo"
}

# LIMPEZA BÁSICA
def limpar_texto(texto):
    if pd.isna(texto):
        return ""

    texto = str(texto).strip()
    texto = re.sub(r'[^\x00-\x7FÀ-ÿ]+', '', texto)
    return texto


def apenas_numeros(texto):
    if pd.isna(texto):
        return ""
    return re.sub(r'\D', '', str(texto))

# TRATAMENTOS ESPECÍFICOS
def tratar_nacionalidade(texto):
    if pd.isna(texto):
        return ""

    texto = str(texto).strip().lower()

    termos_brasil = [
        "brasil",
        "brasileiro",
        "brasileira",
        "brasileir@",
        "salvador bahia brasil"
    ]

    if texto in termos_brasil:
        return "Brasileiro"

    return texto.capitalize()


def tratar_estado_civil(texto):
    if pd.isna(texto):
        return ""

    texto = str(texto).strip()

    t = texto.lower()

    # padrões base de estado civil
    radicais = ["solteir", "casad", "divorciad", "separad", "viúv"]

    for r in radicais:
        if t.startswith(r):
            return r.capitalize() + "o"

    return texto

# PIPELINE PRINCIPAL
def preparar_dados(linha):
    rua = limpar_texto(linha.get("Rua"))
    numero_raw = linha.get("Número")
    bairro = limpar_texto(linha.get("Bairro"))
    cidade = limpar_texto(linha.get("Cidade"))
    estado = limpar_texto(linha.get("Estado"))

    # número seguro
    if pd.isna(numero_raw) or str(numero_raw).strip() == "":
        numero = "S/N"
    else:
        try:
            numero = str(int(float(numero_raw)))
        except:
            numero = str(numero_raw)

    endereco = f"{rua}, {numero} - {bairro}, {cidade} - {estado}"

    return {
        "nome": limpar_texto(linha.get("Nome completo (Como na identidade)")),
        "cpf": apenas_numeros(linha.get("CPF")),
        "profissao": limpar_texto(linha.get("Profissão atual")).capitalize(),
        "nacionalidade": tratar_nacionalidade(limpar_texto(linha.get("Nacionalidade"))),
        "cep": apenas_numeros(linha.get("CEP (apenas números)")),
        "estado_civil": tratar_estado_civil(limpar_texto(linha["Estado Civil"])),
        "endereco": endereco
    }