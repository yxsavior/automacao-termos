def validar_linha(linha):
    obrigatorios = [
        "Nome completo (Como na identidade)",
        "CPF",
        "Profissão atual"
    ]

    # 1. existência
    for campo in obrigatorios:
        if campo not in linha:
            return False

        valor = str(linha[campo]).strip()
        if not valor or valor.lower() == "nan":
            return False

    # 2. regras básicas de qualidade
    cpf = ''.join(filter(str.isdigit, str(linha["CPF"])))
    if len(cpf) != 11:
        return False

    if len(str(linha["Nome completo (Como na identidade)"]).strip()) < 3:
        return False

    return True

# def validar_linha(linha):
#     obrigatorios = [
#         "Nome completo (Como na identidade)",
#         "CPF",
#         "Profissão atual"
#     ]

#     for campo in obrigatorios:
#         valor = str(linha.get(campo, "")).strip()
#         if not valor or valor.lower() == "nan":
#             return False

#     return True