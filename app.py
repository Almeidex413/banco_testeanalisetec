import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import locale

# --- config incial ---
try:
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8') # pt_BR MONETÁRIO
except locale.Error:
    st.error("Locale 'pt_BR.UTF-8' não encontrado. A formatação de moeda pode não funcionar. No Windows, tente 'ptb'.")
    try:
        locale.setlocale(locale.LC_MONETARY, 'ptb')
    except locale.Error:
        locale.setlocale(locale.LC_MONETARY, '')


# --- conecxão e consult ---
def run_query(query):
    """
    consulta no banco PostgreSQL e retorna.
    """
    try:
        with psycopg2.connect(
            dbname="banco_americanas",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        ) as conn:
            df = pd.read_sql_query(query, conn)
            return df
    except psycopg2.OperationalError as e:
        st.error(f"Erro de Conexão: Verifique se o banco de dados está rodando e as credenciais estão corretas. Detalhes: {e}")
        return None
    except Exception as e:
        st.error(f"Erro ao executar a consulta SQL: {e}")
        return None

# --- config pag e sidebar ---
st.set_page_config(layout="wide")
st.title("Análise de Vendas")
st.write("Projeto para a Avaliação Técnica de Analista de Dados.")

st.sidebar.header("Opções de filtros Interativos")

query_para_filtros = """
    SELECT
        pd.data_pedido, c.nome AS nome_do_cliente, pr.categoria
    FROM itens_pedido AS ip
    INNER JOIN produtos AS pr ON ip.id_produto = pr.id_produto
    INNER JOIN pedidos AS pd ON ip.id_pedido = pd.id_pedido
    INNER JOIN clientes AS c ON pd.id_cliente = c.id_cliente
"""
df_para_filtros = run_query(query_para_filtros)

min_data_default = pd.to_datetime("2023-01-01").date()
max_data_default = pd.to_datetime("today").date()
categorias_selecionadas = []
clientes_selecionados = []

if df_para_filtros is not None and not df_para_filtros.empty:
    df_para_filtros['data_pedido'] = pd.to_datetime(df_para_filtros['data_pedido'])
    min_data = df_para_filtros['data_pedido'].min().date()
    max_data = df_para_filtros['data_pedido'].max().date()

    data_inicio = st.sidebar.date_input("Data de Início", min_data, min_value=min_data, max_value=max_data)
    data_fim = st.sidebar.date_input("Data de Fim", max_data, min_value=min_data, max_value=max_data)

    categorias_unicas = sorted(df_para_filtros['categoria'].unique())
    categorias_selecionadas = st.sidebar.multiselect("Selecione a(s) Categoria(s)", options=categorias_unicas, default=categorias_unicas)

    clientes_unicos = sorted(df_para_filtros['nome_do_cliente'].unique())
    clientes_selecionados = st.sidebar.multiselect("Selecione o(s) Cliente(s)", options=clientes_unicos, default=clientes_unicos)
else:
    data_inicio = st.sidebar.date_input("Data de Início", min_data_default)
    data_fim = st.sidebar.date_input("Data de Fim", max_data_default)
    st.sidebar.warning("Não foi possível carregar opções de filtros de categoria e cliente.")


# --- dash principal ---
st.header("Controle Geral de Vendas Interativo")

query_dashboard = """
    SELECT
        pd.data_pedido, pd.id_pedido, c.nome AS nome_do_cliente,
        pr.nome AS nome_do_produto, pr.categoria, ip.quantidade,
        ip.preco_unitario, (ip.quantidade * ip.preco_unitario) AS valor_total_item
    FROM itens_pedido AS ip
    INNER JOIN produtos AS pr ON ip.id_produto = pr.id_produto
    INNER JOIN pedidos AS pd ON ip.id_pedido = pd.id_pedido
    INNER JOIN clientes AS c ON pd.id_cliente = c.id_cliente
"""
df_dashboard = run_query(query_dashboard)

