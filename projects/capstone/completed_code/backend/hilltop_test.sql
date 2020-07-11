--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-10 02:24:09 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 203 (class 1259 OID 26762)
-- Name: tea; Type: TABLE; Schema: public; Owner: dkaminsky
--

CREATE TABLE public.tea (
    id integer NOT NULL,
    title character varying NOT NULL,
    tea_type character varying NOT NULL,
    code character varying NOT NULL,
    packaging character varying NOT NULL,
    price character varying NOT NULL,
    description character varying NOT NULL,
    ingredients character varying NOT NULL,
    instruction character varying,
    tea_quantity integer NOT NULL
);


ALTER TABLE public.tea OWNER TO dkaminsky;

--
-- TOC entry 202 (class 1259 OID 26760)
-- Name: tea_id_seq; Type: SEQUENCE; Schema: public; Owner: dkaminsky
--

CREATE SEQUENCE public.tea_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tea_id_seq OWNER TO dkaminsky;

--
-- TOC entry 3228 (class 0 OID 0)
-- Dependencies: 202
-- Name: tea_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dkaminsky
--

ALTER SEQUENCE public.tea_id_seq OWNED BY public.tea.id;


--
-- TOC entry 3090 (class 2604 OID 26765)
-- Name: tea id; Type: DEFAULT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.tea ALTER COLUMN id SET DEFAULT nextval('public.tea_id_seq'::regclass);


--
-- TOC entry 3222 (class 0 OID 26762)
-- Dependencies: 203
-- Data for Name: tea; Type: TABLE DATA; Schema: public; Owner: dkaminsky
--

COPY public.tea (id, title, tea_type, code, packaging, price, description, ingredients, instruction, tea_quantity) FROM stdin;
1	Hilltop Aristocratic Black Tea. Earl Grey	Black Tea	0001	100g	2.50	Delicate blend of Ceylon teas, lightly scented with the elegant flavor of bergamot. One of the favorite English teas.	Black tea flavored with a high dose of bergamot	One teaspoon of tea for 200 ml of boiled water. Wait 4-5 minutes	500
2	Hilltop Guru Black Tea.	Black Tea	0002	100g	2.70	Delicate blend of Ceylon teas. Created for true gurus	Black Guru tea	Boil it, drink it	200
3	Hilltop Meditation Black Tea	Black Tea	0003	100g	2.70	Delicate blend of Ceylon teas. Best for the piece of mind	Black meditation tea	Boil it, meditate, drink it	300
\.


--
-- TOC entry 3229 (class 0 OID 0)
-- Dependencies: 202
-- Name: tea_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dkaminsky
--

SELECT pg_catalog.setval('public.tea_id_seq', 3, true);


--
-- TOC entry 3092 (class 2606 OID 26770)
-- Name: tea tea_pkey; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.tea
    ADD CONSTRAINT tea_pkey PRIMARY KEY (id);


--
-- TOC entry 3094 (class 2606 OID 26772)
-- Name: tea tea_title_unique_key; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.tea
    ADD CONSTRAINT tea_title_unique_key UNIQUE (title);


-- Completed on 2020-07-10 02:24:09 EEST

--
-- PostgreSQL database dump complete
--




--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-10 02:25:06 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 205 (class 1259 OID 26775)
-- Name: catalog; Type: TABLE; Schema: public; Owner: dkaminsky
--

CREATE TABLE public.catalog (
    id integer NOT NULL,
    tea_category character varying NOT NULL,
    tea_packing character varying NOT NULL
);


ALTER TABLE public.catalog OWNER TO dkaminsky;

--
-- TOC entry 204 (class 1259 OID 26773)
-- Name: catalog_id_seq; Type: SEQUENCE; Schema: public; Owner: dkaminsky
--

CREATE SEQUENCE public.catalog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.catalog_id_seq OWNER TO dkaminsky;

--
-- TOC entry 3226 (class 0 OID 0)
-- Dependencies: 204
-- Name: catalog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dkaminsky
--

ALTER SEQUENCE public.catalog_id_seq OWNED BY public.catalog.id;


