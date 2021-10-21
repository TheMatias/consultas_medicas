CREATE TABLE paciente(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) not null,
    email VARCHAR(100) not null,
    CPF VARCHAR(11) not null,
    data_nasc TIMESTAMP,
    data_cadastro TIMESTAMP NOW; 
    senha VARCHAR(32),
    telefone VARCHAR(13)
);

CREATE TABLE medico(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) not null,
    email VARCHAR(100) not null,
    CRM VARCHAR(11) not null,
    telefone VARCHAR(13)  
);