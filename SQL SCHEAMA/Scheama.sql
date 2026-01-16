
CREATE TABLE Escola_Magia (
    id_escola SERIAL PRIMARY KEY,
    nome_escola VARCHAR(50) NOT NULL
);
CREATE TABLE Classe (
    id_classe SERIAL PRIMARY KEY,
    nome_classe VARCHAR(50) NOT NULL,
);
CREATE TABLE habilidade(
	id_habilidade serial PRIMARY KEY,
	nome_skill VARCHAR(50) NOT NULL,
	descricao text,
	lvl smallint 
);


CREATE TABLE Raca (
    id_raca SERIAL PRIMARY KEY,
    nome_raca VARCHAR(50) NOT NULL,
    descricao_raca TEXT,
    aprim_val_hab VARCHAR(2),
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
    aprim_val_hab VARCHAR(2),
    proficiencias TEXT,
);

CREATE TABLE Subclasse(
	id_subclasse SERIAL PRIMARY KEY,
	id_classe INTEGER REFERENCES Classe(id_classe) ON DELETE CASCADE,
	nome_subclasse VARCHAR(50),
	desc_subclasse TEXT
);
CREATE TABLE habilidade_origem (
    id_habilidade INTEGER REFERENCES habilidade_racial(id_habilidade),
    id_raca INTEGER REFERENCES Raca(id_raca),
	id_subraca INTEGER REFERENCES Sub_raca(id_subraca),
	id_classe INTEGER REFERENCES Classe(id_classe),
	id_subclasse INTEGER REFERENCES Subclasse(id_sublasse),
    PRIMARY KEY (id_habilidade, id_raca, id_subraca, id_classe, id_subclasse)
);

