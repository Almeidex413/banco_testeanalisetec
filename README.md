# Dashboard de Análise de Vendas - Avaliação Técnica

## 📑 Visão Geral

[cite_start]Este projeto é uma solução completa para a avaliação técnica de Analista de Dados, desenvolvida para a empresa Agro-E. [cite: 3] O objetivo foi construir um dashboard interativo utilizando Python, Streamlit e PostgreSQL para analisar um conjunto de dados de vendas simulado e responder a diversas questões de negócio.

Am aplicação final permite a exploração dos dados através de filtros dinâmicos e apresenta análises detalhadas em abas separadas, cobrindo todos os requisitos solicitados na avaliação.

## Funcionalidades Principais

- **Dashboard Interativo:** Painel principal com KPIs (Receita, Pedidos, Itens Vendidos) que se atualizam em tempo real.
- **Filtros Avançados:** Filtre os dados por período, categoria de produto e cliente.
- **Análises Detalhadas:** Respostas para todas as questões da avaliação organizadas em abas, incluindo:
    - [cite_start]Análise RFM (Recência, Frequência, Valor). [cite: 60]
    - [cite_start]Identificação dos 5 produtos mais rentáveis. [cite: 72]
    - [cite_start]Análise de tendências de vendas e clientes inativos. [cite: 87, 93]
    - [cite_start]Detecção de anomalias e sugestões de otimização. [cite: 96, 101]
- [cite_start]**Visualização de Dados:** Gráficos exploratórios criados com Matplotlib. [cite: 113]
- [cite_start]**Testes Unitários:** Testes para garantir a qualidade da lógica de cálculo. [cite: 11]

## Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Banco de Dados:** PostgreSQL
- **Dashboard:** Streamlit
- **Análise de Dados:** Pandas
- **Visualização:** Matplotlib
- **Testes:** Pytest

## Como Executar

Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos
- Python (versão 3.8 ou superior)
- PostgreSQL instalado e em execução.

### Passos

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/Almeidex413/banco_testeanalisetec
    cd banco_testeanalisetec
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados PostgreSQL:**
    - Usando uma ferramenta como o pgAdmin4, crie um novo banco de dados (ex: `banco_americanas`).
    - Conecte-se a este novo banco.
    - Execute o script `schema.sql` para criar todas as tabelas.
    - Em seguida, execute o script `data.sql` para popular as tabelas com os dados de exemplo.

5.  **Verifique a Conexão:**
    - As credenciais de conexão com o banco de dados estão no arquivo `app.py` (função `run_query`). Se você usou um nome de banco, usuário ou senha diferente, ajuste-os lá.

6.  **Execute a Aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```
    O dashboard será aberto no seu navegador.