if df_dashboard is not None and not df_dashboard.empty:
    df_dashboard['data_pedido'] = pd.to_datetime(df_dashboard['data_pedido'])
    
    # filtrs cascata
    df_filtrado = df_dashboard[
        (df_dashboard['data_pedido'].dt.date >= data_inicio) &
        (df_dashboard['data_pedido'].dt.date <= data_fim)
    ]
    if categorias_selecionadas:
        df_filtrado = df_filtrado[df_filtrado['categoria'].isin(categorias_selecionadas)]
    if clientes_selecionados:
        df_filtrado = df_filtrado[df_filtrado['nome_do_cliente'].isin(clientes_selecionados)]

    st.write(f"Análise para o período de **{data_inicio.strftime('%d/%m/%Y')}** a **{data_fim.strftime('%d/%m/%Y')}**.")
    col1, col2, col3 = st.columns(3)
    total_receita = df_filtrado['valor_total_item'].sum()
    total_pedidos = df_filtrado['id_pedido'].nunique()
    total_produtos_vendidos = df_filtrado['quantidade'].sum()
    col1.metric("Receita Total", locale.currency(total_receita, grouping=True))
    col2.metric("Total de Pedidos", f"{total_pedidos}")
    col3.metric("Total de Itens Vendidos", f"{total_produtos_vendidos}")
    
    st.write("Detalhes dos Pedidos no Período Selecionado:")
    df_display_filtrado = df_filtrado.copy()
    df_display_filtrado['valor_total_item'] = df_display_filtrado['valor_total_item'].apply(lambda x: locale.currency(x, grouping=True))
    df_display_filtrado['preco_unitario'] = df_display_filtrado['preco_unitario'].apply(lambda x: locale.currency(x, grouping=True))
    df_display_filtrado['data_pedido'] = df_display_filtrado['data_pedido'].dt.strftime('%d/%m/%Y')
    st.dataframe(df_display_filtrado, use_container_width=True, height=350, hide_index=True)
else:
    st.error("Não foi possível carregar os dados para o dashboard. Verifique se há dados no banco.")


# --- prox questões ---
st.header("Análises Detalhadas (Questões da Avaliação)")

aba2, aba3, aba4, aba5, aba6, aba7, aba8, aba10 = st.tabs([
    "Questão 2: Análise RFM", "Questão 3: Modelo de Dados", "Questão 4: Top Produtos", "Questão 5: Tendências", 
    "Questão 6: Clientes Inativos", "Questão 7: Anomalias", "Questão 8: Otimização", "Questão 10: Análise Exploratória"
])

with aba2:
    st.subheader("Questão 2: Análise RFM (Recência, Frequência e Valor)")
    query_rfm_100_porcento = """
        WITH PedidosNumerados AS (
            SELECT c.id_cliente, c.nome AS nome_cliente, p.data_pedido, p.valor_total,
                   LAG(p.data_pedido, 1) OVER (PARTITION BY c.id_cliente ORDER BY p.data_pedido) AS data_pedido_anterior,
                   ROW_NUMBER() OVER (PARTITION BY c.id_cliente ORDER BY p.data_pedido DESC) as ordem_pedido,
                   COUNT(p.id_pedido) OVER (PARTITION BY c.id_cliente) as total_pedidos
            FROM clientes c JOIN pedidos p ON c.id_cliente = p.id_cliente
        )
        SELECT pn.id_cliente, pn.nome_cliente,
               (CURRENT_DATE - MAX(CASE WHEN pn.ordem_pedido = 1 THEN pn.data_pedido END)) as dias_desde_ultimo_pedido,
               MAX(pn.total_pedidos) as total_pedidos, AVG(pn.valor_total) as ticket_medio
        FROM PedidosNumerados pn GROUP BY pn.id_cliente, pn.nome_cliente ORDER BY dias_desde_ultimo_pedido;
    """
    df_rfm_final = run_query(query_rfm_100_porcento)
    if df_rfm_final is not None:
        df_rfm_final['ticket_medio'] = df_rfm_final['ticket_medio'].apply(lambda x: locale.currency(x, grouping=True))
        st.dataframe(df_rfm_final, use_container_width=True, hide_index=True)

