delete from public.tea;

COPY public.tea (id, title, tea_type, code, packaging, price, description, ingredients, instruction, tea_quantity) FROM stdin;
1	Hilltop Aristocratic Black Tea. Earl Grey	Black Tea	0001	100g	2.50	Delicate blend of Ceylon teas, lightly scented with the elegant flavor of bergamot. One of the favorite English teas.	Black tea flavored with a high dose of bergamot	One teaspoon of tea for 200 ml of boiled water. Wait 4-5 minutes	500
2	Hilltop Guru Black Tea.	Black Tea	0002	100g	2.70	Delicate blend of Ceylon teas. Created for true gurus	Black Guru tea	Boil it, drink it	200
3	Hilltop Meditation Black Tea	Black Tea	0003	100g	2.70	Delicate blend of Ceylon teas. Best for the piece of mind	Black meditation tea	Boil it, meditate, drink it	300
\.


delete from public.catalog;

COPY public.catalog (id, tea_category, tea_packing) FROM stdin;
1	Black Classic Tea	100g
2	Green Classic Tea	100g
3	Black Fruit Tea	100g
4	Testing Tea	1.5gx25
\.


delete from public.clients;

COPY public.clients (name, surname, email, phone, address, city, country, postal_code, id, discount) FROM stdin;
Taylor	Swift	taylor.swift@gmail.com	+392 60203109	Swift street 11 - 94	California	USA	TS-001	1	0
Fedor	Godhand	fedor.godhand@gmail.com	+371 21012102	Godhand street 1 - 12	Riga	Latvia	LV-002	2	10
TEST	Client	test.test@gmail.com	+371 20102010	Test street 1 - 1	Riga	Latvia	LV-003	3	0
\.


delete from public.admins;

COPY public.admins (name, surname, email, phone, address, city, country, postal_code, id) FROM stdin;
Admin	The Great	admin.great@gmail.com	+371 20002040	The Great street 11 - 244	Riga	Latvia	LV-003	1
Admin	Not So Great	admin.notgreat@gmail.com	+371 29392009	Not So Great street 19 - 192	Riga	Latvia	LV-008	2
\.


delete from public.orders;

COPY public.orders (id, tea_id, price, quantity, total_price, client_id, status, created_date, delivered_date) FROM stdin;
1	1	2.50	2	5	1	In Progress	2020-07-08 19:30:00	\N
2	2	2.70	1	2.70	1	Completed	2020-07-08 19:30:00	2020-07-09 19:30:00
3	1	2.50	1	2.25	2	In Progress	2020-07-08 19:30:00	\N
4	1	2.50	100	225	2	In Progress	2020-07-06 19:30:00	\N
\.


delete from public.company_contacts;

COPY public.company_contacts (id, email, requisites, phone, description) FROM stdin;
1	hilltop@gmail.com	LVHABA000232002323002323	+371 209090919	Hilltop - tea company serving finest tea in the world
2	reception@gmail.com	LVHABA000232002323002323	+371 20293921	Company reception address. Hilltop - tea company serving finest tea in the world
\.


delete from public.tea_catalog;

COPY public.tea_catalog (catalog_id, tea_id) FROM stdin;
1	1
1	2
4	3
\.



