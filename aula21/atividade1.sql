CREATE TABLE cliente 
( 
 ID_cliente INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(50),  
 gmail VARCHAR(50) NOT NULL,  
 idade INT NOT NULL,  
); 

CREATE TABLE pedido 
( 
 ID_pedido INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(50) NOT NULL,  
 valor FLOAT NOT NULL,  
 ID_cliente INT, 
 foreign key (ID_cliente) references cliente(ID_cliente) 
); 

CREATE TABLE produto 
( 
 ID_produto INT PRIMARY KEY,  
 nome VARCHAR(50) NOT NULL,  
 preço FLOAT NOT NULL,  
); 

CREATE TABLE item_pedido 
( 
 foreign key (ID_produto) references produto(ID_produto),  
 foreign key (ID_pedido) references pedido(ID_pedido),  
 quantidade INT NOT NULL,  
); 