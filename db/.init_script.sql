-- Tables
-- Ensure that tables are dropped before creating them
DROP TABLE IF EXISTS public.MATRICULAS;
DROP TABLE IF EXISTS public.CLIENTES;
DROP TABLE IF EXISTS public.DEPORTES;

-- Create tables
CREATE TABLE IF NOT EXISTS public.CLIENTES (NOMBRE text NOT NULL, DNI text NOT NULL, FNAC date, TELEFONO text, PRIMARY KEY (DNI));
ALTER TABLE IF EXISTS public.CLIENTES OWNER to admin;

CREATE TABLE IF NOT EXISTS public.DEPORTES (NOMBRE text NOT NULL, PRECIO numeric NOT NULL, PRIMARY KEY (NOMBRE));
ALTER TABLE IF EXISTS public.DEPORTES OWNER to admin;

CREATE TABLE IF NOT EXISTS public.MATRICULAS (DNI text NOT NULL, DEPORTE TEXT NOT NULL, HORARIO TEXT NOT NULL, PRIMARY KEY (DNI, DEPORTE), FOREIGN KEY (DNI) REFERENCES public.CLIENTES(DNI) ON DELETE CASCADE, FOREIGN KEY (DEPORTE) REFERENCES public.DEPORTES(NOMBRE) ON DELETE CASCADE);
ALTER TABLE IF EXISTS public.MATRICULAS OWNER to admin;

-- Initial data

insert into CLIENTES values ('Steffane Kender', '84459842F', '1953-12-04', '+34 548 001 402');
insert into CLIENTES values ('Freeland Pietroni', '13921379D', '1955-12-19', '+34 565 312 945');
insert into CLIENTES values ('Kara Faloon', '18861071F', '1999-11-03', '+34 797 141 001');
insert into CLIENTES values ('Leora Lethcoe', '78915656J', '1978-05-06', '+34 065 628 214');
insert into CLIENTES values ('Benjie Skacel', '77298723D', '1976-01-22', '+34 987 347 612');
insert into CLIENTES values ('Erin Stickland', '56922249W', '2002-10-16', '+34 659 461 360');
insert into CLIENTES values ('Gerladina MacKaig', '94609651Z', '2000-11-15', '+34 970 874 832');
insert into CLIENTES values ('Maybelle Blundell', '23213962Q', '1971-08-30', '+34 176 187 931');
insert into CLIENTES values ('Dalenna Bladge', '60520509A', '1987-06-27', '+34 637 607 060');
insert into CLIENTES values ('Fielding Reen', '01545165M', '2000-08-01', '+34 897 088 287');
insert into CLIENTES values ('Grata Tregonna', '46429307N', '1994-12-07', '+34 714 530 078');
insert into CLIENTES values ('Millie Applegate', '29748914I', '2002-04-19', '+34 408 263 959');
insert into CLIENTES values ('Wynny Younglove', '92585116W', '1975-03-24', '+34 455 710 229');
insert into CLIENTES values ('Christan Hanretty', '48994647X', '1946-03-13', '+34 742 695 561');

INSERT INTO public.DEPORTES VALUES ('tennis', 20);
INSERT INTO public.DEPORTES VALUES ('swimming', 15);
INSERT INTO public.DEPORTES VALUES ('track', 10);
INSERT INTO public.DEPORTES VALUES ('basket', 15);
INSERT INTO public.DEPORTES VALUES ('soccer', 15);

INSERT INTO public.MATRICULAS VALUES ('84459842F', 'track', 'morning');
INSERT INTO public.MATRICULAS VALUES ('84459842F', 'tennis', 'morning');
INSERT INTO public.MATRICULAS VALUES ('13921379D', 'soccer', 'evening');
INSERT INTO public.MATRICULAS VALUES ('13921379D', 'swimming', 'evening');
INSERT INTO public.MATRICULAS VALUES ('18861071F', 'track', 'morning');
INSERT INTO public.MATRICULAS VALUES ('78915656J', 'basket', 'evening');
INSERT INTO public.MATRICULAS VALUES ('77298723D', 'soccer', 'morning');
INSERT INTO public.MATRICULAS VALUES ('56922249W', 'tennis', 'evening');
INSERT INTO public.MATRICULAS VALUES ('94609651Z', 'swimming', 'morning');
INSERT INTO public.MATRICULAS VALUES ('23213962Q', 'track', 'evening');
INSERT INTO public.MATRICULAS VALUES ('60520509A', 'basket', 'morning');
INSERT INTO public.MATRICULAS VALUES ('01545165M', 'soccer', 'evening');
INSERT INTO public.MATRICULAS VALUES ('29748914I', 'swimming', 'evening');
INSERT INTO public.MATRICULAS VALUES ('48994647X', 'track', 'morning');

-- Remove all procedure:
DROP PROCEDURE IF EXISTS destroy_db;

CREATE PROCEDURE public.destroy_db() LANGUAGE 'sql' AS $BODY$ DROP TABLE IF EXISTS public.MATRICULAS; DROP TABLE IF EXISTS public.CLIENTES; DROP TABLE IF EXISTS public.DEPORTES; $BODY$;
ALTER PROCEDURE public.destroy_db() OWNER TO admin;
