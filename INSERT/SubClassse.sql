INSERT INTO Subclasse (id_classe, nome_subclasse) VALUES
(
	(SELECT id_classe FROM Classe where nome_classe = 'Bruxo'),
	'A ArquiFada'
)