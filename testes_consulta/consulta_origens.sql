SELECT nome_magia, Classe.nome_classe, nome_subclasse from Magia 
LEFT JOIN Magia_Origem ON Magia.id_magia = Magia_Origem.id_magia
LEFT JOIN Classe on Classe.id_classe = Magia_Origem.id_classe
LEFT JOIN Subclasse on Subclasse.id_subclasse = Magia_Origem.id_subclasse
WHERE Magia.id_magia = '1'
