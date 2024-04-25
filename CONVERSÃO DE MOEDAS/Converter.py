def converter(v1,v2,m1,m2 )
def Troco(moeda1, moeda2):
    troco = 0
    if moeda1 == moeda2:
        return troco
    v1 = int(moeda1[0])
    v2 = int(moeda2[0])
    if moeda1[1] == moeda2[1]:
        if v1 > v2:
            troco = v1 - v2
            return str(troco)+"_"+moeda1[1]
        else:
            return "Moedas Insuficientes"
    else:
        converter(v1,v2, moeda1[1], moeda2[1])

entrada = "11_PO"
valor_a_pagar = "10_PO"
moeda1 = entrada.split("_")
moeda2 = valor_a_pagar.split("_")

print(Troco(moeda1, moeda2))