with aba3:
    st.subheader("Questão 3: Alteração do Modelo de Dados")
    st.write(
        """
        **Cenário:** Permitir que um pedido tenha múltiplos clientes (compras compartilhadas).
        **Solução:** Implementar uma relação de **Muitos-para-Muitos** através de uma **tabela de junção**.
        """
    )
    st.image("prints/normalização de tabelas MUITOS X MUITOS.png", caption="Diagrama da Relação Muitos-para-Muitos.", use_container_width=True)
    st.code(
        """
-- Passo 1: Remover a coluna que limita o pedido a um único cliente.
ALTER TABLE pedidos DROP COLUMN id_cliente;

-- Passo 2: Criar a nova tabela de junção.
CREATE TABLE pedidos_clientes (
    id_pedido INT REFERENCES pedidos(id_pedido),
    id_cliente INT REFERENCES clientes(id_cliente),
    PRIMARY KEY (id_pedido, id_cliente)
);
        """, language='sql'
    )

with aba4:
    st.subheader("Questão 4: Top 5 Produtos Mais Rentáveis (Último Ano)")
    query_top_produtos_corrigida = """
        WITH receita_produto AS (
          SELECT ip.id_produto, SUM(ip.quantidade * ip.preco_unitario) AS total_vendas
          FROM itens_pedido AS ip JOIN pedidos AS p ON ip.id_pedido = p.id_pedido
          WHERE p.data_pedido >= CURRENT_DATE - INTERVAL '1 year' GROUP BY ip.id_produto
        )
        SELECT pr.id_produto, pr.nome, rp.total_vendas
        FROM receita_produto AS rp JOIN produtos AS pr ON rp.id_produto = pr.id_produto
        ORDER BY rp.total_vendas DESC LIMIT 5;
    """
    df_top_produtos = run_query(query_top_produtos_corrigida)
    if df_top_produtos is not None:
        df_top_produtos['total_vendas'] = df_top_produtos['total_vendas'].apply(lambda x: locale.currency(x, grouping=True))
        st.dataframe(df_top_produtos, use_container_width=True, hide_index=True)

with aba5:
    st.subheader("Questão 5: Análise de Tendências de Vendas Mensais")
    query_tendencia_vendas = """
        WITH VendasMensais AS (
          SELECT TO_CHAR(data_pedido, 'YYYY-MM') AS mes_ano, SUM(valor_total) AS total_vendas
          FROM pedidos GROUP BY mes_ano
        ), TendenciaVendas AS (
          SELECT mes_ano, total_vendas, LAG(total_vendas, 1, 0) OVER (ORDER BY mes_ano) AS vendas_mes_anterior
          FROM VendasMensais
        )
        SELECT mes_ano, total_vendas,
          CASE WHEN vendas_mes_anterior > 0 THEN ((total_vendas - vendas_mes_anterior) / vendas_mes_anterior) * 100 ELSE 0 END AS crescimento_percentual
        FROM TendenciaVendas ORDER BY mes_ano;
    """
    df_tendencia = run_query(query_tendencia_vendas)
    if df_tendencia is not None and not df_tendencia.empty:
        df_tendencia_display = df_tendencia.copy()
        df_tendencia_display['total_vendas'] = df_tendencia_display['total_vendas'].apply(lambda x: locale.currency(x, grouping=True))
        df_tendencia_display['crescimento_percentual'] = df_tendencia_display['crescimento_percentual'].map('{:,.2f}%'.format)
        st.dataframe(df_tendencia_display, use_container_width=True, hide_index=True)
        st.write("Gráfico de Tendência de Vendas Totais por Mês:")
        df_tendencia.set_index('mes_ano', inplace=True)
        st.line_chart(df_tendencia['total_vendas'])

