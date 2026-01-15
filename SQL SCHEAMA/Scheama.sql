CREATE TABLE Escola_Magia (
    id_escola SERIAL PRIMARY KEY,
    nome_escola VARCHAR(50) NOT NULL
);
CREATE TABLE Classe (
    id_classe SERIAL PRIMARY KEY,
    nome_classe VARCHAR(50) NOT NULL,
);
CREATE TABLE habilidade_racial(
	id_habilidade serial PRIMARY KEY,
	nome_skill VARCHAR(50) NOT NULL,
	descricao text
);


CREATE TABLE Raca (
    id_raca SERIAL PRIMARY KEY,
    nome_raca VARCHAR(50) NOT NULL,
    descricao_raca TEXT,
    aprim_val_hab TEXT,
    tamanho VARCHAR(20),
    deslocamento INTEGER,
    proficiencias TEXT,
    idiomas TEXT
);

CREATE TABLE Sub_raca (
    id_subraca SERIAL PRIMARY KEY,
    id_raca INTEGER REFERENCES Raca(id_raca) ON DELETE CASCADE,
    nome_subraca VARCHAR(50),
    descricao_subraca TEXT,
    aprim_val_hab TEXT,
    proficiencias TEXT,
);

CREATE TABLE habilidade_raca (
    id_habilidade INTEGER REFERENCES habilidade_racial(id_habilidade),
    id_raca INTEGER REFERENCES Raca(id_raca),
    PRIMARY KEY (id_habilidade, id_raca)
);
CREATE TABLE habilidade_subraca (
    id_habilidade INTEGER REFERENCES habilidade_racial(id_habilidade),
    id_subraca INTEGER REFERENCES Raca(id_subraca),
    PRIMARY KEY (id_habilidade, id_raca)
);
