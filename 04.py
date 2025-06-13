def primo_ou_nao(x):
    for i in range(2, x+1): 
        if x % i == 0:
            print(f"{x} é primo");
            break
        else:
            print(f"{x} não é primo");
            break

nume = int(input("Digite o número que você quer checar: "));
primo_ou_nao(nume);