with aba6:
    st.subheader("Questão 6: Identificação de Clientes Inativos")
    query_clientes_inativos_corrigida = """
        WITH AtividadeCliente AS (
          SELECT c.id_cliente, c.nome AS nome_cliente, MAX(p.data_pedido) AS data_ultimo_pedido
          FROM clientes AS c LEFT JOIN pedidos AS p ON c.id_cliente = p.id_cliente
          GROUP BY c.id_cliente, c.nome
        )
        SELECT id_cliente, nome_cliente, data_ultimo_pedido FROM AtividadeCliente
        WHERE data_ultimo_pedido < CURRENT_DATE - INTERVAL '6 months' OR data_ultimo_pedido IS NULL
        ORDER BY data_ultimo_pedido DESC NULLS LAST;
    """
    df_inativos = run_query(query_clientes_inativos_corrigida)
    if df_inativos is not None and not df_inativos.empty:
        st.write(f"Encontrados **{len(df_inativos)}** clientes inativos.")
        df_inativos['data_ultimo_pedido'] = df_inativos['data_ultimo_pedido'].fillna('Nunca comprou')
        st.dataframe(df_inativos, use_container_width=True, hide_index=True)
    elif df_inativos is not None:
        st.success("🎉 Todos os clientes estão ativos!")

with aba7:
    st.subheader("Questão 7: Detecção de Anomalias em Vendas")
    query_anomalias = """
        WITH ValorCalculadoPedido AS (
          SELECT id_pedido, SUM(quantidade * preco_unitario) AS valor_calculado
          FROM itens_pedido GROUP BY id_pedido
        )
        SELECT p.id_pedido, p.valor_total AS valor_total_registrado, vcp.valor_calculado
        FROM pedidos AS p JOIN ValorCalculadoPedido AS vcp ON p.id_pedido = vcp.id_pedido
        WHERE p.valor_total != vcp.valor_calculado;
    """
    df_anomalias = run_query(query_anomalias)
    if df_anomalias is not None and not df_anomalias.empty:
        st.warning(f"🚨 Encontradas **{len(df_anomalias)}** anomalias em pedidos!")
        df_anomalias_display = df_anomalias.copy()
        df_anomalias_display['valor_total_registrado'] = df_anomalias_display['valor_total_registrado'].apply(lambda x: locale.currency(x, grouping=True))
        df_anomalias_display['valor_calculado'] = df_anomalias_display['valor_calculado'].apply(lambda x: locale.currency(x, grouping=True))
        st.dataframe(df_anomalias_display, use_container_width=True, hide_index=True)
    elif df_anomalias is not None:
        st.success("✅ Nenhuma anomalia encontrada.")

with aba8:
    st.subheader("Questão 8: Otimização e Indexação")
    st.markdown("A performance das consultas é crucial. A principal estratégia de otimização é a criação de **índices** em colunas estratégicas.")
    st.markdown("##### 1. Índices em Chaves Estrangeiras (Foreign Keys)")
    st.write("Acelera drasticamente as operações de `JOIN`.")
    st.code("""
CREATE INDEX idx_pedidos_id_cliente ON pedidos(id_cliente);
CREATE INDEX idx_itens_pedido_id_pedido ON itens_pedido(id_pedido);
CREATE INDEX idx_itens_pedido_id_produto ON itens_pedido(id_produto);
    """, language='sql')
    st.markdown("##### 2. Índice em Colunas de Filtro (`WHERE`)")
    st.write("Acelera buscas por período (ex: último ano, últimos 6 meses).")
    st.code("CREATE INDEX idx_pedidos_data_pedido ON pedidos(data_pedido);", language='sql')