--
-- TOC entry 3090 (class 2604 OID 26778)
-- Name: catalog id; Type: DEFAULT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.catalog ALTER COLUMN id SET DEFAULT nextval('public.catalog_id_seq'::regclass);


--
-- TOC entry 3220 (class 0 OID 26775)
-- Dependencies: 205
-- Data for Name: catalog; Type: TABLE DATA; Schema: public; Owner: dkaminsky
--

COPY public.catalog (id, tea_category, tea_packing) FROM stdin;
1	Black Classic Tea	100g
2	Green Classic Tea	100g
3	Black Fruit Tea	100g
4	Testing Tea	1.5gx25
\.


--
-- TOC entry 3227 (class 0 OID 0)
-- Dependencies: 204
-- Name: catalog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dkaminsky
--

SELECT pg_catalog.setval('public.catalog_id_seq', 4, true);


--
-- TOC entry 3092 (class 2606 OID 26783)
-- Name: catalog catalog_pkey; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.catalog
    ADD CONSTRAINT catalog_pkey PRIMARY KEY (id);


-- Completed on 2020-07-10 02:25:06 EEST

--
-- PostgreSQL database dump complete
--




--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-10 02:25:30 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 207 (class 1259 OID 26786)
-- Name: clients; Type: TABLE; Schema: public; Owner: dkaminsky
--

CREATE TABLE public.clients (
    name character varying NOT NULL,
    surname character varying NOT NULL,
    email character varying NOT NULL,
    phone character varying NOT NULL,
    address character varying NOT NULL,
    city character varying NOT NULL,
    country character varying NOT NULL,
    postal_code character varying NOT NULL,
    id integer NOT NULL,
    discount integer
);


ALTER TABLE public.clients OWNER TO dkaminsky;

--
-- TOC entry 206 (class 1259 OID 26784)
-- Name: clients_id_seq; Type: SEQUENCE; Schema: public; Owner: dkaminsky
--

CREATE SEQUENCE public.clients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clients_id_seq OWNER TO dkaminsky;

--
-- TOC entry 3226 (class 0 OID 0)
-- Dependencies: 206
-- Name: clients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dkaminsky
--

ALTER SEQUENCE public.clients_id_seq OWNED BY public.clients.id;


--
-- TOC entry 3090 (class 2604 OID 26789)
-- Name: clients id; Type: DEFAULT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.clients ALTER COLUMN id SET DEFAULT nextval('public.clients_id_seq'::regclass);


--
-- TOC entry 3220 (class 0 OID 26786)
-- Dependencies: 207
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: dkaminsky
--

COPY public.clients (name, surname, email, phone, address, city, country, postal_code, id, discount) FROM stdin;
Taylor	Swift	taylor.swift@gmail.com	+392 60203109	Swift street 11 - 94	California	USA	TS-001	1	0
Fedor	Godhand	fedor.godhand@gmail.com	+371 21012102	Godhand street 1 - 12	Riga	Latvia	LV-002	2	10
TEST	Client	test.test@gmail.com	+371 20102010	Test street 1 - 1	Riga	Latvia	LV-003	3	0
\.


--
-- TOC entry 3227 (class 0 OID 0)
-- Dependencies: 206
-- Name: clients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dkaminsky
--

SELECT pg_catalog.setval('public.clients_id_seq', 3, true);


--
-- TOC entry 3092 (class 2606 OID 26794)
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (id);


-- Completed on 2020-07-10 02:25:30 EEST

--
-- PostgreSQL database dump complete
--




--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-10 02:25:56 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 209 (class 1259 OID 26797)
-- Name: admins; Type: TABLE; Schema: public; Owner: dkaminsky
--

