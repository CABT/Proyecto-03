--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: album; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE album (
    id integer,
    nombre text,
    anio integer
);


ALTER TABLE public.album OWNER TO sango;

--
-- Name: banda; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE banda (
    id integer,
    nombre text
);


ALTER TABLE public.banda OWNER TO sango;

--
-- Name: genero; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE genero (
    id integer,
    nombre text
);


ALTER TABLE public.genero OWNER TO sango;

--
-- Name: pais; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE pais (
    id integer,
    nombre text
);


ALTER TABLE public.pais OWNER TO sango;

--
-- Name: relacion_banda_pais; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE relacion_banda_pais (
    banda_id integer,
    pais_id integer
);


ALTER TABLE public.relacion_banda_pais OWNER TO sango;

--
-- Name: relacion_usuario_pais; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE relacion_usuario_pais (
    usuario_id integer,
    pais_id integer
);


ALTER TABLE public.relacion_usuario_pais OWNER TO sango;

--
-- Name: tema; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE tema (
    id integer,
    nombre text
);


ALTER TABLE public.tema OWNER TO sango;

--
-- Name: usuario; Type: TABLE; Schema: public; Owner: sango; Tablespace: 
--

CREATE TABLE usuario (
    id integer,
    nombre character varying(80),
    administrador boolean,
    fecha_nacimiento date
);


ALTER TABLE public.usuario OWNER TO sango;

--
-- Data for Name: album; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY album (id, nombre, anio) FROM stdin;
\.


--
-- Data for Name: banda; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY banda (id, nombre) FROM stdin;
\.


--
-- Data for Name: genero; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY genero (id, nombre) FROM stdin;
\.


--
-- Data for Name: pais; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY pais (id, nombre) FROM stdin;
\.


--
-- Data for Name: relacion_banda_pais; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY relacion_banda_pais (banda_id, pais_id) FROM stdin;
\.


--
-- Data for Name: relacion_usuario_pais; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY relacion_usuario_pais (usuario_id, pais_id) FROM stdin;
\.


--
-- Data for Name: tema; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY tema (id, nombre) FROM stdin;
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: sango
--

COPY usuario (id, nombre, administrador, fecha_nacimiento) FROM stdin;
\.


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

