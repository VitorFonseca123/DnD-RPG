def subtrair(v1, v2, m1):
    if v1 > v2:
        troco = v1 - v2
        return str(troco)+ "_" + m1
    else:
        return "Moedas Insuficientes"
def converter(v1,v2,m1,m2 ):
    conversao = {
        "PL": {"PO": 10, "PE": 20, "PP": 100, "PC": 100},
        "PO": {"PL": 10, "PE": 2, "PP": 10, "PC": 100},
        "PE": {"PL": 20, "PO": 2, "PP": 5, "PC": 50},
        "PP": {"PL": 100, "PO": 10, "PE": 5, "PC": 10},
        "PC": {"PL": 1000, "PO": 100, "PE": 50, "PP": 10},
    }
    if m1 in conversao and m2 in conversao[m1]:
        if m1 == "PL":
            return v1 * conversao[m1][m2]
        if m1 == "PO" and m2 == "PL":
            return v2 * conversao[m2][m1]
        if m1 == "PE" and (m2 == "PL" or m2 == "PO"):
            return v2 * conversao[m2][m1]
        if m1 == "PP" and (m2 == "PL" or m2 == "PO" or m2 == "PE"):
            return v2 * conversao[m2][m1]
        if m1 == "PC":
            return v2 * conversao[m2][m1]

def Troco(moeda1, moeda2):
    troco = 0
    moeda1[1]= moeda1[1].upper()
    if moeda1 == moeda2:
        return troco+"_"+moeda1[1]
    v1 = int(moeda1[0])
    v2 = int(moeda2[0])
    if moeda1[1] == moeda2[1]:
      return subtrair(v1,v2)
    else:
        v2 = converter(v1,v2, moeda1[1], moeda2[1].upper())
        return subtrair(v1,v2, moeda1[1])
def main():
    entrada = "3_PE"
    valor_a_pagar = "1_Po"
    moeda1 = entrada.split("_")
    moeda2 = valor_a_pagar.split("_")

    print(Troco(moeda1, moeda2))

main()