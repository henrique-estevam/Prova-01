x = int(input("Digite um dos números do intervalo: "));
y = int(input("Digite o outro número do intervalo: "));

if x > y:
    for i in range (y, x+1):
        if i % 5 == 2:
            print(i);
        if i % 5 == 3: 
            print(i);
else: 
    for i in range (x, y+1): 
        if i % 5 == 2: 
            print(i);
        if i % 5 == 3: 
            print(i);