--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

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
-- Name: movement; Type: TABLE; Schema: public; Owner: aiosuperusercovid
--

CREATE TABLE public.movement (
    uniqid character varying(36) NOT NULL,
    value integer,
    created_at timestamp without time zone
);


ALTER TABLE public.movement OWNER TO aiosuperusercovid;

--
-- Data for Name: movement; Type: TABLE DATA; Schema: public; Owner: aiosuperusercovid
--

COPY public.movement (uniqid, value, created_at) FROM stdin;
\.


--
-- Name: movement movement_pkey; Type: CONSTRAINT; Schema: public; Owner: aiosuperusercovid
--

ALTER TABLE ONLY public.movement
    ADD CONSTRAINT movement_pkey PRIMARY KEY (uniqid);


--
-- PostgreSQL database dump complete
--

