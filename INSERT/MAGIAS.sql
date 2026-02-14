WITH nova_magia AS (
    INSERT INTO Magia
(nome_magia, nivel, id_escola, tempo_conju,alcance,duracao,descricao_magia,
is_ritual,is_concentration,somatico,verbal,material)
VALUES(
	'ACALMAR EMOÇÕES', 2, 
	(SELECT id_escola FROM Escola_Magia WHERE nome_escola = 'Encantamento'),
	'1 ação', '18 metros', 'Concentração, até 1 minuto', 
	'Você tenta suprimir emoções fortes em um grupo de pessoas. Cada humanoide em uma esfera de 6 metros de raio, centrada em um ponto que você escolher dentro do alcance, deve realizar um teste de resistência de Carisma; uma criatura pode escolher falhar nesse teste, se desejar. Se uma criatura falhar na resistência, escolha um dentre os dois efeitos a seguir. Você pode suprimir qualquer efeito que esteja deixando a criatura enfeitiçada ou amedrontada. Quando essa magia terminar, qualquer efeito suprimido volta a funcionar, considerando que sua duração não tenha acabado nesse meio tempo. Alternativamente, você pode tornar um alvo indiferente às criaturas que você escolher que forem hostis a ele. Essa indiferença acaba se o alvo for atacado ou ferido por uma magia ou se ele testemunhar qualquer dos seus amigos sendo ferido. Quando a magia terminar, a criatura se tornará hostil novamente, a não ser que o Mestre diga o contrário.',
	false, true, true, true, null  
	
)
    RETURNING id_magia 
),
ins_classes AS (
	INSERT INTO Magia_Origem (id_magia, id_classe)
    SELECT m.id_magia, c.id_classe 
    FROM nova_magia m, Classe c 
    WHERE c.nome_classe IN ('Bardo', 'Clérigo')
)
INSERT INTO Magia_Origem (id_magia, id_subclasse)
SELECT  m.id_magia, (SELECT id_subclasse  FROM Subclasse WHERE nome_subclasse  = 'A ArquiFada') 
FROM nova_magia m;