CREATE TABLE Aluno 
( 
 ID_aluno INT PRIMARY KEY AUTO_INCREMENT,  
 CPF CHAR(n) NOT NULL,  
 EMAIL VARCHAR(n) NOT NULL,  
 NOME VARCHAR(n) NOT NULL,  
); 

CREATE TABLE Curso 
( 
 id_CURSO INT PRIMARY KEY AUTO_INCREMENT,  
 NOME VARCHAR(n) NOT NULL,  
); 

CREATE TABLE Matricula 
( 
 foreign key (id_CURSO) references Curso(id_CURSO),  
 foreign key (ID_aluno) references Aluno(ID_aluno),  
 DATA DATE NOT NULL,  
); 