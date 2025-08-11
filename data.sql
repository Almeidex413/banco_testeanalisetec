--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

-- Started on 2025-08-11 10:16:53

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4817 (class 0 OID 16481)
-- Dependencies: 218
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (id_cliente, nome, data_cadastro) FROM stdin;
1	LUCAS DE ALMEIDA E SILVA	2024-01-01
2	JERONIMA NATALINA DA SILVA RAMOS	2024-02-08
3	PAULO DA SILVA RAMOS	2024-03-15
4	INGRID GOMES DOS SANTOS	2025-10-12
5	CLAUDIA DE FATIMA ALMEIDA	2025-01-20
\.


--
-- TOC entry 4823 (class 0 OID 16558)
-- Dependencies: 224
-- Data for Name: itens_pedido; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.itens_pedido (id_item, id_pedido, id_produto, quantidade, preco_unitario) FROM stdin;
1	1	1	10	23.99
2	2	4	60	59.99
5	4	11	8	359
6	5	12	6	800
7	6	8	3	6000
8	7	16	100	49.90
9	8	17	100	39.90
10	9	18	250	69.90
11	10	13	10	100
12	11	14	500	3
15	14	11	8	359
16	15	12	6	800
17	16	8	3	6000
18	17	16	100	49.90
19	18	17	100	39.90
20	19	18	250	69.90
21	20	13	10	100
22	21	14	500	3
13	12	15	100	69.90
14	13	15	100	69.90
23	22	15	100	69.90
4	3	10	10	400
24	23	15	100	69.98
\.


--
-- TOC entry 4821 (class 0 OID 16544)
-- Dependencies: 222
-- Data for Name: pedidos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pedidos (id_pedido, data_pedido, valor_total, id_cliente) FROM stdin;
1	2024-02-13	239.9	1
2	2024-03-20	3599.4	1
3	2024-04-01	4000	1
4	2024-05-01	2872	1
5	2024-05-01	4800	1
6	2024-06-04	18000	1
7	2024-09-10	4990	1
8	2025-03-10	3990	1
9	2025-05-01	17475	1
10	2024-05-01	1000	2
11	2025-04-08	1500	2
12	2024-06-04	6990	2
13	2025-06-04	6990	2
14	2024-05-01	2872	3
15	2024-05-01	4800	3
16	2024-06-04	18000	3
17	2024-09-10	4990	3
18	2025-03-10	3990	3
19	2025-05-01	17475	3
20	2024-05-01	1000	3
21	2025-04-08	1500	3
22	2024-06-04	6990	3
23	2025-06-04	6990	3
\.


--
-- TOC entry 4819 (class 0 OID 16488)
-- Dependencies: 220
-- Data for Name: produtos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produtos (id_produto, nome, categoria, preco) FROM stdin;
1	Milka ao leite	Doces e guloseimas	23.99
2	Milka meio amargo	Doces e guloseimas	23.99
3	Milka com nozes	Doces e guloseimas	23.99
4	Boneco BEN 10	Brinquedos	59.99
5	Boneco Fofão	Brinquedos	199
6	Boneca Barbie	Brinquedos	299
7	Smartphone APPLE 16	Eletrônicos	18000
8	Smartphone SAMSUNG S21	Eletrônicos	6000
9	Smartphone ALMEIDEX T180	Eletrônicos	2000
10	Liquidificador	Eletroportáteis	400
11	Cafeteira	Eletroportáteis	359
12	Microondas	Eletroportáteis	800
13	Panela	Utilidades Domésticas	100
14	Pote pequeno	Utilidades Domésticas	3
15	Jogo de talheres	Utilidades Domésticas	69.90
16	Blusa feminina	Vestuário	49.90
17	Blusa masculina	Vestuário	39.90
18	Blusa unisex	Vestuário	69.90
19	Quem sou?	Livro	49.90
20	Receitas da Chiquinha	Livro	129.90
21	Codigo de Honra dos Samurais	Livro	200
\.


--
-- TOC entry 4833 (class 0 OID 0)
-- Dependencies: 217
-- Name: clientes_id_cliente_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clientes_id_cliente_seq', 10, true);


--
-- TOC entry 4834 (class 0 OID 0)
-- Dependencies: 223
-- Name: itens_pedido_id_item_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.itens_pedido_id_item_seq', 24, true);


--
-- TOC entry 4835 (class 0 OID 0)
-- Dependencies: 221
-- Name: pedidos_id_pedido_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pedidos_id_pedido_seq', 23, true);


--
-- TOC entry 4836 (class 0 OID 0)
-- Dependencies: 219
-- Name: produtos_id_produto_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produtos_id_produto_seq', 21, true);


-- Completed on 2025-08-11 10:16:53

--
-- PostgreSQL database dump complete
--

