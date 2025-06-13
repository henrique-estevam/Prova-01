quant = int(input("Quantos alunos têm na escola? "));
notas = [];
notas_acima = [];
notas_abaixo = [];

def escola(n):
    if quant > 2000: 
        print("O número de alunos precisa ser menor ou igual a 2000!");
        return
    else:
        for i in range(n):
            nota_individual = float(input(f"Digite a nota do aluno {i+1}: "));
            notas.append(nota_individual) ;
        dividendo = sum(notas);
        media = (dividendo/quant);
        print(f"A média da turma é: {media}");
        for nota in notas: 
            if nota>media*0.1: 
                notas_acima.append(nota);
            else:
                notas_abaixo.append(nota);
        print(f"{len(notas_acima)} alunos ficaram acima de 10% da média");
        print(f"{len(notas_abaixo)} alunos dicaram abaixo de 10% da média");

escola(quant);