CREATE TABLE public.admins (
    name character varying NOT NULL,
    surname character varying NOT NULL,
    email character varying NOT NULL,
    phone character varying NOT NULL,
    address character varying NOT NULL,
    city character varying NOT NULL,
    country character varying NOT NULL,
    postal_code character varying NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.admins OWNER TO dkaminsky;

--
-- TOC entry 208 (class 1259 OID 26795)
-- Name: admins_id_seq; Type: SEQUENCE; Schema: public; Owner: dkaminsky
--

CREATE SEQUENCE public.admins_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admins_id_seq OWNER TO dkaminsky;

--
-- TOC entry 3226 (class 0 OID 0)
-- Dependencies: 208
-- Name: admins_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dkaminsky
--

ALTER SEQUENCE public.admins_id_seq OWNED BY public.admins.id;


--
-- TOC entry 3090 (class 2604 OID 26800)
-- Name: admins id; Type: DEFAULT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.admins ALTER COLUMN id SET DEFAULT nextval('public.admins_id_seq'::regclass);


--
-- TOC entry 3220 (class 0 OID 26797)
-- Dependencies: 209
-- Data for Name: admins; Type: TABLE DATA; Schema: public; Owner: dkaminsky
--

COPY public.admins (name, surname, email, phone, address, city, country, postal_code, id) FROM stdin;
Admin	The Great	admin.great@gmail.com	+371 20002040	The Great street 11 - 244	Riga	Latvia	LV-003	1
Admin	Not So Great	admin.notgreat@gmail.com	+371 29392009	Not So Great street 19 - 192	Riga	Latvia	LV-008	2
\.


--
-- TOC entry 3227 (class 0 OID 0)
-- Dependencies: 208
-- Name: admins_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dkaminsky
--

SELECT pg_catalog.setval('public.admins_id_seq', 2, true);


--
-- TOC entry 3092 (class 2606 OID 26805)
-- Name: admins admins_pkey; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.admins
    ADD CONSTRAINT admins_pkey PRIMARY KEY (id);


-- Completed on 2020-07-10 02:25:56 EEST

--
-- PostgreSQL database dump complete
--



--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-10 02:26:28 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 214 (class 1259 OID 26836)
-- Name: orders; Type: TABLE; Schema: public; Owner: dkaminsky
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    tea_id integer,
    price character varying NOT NULL,
    quantity integer NOT NULL,
    total_price character varying NOT NULL,
    client_id integer,
    status character varying NOT NULL,
    created_date timestamp without time zone NOT NULL,
    delivered_date timestamp without time zone
);


ALTER TABLE public.orders OWNER TO dkaminsky;

--
-- TOC entry 213 (class 1259 OID 26834)
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: dkaminsky
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_seq OWNER TO dkaminsky;

--
-- TOC entry 3228 (class 0 OID 0)
-- Dependencies: 213
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dkaminsky
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- TOC entry 3090 (class 2604 OID 26839)
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- TOC entry 3222 (class 0 OID 26836)
-- Dependencies: 214
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: dkaminsky
--

COPY public.orders (id, tea_id, price, quantity, total_price, client_id, status, created_date, delivered_date) FROM stdin;
1	1	2.50	2	5	1	In Progress	2020-07-08 19:30:00	\N
2	2	2.70	1	2.70	1	Completed	2020-07-08 19:30:00	2020-07-09 19:30:00
3	1	2.50	1	2.25	2	In Progress	2020-07-08 19:30:00	\N
4	1	2.50	100	225	2	In Progress	2020-07-06 19:30:00	\N
\.


--
-- TOC entry 3229 (class 0 OID 0)
-- Dependencies: 213
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dkaminsky
--

SELECT pg_catalog.setval('public.orders_id_seq', 4, true);


--
-- TOC entry 3092 (class 2606 OID 26844)
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- TOC entry 3094 (class 2606 OID 26850)
-- Name: orders orders_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.clients(id);


--
-- TOC entry 3093 (class 2606 OID 26845)
-- Name: orders orders_tea_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_tea_id_fkey FOREIGN KEY (tea_id) REFERENCES public.tea(id);


-- Completed on 2020-07-10 02:26:28 EEST

--
-- PostgreSQL database dump complete
--




--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-10 02:26:48 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 211 (class 1259 OID 26808)
-- Name: company_contacts; Type: TABLE; Schema: public; Owner: dkaminsky
--

