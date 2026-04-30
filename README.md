# 🤖 Automação de Geração de Termos

Este projeto automatiza o preenchimento e download de termos via Playwright.

---

## 🚀 O que o sistema faz

* Faz login na plataforma automaticamente
* Lê dados de um arquivo CSV
* Preenche formulários automaticamente
* Gera 3 tipos de termos:

  * Confidencialidade
  * Imagem
  * Voluntariado
* Faz download automático dos arquivos em PDF
* Organiza os arquivos em pastas separadas
* Permite execução parcial (escolha de termos via CLI ou menu)

---

## 📁 Estrutura do projeto

```txt
data/        → arquivo CSV com os dados dos trainees
core/        → lógica principal da automação (Playwright + regras)
TERMOS/      → arquivos gerados (downloads organizados por tipo)
logs/        → arquivos de log da execução
config.py    → configurações gerais (URLs, caminhos, credenciais)
main.py      → ponto de execução do sistema
```

---

## 📦 Pré-requisitos

* Python 3.10+
* Playwright instalado

### Instalação

```bash
pip install -r requirements.txt
playwright install
```

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto com:

```env
# URL base do sistema (obrigatório)
BASE_URL="https://seusite.com.br"

# Credenciais de login (exemplo)
USUARIO_LOGIN=seu_usuario
SENHA_LOGIN=sua_senha
```

---

## 📊 Estrutura do CSV

O arquivo `data/dados.csv` deve conter as seguintes colunas:

* Nome completo
* CPF
* Profissão
* Estado Civil
* Nacionalidade
* CEP
* Rua
* Número
* Bairro
* Cidade
* Estado

---

## 🔄 Fluxo da automação

1. Login na plataforma
2. Leitura do CSV
3. Para cada linha:

   * valida os dados
   * preenche formulário
   * gera os termos selecionados
   * realiza download automático
4. Organiza arquivos por tipo em pastas separadas

---

## ▶️ Como executar

### 🟢 Modo interativo (menu)

```bash
python main.py
```

O sistema exibirá:

```
1 - Confidencialidade
2 - Imagem
3 - Voluntariado
4 - Todos
```

---

### 🟡 Modo via terminal (CLI)

```bash
python main.py confidencialidade
python main.py imagem
python main.py voluntariado
python main.py todos
```

---

## 📂 Saída dos arquivos

Os arquivos são salvos automaticamente em:

```txt
TERMOS/
 ├── confidencialidade/
 ├── imagem/
 └── voluntariado/
```