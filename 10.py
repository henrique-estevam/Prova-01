def inverter(dado):
    lista_i.append(dado);
    lista_i.sort(reverse=True);

def reverter(dado):
    invertido = int(str(dado)[::-1]);
    lista_r.append(invertido);

limite = int(input("Digite quantos números serão inseridos: "))
lista_i = [];
lista_r = [];

for i in range(limite):
    dado = int(input("Digite o número que entrará na lista: "));
    inverter(dado);
    reverter(dado);

print(f"Lista em ordem decrescente: {lista_i}");
print(f"Lista com números invertidos: {lista_r}");