CREATE TABLE public.company_contacts (
    id integer NOT NULL,
    email character varying NOT NULL,
    requisites character varying NOT NULL,
    phone character varying,
    description character varying
);


ALTER TABLE public.company_contacts OWNER TO dkaminsky;

--
-- TOC entry 210 (class 1259 OID 26806)
-- Name: company_contacts_id_seq; Type: SEQUENCE; Schema: public; Owner: dkaminsky
--

CREATE SEQUENCE public.company_contacts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_contacts_id_seq OWNER TO dkaminsky;

--
-- TOC entry 3228 (class 0 OID 0)
-- Dependencies: 210
-- Name: company_contacts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dkaminsky
--

ALTER SEQUENCE public.company_contacts_id_seq OWNED BY public.company_contacts.id;


--
-- TOC entry 3090 (class 2604 OID 26811)
-- Name: company_contacts id; Type: DEFAULT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.company_contacts ALTER COLUMN id SET DEFAULT nextval('public.company_contacts_id_seq'::regclass);


--
-- TOC entry 3222 (class 0 OID 26808)
-- Dependencies: 211
-- Data for Name: company_contacts; Type: TABLE DATA; Schema: public; Owner: dkaminsky
--

COPY public.company_contacts (id, email, requisites, phone, description) FROM stdin;
1	hilltop@gmail.com	LVHABA000232002323002323	+371 209090919	Hilltop - tea company serving finest tea in the world
2	reception@gmail.com	LVHABA000232002323002323	+371 20293921	Company reception address. Hilltop - tea company serving finest tea in the world
\.


--
-- TOC entry 3229 (class 0 OID 0)
-- Dependencies: 210
-- Name: company_contacts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dkaminsky
--

SELECT pg_catalog.setval('public.company_contacts_id_seq', 2, true);


--
-- TOC entry 3092 (class 2606 OID 26816)
-- Name: company_contacts company_contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.company_contacts
    ADD CONSTRAINT company_contacts_pkey PRIMARY KEY (id);


--
-- TOC entry 3094 (class 2606 OID 26818)
-- Name: company_contacts company_email_key; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.company_contacts
    ADD CONSTRAINT company_email_key UNIQUE (email);


-- Completed on 2020-07-10 02:26:48 EEST

--
-- PostgreSQL database dump complete
--




--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-10 02:27:06 EEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 212 (class 1259 OID 26819)
-- Name: tea_catalog; Type: TABLE; Schema: public; Owner: dkaminsky
--

CREATE TABLE public.tea_catalog (
    catalog_id integer NOT NULL,
    tea_id integer NOT NULL
);


ALTER TABLE public.tea_catalog OWNER TO dkaminsky;

--
-- TOC entry 3220 (class 0 OID 26819)
-- Dependencies: 212
-- Data for Name: tea_catalog; Type: TABLE DATA; Schema: public; Owner: dkaminsky
--

COPY public.tea_catalog (catalog_id, tea_id) FROM stdin;
1	1
1	2
4	3
\.


--
-- TOC entry 3091 (class 2606 OID 26823)
-- Name: tea_catalog tea_catalog_pkey; Type: CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.tea_catalog
    ADD CONSTRAINT tea_catalog_pkey PRIMARY KEY (catalog_id, tea_id);


--
-- TOC entry 3092 (class 2606 OID 26824)
-- Name: tea_catalog tea_catalog_catalog_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.tea_catalog
    ADD CONSTRAINT tea_catalog_catalog_id_fkey FOREIGN KEY (catalog_id) REFERENCES public.catalog(id);


--
-- TOC entry 3093 (class 2606 OID 26829)
-- Name: tea_catalog tea_catalog_tea_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dkaminsky
--

ALTER TABLE ONLY public.tea_catalog
    ADD CONSTRAINT tea_catalog_tea_id_fkey FOREIGN KEY (tea_id) REFERENCES public.tea(id);


-- Completed on 2020-07-10 02:27:06 EEST

--
-- PostgreSQL database dump complete
--


