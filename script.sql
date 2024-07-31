CREATE DATABASE IF NOT EXISTS clinica;

USE clinica;

CREATE TABLE IF NOT EXISTS profissional (
    id int NOT NULL AUTO_INCREMENT,
    nome_completo varchar(255) NOT NULL,
    nome_social varchar(255),
    profissao varchar(50) NOT NULL,
   	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS contato (
    id int NOT NULL AUTO_INCREMENT,
    prefixo int NOT NULL,
    numero varchar(10),
   	PRIMARY KEY (id),
   	UNIQUE KEY unique_numero (prefixo, numero)
);

CREATE TABLE IF NOT EXISTS profissional_contato (
    id int NOT NULL AUTO_INCREMENT,
    id_profissional int NOT NULL,
    id_contato int NOT NULL,
   	PRIMARY KEY (id),
   	FOREIGN KEY (id_profissional) REFERENCES profissional(id),
   	FOREIGN KEY (id_contato) REFERENCES contato(id)
);


CREATE TABLE IF NOT EXISTS endereco (
    id int NOT NULL AUTO_INCREMENT,
    logradouro varchar(255) NOT NULL,
    numero varchar(30) NOT NULL,
    complemento varchar(50) NOT NULL,
    bairro varchar(50) NOT NULL,
    cidade varchar(50) NOT NULL,
    uf varchar(2) NOT NULL,
    cep varchar(8) NOT NULL,
   	PRIMARY KEY (id),
   	UNIQUE KEY unique_cep (cep)
);

CREATE TABLE IF NOT EXISTS profissional_endereco (
    id int NOT NULL AUTO_INCREMENT,
    id_profissional int NOT NULL,
    id_endereco int NOT NULL,
   	PRIMARY KEY (id),
   	FOREIGN KEY (id_profissional) REFERENCES profissional(id),
   	FOREIGN KEY (id_endereco) REFERENCES endereco(id)
);

CREATE TABLE IF NOT EXISTS consulta (
    id int NOT NULL AUTO_INCREMENT,
    data_consulta varchar(10),
    id_profissional int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_profissional) REFERENCES profissional(id)
);