with aba10:
    st.subheader("Questão 10: Análise Exploratória com Pandas e Matplotlib")
    st.write("Investigando os dados para encontrar informações importantes.")
    
    df_produtos_q10 = run_query("SELECT categoria, nome, preco FROM produtos WHERE preco IS NOT NULL;")
    df_itens_q10 = run_query("SELECT quantidade, preco_unitario FROM itens_pedido;")

    plot_type = st.selectbox(
        "Escolha qual investigação você quer ver:",
        ["Como os preços se distribuem?", "Qual categoria é mais cara?", "Preço afeta a quantidade vendida?"],
        key="q10_final" 
    )
    st.markdown("---")
    
    if plot_type == "Como os preços se distribuem?" and df_produtos_q10 is not None:
        st.markdown("#### Investigação 1: Temos mais produtos caros ou baratos?")
        col1, col2 = st.columns([2, 1])
        with col1:
            fig, ax = plt.subplots()
            ax.hist(df_produtos_q10['preco'], bins=20, edgecolor='black', alpha=0.7, color='skyblue')
            ax.set_title("Distribuição de Preços dos Produtos")
            ax.set_xlabel("Faixa de Preço (R$)")
            ax.set_ylabel("Quantidade de Produtos")
            st.pyplot(fig)
        with col2:
            st.write("**O que este gráfico nos diz?**")
            st.info("As barras mais altas mostram as faixas de preço onde se concentra a maioria dos nossos produtos. Assim, descobrimos se nossa loja tem mais produtos em conta ou de luxo.")
            preco_medio = df_produtos_q10['preco'].mean()
            st.metric("Preço Médio de um Produto", locale.currency(preco_medio, grouping=True))

    elif plot_type == "Qual categoria é mais cara?" and df_produtos_q10 is not None:
        st.markdown("#### Investigação 2: Comparando os preços entre as categorias")
        st.info("**Como ler o gráfico:** Cada caixa é um 'resumo' dos preços de uma categoria. A linha no meio é o preço mais comum. Isso nos ajuda a ver qual categoria tem preços geralmente mais altos.")
        data_to_plot = df_produtos_q10.groupby('categoria')['preco'].apply(list)
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.boxplot(data_to_plot, labels=data_to_plot.index, patch_artist=True)
        ax.set_title("Comparação de Preços por Categoria")
        ax.set_xlabel("Categoria")
        ax.set_ylabel("Faixa de Preço (R$)")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)

    elif plot_type == "Preço afeta a quantidade vendida?" and df_itens_q10 is not None:
        st.markdown("#### Investigação 3: A relação entre o preço e a quantidade vendida")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write("**O que estamos procurando?**")
            st.info("Queremos ver se existe um padrão. Por exemplo, será que produtos mais caros vendem em menor quantidade?")
            st.write("**Nota de Correlação:**")
            correlacao = df_itens_q10['quantidade'].corr(df_itens_q10['preco_unitario'])
            st.metric("Correlação (de -1 a 1)", f"{correlacao:.2f}")
            st.write("**Se** a nota for perto de -1 (negativa): Significa que existe uma forte relação inversa. No nosso caso, confirmaria que quanto mais caro o produto, menor a quantidade vendida.")
            
            st.write("**Se** a nota for perto de +1 (positiva): Significa que existe uma forte relação direta (quanto mais caro, maior a quantidade vendida, o que é raro).")
            
            st.write("**Se** a nota for perto de 0: Significa que não existe uma ligação forte. O preço de um item não parece influenciar muito a quantidade que as pessoas compram dele em um pedido.")
        with col2:
            fig, ax = plt.subplots()
            ax.scatter(df_itens_q10['quantidade'], df_itens_q10['preco_unitario'], alpha=0.4, color='coral')
            ax.set_title("Dispersão: Preço Unitário vs. Quantidade")
            ax.set_xlabel("Quantidade Vendida")
            ax.set_ylabel("Preço Unitário (R$)")
            st.pyplot(fig)