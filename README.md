# 🤖 Automação de Geração de Termos

Automação de geração de documentos utilizando Python, Pandas e Playwright. O projeto realiza a ingestão de dados a partir de arquivos CSV, executa validações e transformações para padronização dos registros e utiliza essas informações para preencher formulários automaticamente em uma plataforma web, gerar documentos e organizar os arquivos resultantes.

## 🎯 Objetivo

Automatizar um processo operacional de geração de termos, reduzindo atividades manuais e garantindo maior consistência dos dados utilizados no preenchimento dos documentos.

---

## 🚀 Funcionalidades

* Login automático na plataforma
* Leitura de dados a partir de arquivo CSV
* Validação de registros antes do processamento
* Padronização e tratamento de dados
* Preenchimento automatizado de formulários via Playwright
* Geração de múltiplos tipos de termos
* Download automático dos arquivos gerados
* Organização dos documentos por categoria
* Registro detalhado de execução através de logs
* Execução parcial ou completa via linha de comando

---

## 📊 Tratamento e Qualidade de Dados

Além da automação web, o projeto implementa uma etapa de preparação dos dados antes do envio para a plataforma.

### Validações

* Verificação de campos obrigatórios
* Validação básica de CPF (11 dígitos)
* Verificação de tamanho mínimo para nomes

### Transformações

* Leitura automática de CSV com diferentes separadores
* Remoção de caracteres inválidos
* Padronização de CPF e CEP
* Normalização de nacionalidade
* Normalização de estado civil
* Tratamento de valores ausentes
* Construção automática de endereços completos a partir de múltiplas colunas

### Fluxo de Dados

```text
CSV
 ↓
Validação
 ↓
Transformação e Padronização
 ↓
Automação Web (Playwright)
 ↓
Geração dos Termos
 ↓
Download dos Arquivos
```

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Playwright
* Logging
* Regex (tratamento de texto)
* Manipulação de arquivos CSV
* Variáveis de ambiente (.env)

---

## 📁 Estrutura do Projeto

```text
data/        → arquivos CSV de entrada
core/        → regras de negócio, validações e automação
TERMOS/      → arquivos gerados organizados por categoria
logs/        → logs de execução
config.py    → configurações gerais do sistema
main.py      → ponto de entrada da aplicação
```

---

## 📦 Instalação

### Pré-requisitos

- Python 3.10 ou superior

### Dependências:

```bash
pip install -r requirements.txt
```

### Navegadores do Playwright:

```bash
playwright install
```

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
BASE_URL=https://seusite.com.br

USUARIO_LOGIN=seu_usuario
SENHA_LOGIN=sua_senha
```

---

## 📄 Estrutura Esperada do CSV

O arquivo CSV deve conter as seguintes colunas:

```text
Nome completo (Como na identidade)
CPF
Profissão atual
Estado Civil
Nacionalidade
CEP (apenas números)
Rua
Número
Bairro
Cidade
Estado
```

---

## 🔄 Fluxo da Automação

1. Realiza login na plataforma
2. Carrega os dados do CSV
3. Valida os registros
4. Executa transformações e padronizações
5. Preenche os formulários automaticamente
6. Gera os termos selecionados
7. Realiza o download dos arquivos
8. Organiza os documentos por categoria
9. Registra todas as etapas em log

---

## 📑 Tipos de Termos

* Confidencialidade
* Imagem
* Voluntariado

---

## ▶️ Como Executar

### Modo Interativo

```bash
python main.py
```

Opções disponíveis:

```text
1 - Confidencialidade
2 - Imagem
3 - Voluntariado
4 - Todos
```

### Modo CLI

```bash
python main.py confidencialidade
python main.py imagem
python main.py voluntariado
python main.py todos
```

---

## 📂 Saída dos Arquivos

Os documentos gerados são organizados automaticamente:

```text
TERMOS/
 ├── confidencialidade/
 ├── imagem/
 └── voluntariado/
```

Os arquivos baixados são armazenados utilizando nomes padronizados e seguros para o sistema operacional.

---

## 📝 Logs

Toda execução gera registros de auditoria em:

```text
logs/app.log
```

Exemplos de eventos registrados:

* Login realizado
* Arquivos gerados
* Falhas de validação
* Erros de automação
* Tentativas de reprocessamento

---

## 🔮 Possíveis Melhorias

* Implementar validação completa de CPF utilizando os dígitos verificadores.
* Exportar registros inválidos para auditoria e reprocessamento.
* Evoluir a etapa de ingestão e transformação para uma camada ETL independente da automação.
* Adicionar suporte à leitura de arquivos Excel (.xlsx) além de CSV.
* Converter automaticamente os arquivos `.tex` gerados para PDF.
