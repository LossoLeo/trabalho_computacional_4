from numpy.polynomial import Polynomial as P
from numpy import polynomial

def function1():
    print("Interpolação de Lagrange")
    pontos = []
    k = 0
    while True:
        k += 1
        while True:
            print("Digite as coordenadas do ", k,"º ponto separados por espaço:", end="\nf para finalizar \n")
            l = input()
            if l == "f".lower():
                break
            l = l.split() 
            if len(l) == 2: 
                break
            else:
                print("Entrada inválida, tente novamente!")
        if l == "f".lower():
            break
        for i in range(len(l)):
            l[i] = float(l[i])
        pontos.append(l)

    Pn = 0

    for k in range(len(pontos)):
        numerador = P([1])
        denominador = P([1])
        for j in range(len(pontos)):
            if j == k:
                continue
            numerador *= P([-pontos[j][0], 1])
            denominador *= pontos[k][0] - pontos[j][0]
        Pn = Pn + pontos[k][1] * (numerador // denominador)
    funcao = list(Pn)
    texto = ""
    for i in range(len(funcao)):
        if funcao[i] == 0:
            continue
        elif i == 0:
            texto += str(funcao[i])
        else:
            texto += " + " + str(funcao[i])
            texto += ("*x^%o" % (i))
    print("Pn(x) :")
    print(texto)
    s = input(
        "Deseja calcular Pn(x) dado um valor de x? \n [S/N]").lower()
    if s == "s":
        print("Pn(x) em qual ponto?")
        p = float(input())
        print("Pn(%a) é igual a %a" % (p, Pn(p)))
    s = input(
        "Encontrar os valores de x dado um valor de Pn(x)? \n [S/N]")
    if s == "s":
        print("Valores de x para qual valor de Pn(x)")
        p = float(input())
        print("para Pn(x)=%a temos: " % p, polynomial.polynomial.polyroots(list(Pn - P([p]))),
            "Obs: Se houver, j = raiz de menos 1")
    print("(x,Pn(x))")
    for i in range(len(pontos)):
        print("(%a,%a)" % (pontos[i][0], round(Pn(pontos[i][0]), 4)))

def function2():
    print("Interpolação de Newton")
    pontos = []
    k = 0
    while True:
        k += 1
        while True:
            print("Digite as coordenadas do ", k, "º ponto separados por espaço:", end="\nf para finalizar \n")
            l = input()
            if l == "f".lower():  
                break
            l = l.split()
            if len(l) == 2:
                break
            else:
                print("Entrada inválida, tente novamente!")
        if l == "f".lower():
            break
        for i in range(len(l)): 
            l[i] = float(l[i])
        pontos.append(l)

    l = []
    for i in range(len(pontos)):
        l.append(pontos[i][1])
    tabela = [] 
    tabela.append(l)
    
    
    for i in range(len(pontos) - 1):
        l = []
        for j in range(len(pontos) - i - 1):
            dif = (tabela[i][j + 1] - tabela[i][j]) / (pontos[j + 1 + i][0] - pontos[j][0])
            l.append(dif)
        tabela.append(l)
    difdiv = [] 
    
    for i in range(len(tabela)):
        difdiv.append(tabela[i][0])
    
    somatorio = 0
    for i in range(1, len(pontos)):
        produtorio = 1
        for k in range(i): 
            produtorio *= (P([-pontos[k][0], 1])) 
        somatorio += difdiv[i] * produtorio
    Pn = difdiv[0] + somatorio
    funcao = list(Pn) 
    
    texto = ""
    for i in range(len(funcao)):
        if funcao[i] == 0:
            continue
        elif i == 0:
            texto += str(funcao[i])
        else:
            texto += " + " + str(funcao[i])
            texto += ("*x^%o" % (i))
    print("Pn(x) :")
    print(texto)
    s = input(
        "Deseja calcular Pn(x) dado um valor de x? \n [S/N]").lower() 
    if s == "s":
        print("Pn(x) em qual ponto?")
        p = float(input())
        print("Pn(%a) é igual a %a" % (p, Pn(p)))
    print("Raízes de Pn(x): ", polynomial.polynomial.polyroots(list(Pn)))
    s = input(
        "Encontrar os valores de x dado um valor de Pn(x)? \n [S/N]") 
    if s == "s":
        print("Valores de x para qual valor de Pn(x)")
        p = float(input())
        print("para Pn(x)=%a temos: " % p, polynomial.polynomial.polyroots(list(Pn - P([p]))),
            "Obs: Se houver, j = raiz de menos 1")
    
    print("(x,Pn(x))")
    for i in range(len(pontos)):
        print("(%a,%a)" % (pontos[i][0], round(Pn(pontos[i][0]), 4)))

def function3():
    print("Método de Newton-Gregory\n\n****Valores de X,Y e o F(x) estão definidos nas linhas: 164, 169-174, 189.****\n\n")
    def u_cal(u, n):

        temp = u;
        for i in range(1, n):
            temp = temp * (u - i);
        return temp;


    def fact(n):
        f = 1;
        for i in range(2, n + 1):
            f *= i;
        return f;


    #Numero de termos ---> n
    n = 6;
    x = [ 0 ,1 ,2 ,3 ,4 ,5 ]; #pode alterar.
        
    #Coordenadas dos pontos, pode alterar.
    y = [[0 for i in range(n)]
        for j in range(n)];
    y[0][0] = 1;
    y[1][0] = 2;
    y[2][0] = 4;
    y[3][0] = 8;
    y[4][0] = 16;
    y[5][0] = 32;


    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

    # Tabela de diferenças
    for i in range(n):
        print(x[i], end = "\t");
        for j in range(n - i):
            print(y[i][j], end = "\t");
        print("");

    # Valor do F(x) para calcular pode alterar.
    F_de_X = 4.12;

    #Iniciando a variavel soma e a variavel u
    soma = y[0][0];
    u = (F_de_X - x[0]) / (x[1] - x[0]);
    for i in range(1,n):
        soma = soma + (u_cal(u, i) * y[0][i]) / fact(i);

    print("\nValor do F(",F_de_X,") é igual a", round(soma, 6));

def switch(case):
    if case == "1":
        return function1
    elif case == "2":
        return function2
    elif case == "3":
        return function3

if __name__ == "__main__":
    print("Digite a opção:\n1-Lagrange\n2-Newton\n3-Newton-Gregory")
    opt = input()
    function = switch(opt)
    function()