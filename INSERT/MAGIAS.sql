WITH nova_magia AS (
    INSERT INTO Magia 
    (nome_magia, nivel, id_escola, tempo_conju, alcance, duracao, descricao_magia, is_ritual, is_concentration, somatico, verbal, material)
    VALUES (
        'ACALMAR EMOÇÕES', 
        2, 
        (SELECT id_escola FROM Escola_Magia WHERE nome_escola = 'Encantamento'),
        '1 ação', 
        '18 metros', 
        'Concentração, até 1 minuto', 
        'Você tenta suprimir emoções fortes...', 
        false, 
        true, 
        true, 
        true, 
        NULL
    )
    RETURNING id_magia 
)
INSERT INTO Magia_Origem (id_magia, id_classe)
SELECT id_magia, (SELECT id_classe FROM Classe WHERE nome_classe = 'Bardo') 
FROM nova_magia;