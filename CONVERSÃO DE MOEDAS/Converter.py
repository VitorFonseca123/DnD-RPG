def converter(v1,v2,m1,m2 ):
    if m1 == "PL":
        # Se o pagamento for em peças de platina
        if m2 == "PO":
            return str((v1*10)-v2)+"_PO"
        elif m2 == "PE":
            return str((v1*20)-v2)+"_PE"
        elif m2 == "PP":
            return str((v1*100)-v2)+"_PP"
        elif m2 == "PC":
            return str((v1*100)-v2)+"_PC"
    elif m1 == "PO":
        # Se o pagamento for em peças de Ouro
        if m2 == "PL":
            convertido = v2*10
            if v1>(convertido):
                return str(v1-convertido)+"_PO"
            else:

def Troco(moeda1, moeda2):
    troco = 0
    if moeda1 == moeda2:
        return troco+"_"+moeda1[1]
    v1 = int(moeda1[0])
    v2 = int(moeda2[0])
    if moeda1[1] == moeda2[1]:
        if v1 > v2:
            troco = v1 - v2
            return str(troco)+"_"+moeda1[1]
        else:
            return "Moedas Insuficientes"
    else:
        return converter(v1,v2, moeda1[1].upper(), moeda2[1].upper())

entrada = "1_Pl"
valor_a_pagar = "9_Po"
moeda1 = entrada.split("_")
moeda2 = valor_a_pagar.split("_")

print(Troco(moeda1, moeda2))
