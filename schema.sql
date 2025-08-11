--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

-- Started on 2025-08-11 10:15:40

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16481)
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    id_cliente integer NOT NULL,
    nome character varying(100),
    data_cadastro date
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16480)
-- Name: clientes_id_cliente_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clientes_id_cliente_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_id_cliente_seq OWNER TO postgres;

--
-- TOC entry 4829 (class 0 OID 0)
-- Dependencies: 217
-- Name: clientes_id_cliente_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clientes_id_cliente_seq OWNED BY public.clientes.id_cliente;


--
-- TOC entry 224 (class 1259 OID 16558)
-- Name: itens_pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.itens_pedido (
    id_item integer NOT NULL,
    id_pedido integer,
    id_produto integer,
    quantidade integer,
    preco_unitario numeric
);


ALTER TABLE public.itens_pedido OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16557)
-- Name: itens_pedido_id_item_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.itens_pedido_id_item_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.itens_pedido_id_item_seq OWNER TO postgres;

--
-- TOC entry 4830 (class 0 OID 0)
-- Dependencies: 223
-- Name: itens_pedido_id_item_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.itens_pedido_id_item_seq OWNED BY public.itens_pedido.id_item;


--
-- TOC entry 222 (class 1259 OID 16544)
-- Name: pedidos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedidos (
    id_pedido integer NOT NULL,
    data_pedido date,
    valor_total numeric,
    id_cliente integer
);


ALTER TABLE public.pedidos OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16543)
-- Name: pedidos_id_pedido_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pedidos_id_pedido_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pedidos_id_pedido_seq OWNER TO postgres;

--
-- TOC entry 4831 (class 0 OID 0)
-- Dependencies: 221
-- Name: pedidos_id_pedido_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pedidos_id_pedido_seq OWNED BY public.pedidos.id_pedido;


--
-- TOC entry 220 (class 1259 OID 16488)
-- Name: produtos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produtos (
    id_produto integer NOT NULL,
    nome character varying(100),
    categoria character varying(50),
    preco numeric
);


ALTER TABLE public.produtos OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16487)
-- Name: produtos_id_produto_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produtos_id_produto_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.produtos_id_produto_seq OWNER TO postgres;

--
-- TOC entry 4832 (class 0 OID 0)
-- Dependencies: 219
-- Name: produtos_id_produto_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produtos_id_produto_seq OWNED BY public.produtos.id_produto;


--
-- TOC entry 4656 (class 2604 OID 16484)
-- Name: clientes id_cliente; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id_cliente SET DEFAULT nextval('public.clientes_id_cliente_seq'::regclass);


--
-- TOC entry 4659 (class 2604 OID 16561)
-- Name: itens_pedido id_item; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.itens_pedido ALTER COLUMN id_item SET DEFAULT nextval('public.itens_pedido_id_item_seq'::regclass);


--
-- TOC entry 4658 (class 2604 OID 16547)
-- Name: pedidos id_pedido; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos ALTER COLUMN id_pedido SET DEFAULT nextval('public.pedidos_id_pedido_seq'::regclass);


--
-- TOC entry 4657 (class 2604 OID 16491)
-- Name: produtos id_produto; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos ALTER COLUMN id_produto SET DEFAULT nextval('public.produtos_id_produto_seq'::regclass);


--
-- TOC entry 4661 (class 2606 OID 16486)
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id_cliente);


--
-- TOC entry 4667 (class 2606 OID 16565)
-- Name: itens_pedido itens_pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.itens_pedido
    ADD CONSTRAINT itens_pedido_pkey PRIMARY KEY (id_item);


--
-- TOC entry 4665 (class 2606 OID 16551)
-- Name: pedidos pedidos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pedidos_pkey PRIMARY KEY (id_pedido);


--
-- TOC entry 4663 (class 2606 OID 16495)
-- Name: produtos produtos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT produtos_pkey PRIMARY KEY (id_produto);


--
-- TOC entry 4669 (class 2606 OID 16566)
-- Name: itens_pedido itens_pedido_id_pedido_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.itens_pedido
    ADD CONSTRAINT itens_pedido_id_pedido_fkey FOREIGN KEY (id_pedido) REFERENCES public.pedidos(id_pedido);


--
-- TOC entry 4670 (class 2606 OID 16571)
-- Name: itens_pedido itens_pedido_id_produto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.itens_pedido
    ADD CONSTRAINT itens_pedido_id_produto_fkey FOREIGN KEY (id_produto) REFERENCES public.produtos(id_produto);


--
-- TOC entry 4668 (class 2606 OID 16552)
-- Name: pedidos pedidos_id_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pedidos_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES public.clientes(id_cliente);


-- Completed on 2025-08-11 10:15:41

--
-- PostgreSQL database dump complete
--

