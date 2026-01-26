
CREATE TABLE Escola_Magia (
    id_escola SERIAL PRIMARY KEY,
    nome_escola VARCHAR(50) NOT NULL
);
CREATE TABLE Classe (
    id_classe SERIAL PRIMARY KEY,
    nome_classe VARCHAR(50) NOT NULL
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
    aprim_val_hab VARCHAR(50),
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
    aprim_val_hab VARCHAR(50),
    proficiencias TEXT
);

CREATE TABLE Subclasse(
	id_subclasse SERIAL PRIMARY KEY,
	id_classe INTEGER REFERENCES Classe(id_classe) ON DELETE CASCADE,
	nome_subclasse VARCHAR(50),
	desc_subclasse TEXT
);
CREATE TABLE habilidade_origem (
	id_habilidadeOr SERIAL PRIMARY KEY,
    id_habilidade INTEGER REFERENCES habilidade(id_habilidade),
    id_raca INTEGER REFERENCES Raca(id_raca),
	id_subraca INTEGER REFERENCES Sub_raca(id_subraca),
	id_classe INTEGER REFERENCES Classe(id_classe),
	id_subclasse INTEGER REFERENCES Subclasse(id_subclasse)
    
);
CREATE TABLE Magia (
    id_magia SERIAL PRIMARY KEY,
    nome_magia VARCHAR(100) NOT NULL,
    nivel INTEGER NOT NULL,
    id_escola INTEGER REFERENCES Escola_Magia(id_escola),
    tempo_conju VARCHAR(50),
    alcance VARCHAR(50),
    duracao VARCHAR(50),
    descricao_magia TEXT,
    is_ritual BOOLEAN DEFAULT false,
    is_concentration BOOLEAN DEFAULT false,
    somatico BOOLEAN DEFAULT false,
    verbal BOOLEAN DEFAULT false,
    material TEXT
);

CREATE TABLE Magia_Origem (
	id_MagiaOR SERIAL PRIMARY KEY,
	id_magia INTEGER REFERENCES Magia(id_magia),
    id_raca INTEGER REFERENCES Raca(id_raca),
	id_subraca INTEGER REFERENCES Sub_raca(id_subraca),
	id_classe INTEGER REFERENCES Classe(id_classe),
	id_subclasse INTEGER REFERENCES Subclasse(id_subclasse)
    
);