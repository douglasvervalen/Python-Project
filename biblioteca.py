import numpy as np
from colored import fg, attr
from time import sleep

colors = True
if colors:
    white = fg(15)
    red = fg(1)
    red1 = fg(9)
    red2 = fg(196)
    green = fg(2)
    green1 = fg(10)
    green2 = fg(34)
    green4 = fg(46)
    green5 = fg(82)
    moss = fg(142)
    moss1 = fg(148)
    blue = fg(4)
    blue1 = fg(12)
    blue3 = fg(39)
    orange = fg(9)
    orange1 = fg(11)
    orange2 = fg(214)
    orange3 = fg(172)
    orange4 = fg(130)
    orange5 = fg(208)
    orange6 = fg(202)
    orange7 = fg(214)
    pink = fg(161)
    pink1 = fg(162)
    pink2 = fg(125)
    pink3 = fg(126)
    pink4 = fg(197)
    pink5 = fg(199)
    yellow = fg(226)
    yellow1 = fg(11)
    pink6 = fg(205)
    clay = fg(7)
    gray = fg(253)
    res = attr(0)
    bold = attr(1)
    sub = attr(7)
    rsub = attr(27)

#Mutiplica uma linha e soma com outra
def add(x, y, i, j):
    z = x.shape[0]
    matriz = np.eye(z)
    if i == j:
        matriz[i, i] = y + 1
    else:
        matriz[i, j] = y
    return matriz @ x
#Mutiplica uma linha por um escalar
def scale(x, i, j):
    y = x.shape[0]
    matriz = np.eye(y)
    matriz[j, j] = i
    return matriz @ x
#Troca linhas
def swap(x, i, j):
    y = x.shape[0]
    matriz = np.eye(y)
    matriz[i, i] = 0
    matriz[j, j] = 0
    matriz[i, j] = 1
    matriz[j, i] = 1
    return matriz @ x
#Soluções para matriz 3x4 e 4x5
def solucao3(m):
 x3 = m[2, 3] / m[2, 2]
 x2 = (m[1, 3] - (m[1, 2] * x3)) / m[1, 1]
 x1 = (m[0, 3] - (m[0, 2] * x3) - (m[0,1] * x2)) / m[0, 0]
 return x1, x2, x3
def solucao4(m):
    x4 = m[3, 4] / m[3, 3]
    x3 = (m[2, 4] - (m[2, 3] * x4)) / m[2, 2]
    x2 = (m[1, 4] - (m[1, 3] * x4) - (m[1, 2] * x3)) / m[1, 1]
    x1 = (m[0, 4] - (m[0, 3] * x4) - (m[0, 2] * x3) - (m[0, 1] * x2)) / m[0, 0]
    return x1, x2, x3, x4

#Cria uma matriz 2d
def criar_matriz():
    while True:
        tamanho = input(f"{white}{bold}Tamanho da Matriz no formato {orange7}({white}linha coluna{orange7}){white}: {res}").split()
        if len(tamanho) == 2:
            l, c = [int(value) for value in tamanho]
            matrix = np.zeros((l,c))
            t = 0
            i = 0
            counter = 0
            while i < l:
                x = input(f'{white}{bold}Linha {counter+1}: {res}').split()
                if len(x) == c:
                    for j in range(0, 2):
                        matrix[i, 0:c+1:1] = x
                    t += 1
                    i += 1
                    counter += 1
                else:
                    loading()
                    print(f'{red2}{bold}Entrada Inválida!!!')
                    print(f'Número de colunas entrado não compátivel com os da matriz')
                    print(f'Valor Entrado {white}{len(x)} {red2}Tamanho da Matriz {white}{c}{res}')
                    loading()
                    if counter == t:
                        i = t
            return matrix
            break
        else:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'Tamanho da Matriz deve ser indicado por {orange7}({white}Linha Coluna{orange7}) {red2}|| Ex: {white}(3 3){res}')
            loading()
#Cria um vetor de n dimensões
def criar_vetor():
    while True:
        y = input(f'{white}{bold}Tamanho do vetor: {res}').split()
        dimensao = [int(value) for value in y]
        if len(dimensao) == 1 and dimensao[0] != 0:
            dimensão = dimensao[0]
            vetor = np.zeros((1,dimensão))
            i = 0
            while i < 1:
                x = input(f'{white}{bold}Elementos do vetor: {res}').split()
                if len(x) == dimensão:
                    for i in range(0,2):
                        vetor[0,0:dimensão:1] = x
                    i += 1
                    realvetor = vetor.flatten()
                    return realvetor
                    break
                else:
                    loading()
                    print(f'{red2}{bold}Entrada Inválida!!!')
                    print(f'Números de elementos entrado não compátivel com o tamanho do {white}vetor')
                    print(f'{red2}Valor Entrado {white}{len(x)} {red2}Tamanho do Vetor {white}{dimensão}{res}')
                    loading()
        elif dimensao[0] == 0:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'Tamanho do {white}vetor {red2}deve ser maior que {white}{dimensao[0]}.{res}')
            loading()
        else:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'Tamanho do {white}vetor {red2}inválido{res}')
            loading()
#Cria um vetor com tamanho definido (1,3)
def criar_vetor_3():
    dimensão = 3
    vetor = np.zeros((1,dimensão))
    i = 0
    while i < 1:
        x = input(f'{white}{bold}Elementos do vetor no formato {orange7}({white}x y z{orange7}){white}: {res}')
        x = x.split()
        if len(x) == dimensão:
            for i in range(0,2):
                vetor[0,0:dimensão:1] = x
            i += 1
            realvetor = vetor.flatten()
            return realvetor
            break
        else:
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'Números de elementos entrado não compátivel com o tamanho do {white}vetor')
            print(f'{red2}Valor Entrado {white}{len(x)} {red2}Tamanho do {white}Vetor {white}{dimensão}{res}')
#Cria uma matriz quadrada
def criar_matriz_sqr():
    while True:
        y = input(f"{white}{bold}Tamanho da Matriz no formato {orange7}({white} x {orange7}){white}: {res}").split()
        dimensao = [int(value) for value in y]
        if len(dimensao) == 1 and dimensao[0] != 0:
            tamanho = dimensao[0]
            matrix = np.identity(tamanho)
            t = 0
            i = 0
            counter = 0
            while i < tamanho:
                x = input(f'{white}{bold}{orange}{white}Linha {counter+1}: {res}').split()
                if len(x) == tamanho:
                    for j in range(0, 2):
                        matrix[t, 0:tamanho+1:1] = x
                    t += 1
                    i += 1
                    counter += 1
                else:
                    loading()
                    print(f'{red2}{bold}Entrada Inválida!!!')
                    print(f'Número de {white}colunas {red2}não é compátivel com os da {white}matriz')
                    print(f'{red2}Valor Entrado {white}{len(x)} {red2}Tamanho da Matriz {white}{tamanho}.')
                    loading()
                    if counter == t:
                        i = t
            return matrix
            break
        elif dimensao[0] == 0:
            loading()
            print(f'{bold}{red2}Entrada Inválida!!!')
            print(f'Tamanho da {white}matriz {red2}deve ser maior que {white}{dimensao[0]}.{res}')
            loading()
        else:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'{red2}Tamanho da {white}matriz {red2}inválido{res}')
            loading()

#Geometria analitica
#Faz o produto escalar entre 2 vetores
def produto_escalar():
    while True:
        print(f"{pink}{bold}-=-=(Vetor A)=-=-{res}")
        a = criar_vetor()
        dim = a.size
        print(f"{blue3}{bold}-=-=(Vetor B)=-=-{res}")
        b = criar_vetor_copy(dim)
        multvetor = a * b
        result = sum(multvetor)
        return result
        break
#Faz o produto vetorial entre 2 vetores
def produto_vetorial():
    while True:
        print(f"{pink}{bold}-=-=(Vetor A)=-=-{res}")
        a = criar_vetor_3()
        print(f"{blue3}{bold}-=-=(Vetor B)=-=-{res}")
        b = criar_vetor_3()
        vetor = np.cross(a, b)
        return vetor
        break
#Faz o produto misto entre 3 vetores
def produto_misto():
    print(f"{blue}{bold}-=-=(Vetor u)=-=-{res}")
    u = criar_vetor_3()
    print(f"{orange7}{bold}-=-=(Vetor v)=-=-{res}")
    v = criar_vetor_3()
    print(f"{green}{bold}-=-=(Vetor w)=-=-{res}")
    w = criar_vetor_3()
    uvw = np.zeros((3,3))
    vetores = [u, v, w]
    c = 0
    for i in range(0,3):
        for j in range(0,2):
            uvw[c, 0:4:1] = vetores[c]
        c += 1
    result = determinante_copy(uvw)
    return result

#Algebra Linear
#Acha a determinante de uma matriz
def determinante():
    a = criar_matriz_sqr()
    result = np.linalg.det(a)
    return result
#Acha a matriz inversa
def matriz_inversa():
    a = criar_matriz_sqr()
    b = determinante_copy(a)
    if b != 0:
        result = np.linalg.inv(a)
        return result
    else:
        loading()
        print(f'{bold}{white}Matriz {red2}inválida!!!')
        print(f'{white}Matriz {red2}não admite inversa{res}')
#Acha a solução de um sistema
def soluçao_do_sistema():
    while True:
        x = (input(f'{white}{bold}Número de equações do sistema: {res}')).split()
        verify = [int(value) for value in x]
        recipiente = []
        count = 0
        if len(verify) == 1:
            tamanho = verify[0]
            while count < tamanho:
                for i in range(tamanho):
                    y = input(f'{white}{bold}Coeficientes da equação {i+1}:{res} ').split()
                    coef = [float(values) for values in y]
                    recipiente.append(coef)
                for k in range(tamanho):
                    if len(recipiente[0]) == len(recipiente[k - 1]):
                        count += 1
                    else:
                        count -= 1
                        print(f'{bold}{red2}As seguintes {white}equações {red2}possuem o número de coeficientes diferentes {white}{recipiente[0]} {red2}e {white}{recipiente[k - 1]}{res}')
                if count < tamanho:
                    recipiente.clear()
            equaçoes = np.asarray(recipiente)
            gambiarra = np.zeros((tamanho, tamanho))
            if equaçoes.shape == gambiarra.shape:
                sol = determinante_copy(equaçoes)
                if sol != 0:
                    index = 0
                    recipiente2 = []
                    while index < tamanho:
                        x2 = input(f'{white}{bold}Termo Independete da Equação {index+1}{res}: ').split()
                        ti = [float(values2) for values2 in x2]
                        if len(ti) == 1:
                            y2 = ti[0]
                            recipiente2.append(y2)
                            index += 1
                        else:
                            print(f'{red}{bold}Entrada Inválida!!!{res}')
                    termoindependente = np.asarray(recipiente2)
                    resultado = np.linalg.solve(equaçoes, termoindependente)
                    return resultado
                    break
                else:
                    resultado = []
                    return resultado
                    break
            else:
                loading()
                print(f'{red2}{bold}Sistema entrado não compátivel!!!')
                print(f'Por favor! entrar com um sistema do tipo: "2x2, 3x3, 4x4, nxn"{res}')
                loading()
        else:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!{res}')
            loading()
#Solução do sistema por Gauss-Jordan
def Gauss():
    np.set_printoptions(suppress=True)
    m = criar_matriz()
    loading()
    print(f'{bold}{orange7} Matriz Entrada {white}{res}')
    print(f'{bold}{white}{m}{res}')
    if m.shape[0] == 3:
        np.set_printoptions(suppress=True)
        contador = 0
        j = 0
        k = 1
        for i in range(0, 6):
            m = add(m, - m[k, j] / m[j, j], k, j)
            loading()
            mc3 = np.around(m, 4)
            print(f'{bold}{orange7} Passo: {white}{contador}{res}')
            print(f'{bold}{white}{mc3}{res}')
            contador += 1
            k += 1
            if k == j:
                k += 1
            if k > 2:
                k = 0
                j += 1
            if j > 3:
                j = 0
    if m.shape[0] == 4:
        np.set_printoptions(suppress=True)
        contador = 1
        j = 0
        k = 1
        for i in range(0, 12):
            m = add(m, - m[k, j] / m[j, j], k, j)
            loading()
            mc4 = np.around(m, 4)
            print(f'{bold}{orange7} Passo: {white}{contador}{res}')
            print(f'{bold}{white}{mc4}{res}')
            contador += 1
            k += 1
            if k == j:
                k += 1
            if k > 3:
                k = 0
                j += 1
            if j > 4:
                j = 0
    mf = np.around(m, 4)
    loading()
    print(f'{bold}{orange7} Matriz Final {white}{res}')
    print(f'{bold}{white}{mf}{res}')
    if m.shape[0] == 3:
        x1 = m[0, 3] / m[0, 0]
        x2 = m[1, 3] / m[1, 1]
        x3 = m[2, 3] / m[2, 2]
        loading()
        print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end='\n')
    if m.shape[0] == 4:
        x1 = m[0,4] / m[0, 0]
        x2 = m[1,4] / m[1, 1]
        x3 = m[2,4] / m[2, 2]
        x4 = m[3,4] / m[3, 3]
        loading()
        print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x4{white}: {x4:.4f}]', end='\n')
#Solução do sistema por Eliminação de Gauss
def Gauss_Elimination():
    np.set_printoptions(suppress=True)
    m = criar_matriz()
    loading()
    print(f'{bold}{orange7} Matriz Entrada {white}{res}')
    print(f'{bold}{white}{m}{res}')
    if m.shape[0] == 3:
        np.set_printoptions(suppress=True)
        j = 0
        k = 1
        contador = 1
        for i in range(0,2):
            if j == 0:
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc3 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador} {res}')
                print(f'{bold}{white}{mc3}{res}')
                print(j)
                contador += 1
                k += 1
            if k > 2:
                j += 1
            if j == 1:
                k = 2
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc3 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                print(f'{bold}{white}{mc3}{res}')
                contador += 1
                j += 1
    if m.shape[0] == 4:
        np.set_printoptions(suppress=True)
        j = 0
        contador = 1
        k = 1
        for i in range(0, 3):
            m = add(m, - m[k, j] / m[j, j], k, j)
            mc4 = np.around(m, 4)
            loading()
            print(f'{bold}{orange7} Passo: {white}{contador}{res}')
            print(f'{bold}{white}{mc4}{res}')
            contador += 1
            k += 1
            if k > 3:
                j += 1
            if j == 1:
                k = 2
                for x in range(0, 2):
                    m = add(m, - m[k, j] / m[j, j], k, j)
                    mc4 = np.around(m, 4)
                    loading()
                    print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                    print(f'{bold}{white}{mc4}{res}')
                    contador += 1
                    k += 1
                j += 1
            if j == 2:
                k = 3
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc4 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                print(f'{bold}{white}{mc4}{res}')
                contador += 1
    mf = np.around(m, 4)
    loading()
    print(f'{bold}{orange7} Matriz Final {white}{res}')
    print(f'{bold}{white}{mf}{res}')
    if m.shape[0] == 3:
        x1, x2, x3 = solucao3(m)
        loading()
        print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end='\n')
    if m.shape[0] == 4:
        x1, x2, x3, x4 = solucao4(m)
        loading()
        print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x4{white}: {x4:.4f}]', end='\n')
#Solução do sistema por Eliminação de Gauss c/ Troca de Linha
def Gauss_Elimination_L():
    np.set_printoptions(suppress=True)
    m = criar_matriz()
    loading()
    print(f'{bold}{orange7} Matriz Entrada {white}{res}')
    print(f'{bold}{white}{m}{res}')

    if m.shape[0] == 3:
        contador = 1
        j = 0
        k = 1
        n = 1
        for i in range(0, 2):
            if j == 0:
                if abs(m[0, j]) < abs(m[n + 1, j]):
                    m = swap(m, 0, n)
                if abs(m[0, j]) < abs(m[n, j]):
                    m = swap(m, 0, n)
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc3 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador} {res}')
                print(f'{bold}{white}{mc3}{res}')
                contador += 1
                k += 1
            if k > 2:
                j += 1
                n = 1
            if j == 1:
                if abs(m[1, j]) < abs(m[n + 1, j]):
                    m = swap(m, 1, n)
                if abs(m[1, j]) < abs(m[n, j]):
                    m = swap(m, 1, n)
                k = 2
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc3 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                print(f'{bold}{white}{mc3}{res}')
                contador += 1
                j += 1

    if m.shape[0] == 4:
        np.set_printoptions(suppress=True)
        contador = 1
        j = 0
        k = 1
        n = 1
        for i in range(0, 3):
            if abs(m[0, j]) < abs(m[n + 1, j]):
                m = swap(m, 0, n + 1)
            if abs(m[0, j]) < abs(m[n, j]):
                m = swap(m, 0, n)
            m = add(m, - m[k, j] / m[j, j], k, j)
            mc4 = np.around(m, 4)
            loading()
            print(f'{bold}{orange7} Passo: {white}{contador}{res}')
            print(f'{bold}{white}{mc4}{res}')
            contador += 1
            k += 1
            if k > 3:
                j += 1
            if j == 1:
                n = 2
                if abs(m[1, j]) < abs(m[n + 1, j]):
                    m = swap(m, 1, n + 1)
                if abs(m[1, j]) < abs(m[n, j]):
                    m = swap(m, 1, n)
                k = 2
                for x in range(0, 2):
                    m = add(m, - m[k, j] / m[j, j], k, j)
                    mc4 = np.around(m, 4)
                    loading()
                    print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                    print(f'{bold}{white}{mc4}{res}')
                    contador += 1
                    k += 1
                j += 1
            if j == 2:
                n = 2
                if abs(m[0, j]) < abs(m[n + 1, j]):
                    m = swap(m, 2, n + 1)
                if abs(m[0, j]) < abs(m[n, j]):
                    m = swap(m, 2, n)
                k = 3
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc4 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                print(f'{bold}{white}{mc4}{res}')
                contador += 1
    mf = np.around(m, 4)
    loading()
    print(f'{bold}{orange7} Matriz Final {white}{res}')
    print(f'{bold}{white}{mf}{res}')
    if m.shape[0] == 3:
        x1, x2, x3 = solucao3(m)
        loading()
        print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end='\n')
    if m.shape[0] == 4:
        x1, x2, x3, x4 = solucao4(m)
        loading()
        print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end=' ')
        print(f'{bold}{white}[{orange7}x4{white}: {x4:.4f}]', end='\n')
#Solução do sistema fatorando a matriz A por duas matrizes lower e uper
def Fatoracao_LU():
    global multiplicadores

    def lu(l, m):
        for p in range(0, 2):
            l[p + 1, 0] = m[p]
        l[2, 1] = m[2]

    def lu2(l, m):
        for p in range(0, 3):
            l[p + 1, 0] = m[p]
        for i in range(0, 2):
            l[i + 2, 1] = m[i + 3]
        l[3, 2] = m[5]

    def col(x, y, z):
        a = np.array([[1.0], [1.0], [1.0]])
        a[0] = x
        a[1] = y
        a[2] = z
        return a
    def col2(x, y, z, w):
        a = np.array([[1.0], [1.0], [1.0], [1.0]])
        a[0] = x
        a[1] = y
        a[2] = z
        a[3] = w
        return a

    def solucaop3(m):
        x1 = m[0, 3] / m[0, 0]
        x2 = (m[1, 3] - (m[1, 0] * x1)) / m[1, 1]
        x3 = (m[2, 3] - (m[2, 0] * x1) - (m[2, 1] * x2)) / m[2, 2]
        return x1, x2, x3

    def solucaop4(m):
        x1 = m[0, 4] / m[0, 0]
        x2 = (m[1, 4] - (m[1, 0] * x1)) / m[1, 1]
        x3 = (m[2, 4] - (m[2, 0] * x1) - (m[2, 1] * x2)) / m[2, 2]
        x4 = (m[3, 4] - (m[3, 0] * x1) - (m[3, 1] * x2) - (m[3,2] * x3)) / m[3, 3]
        return x1, x2, x3, x4

    np.set_printoptions(suppress=True)
    m = criar_matriz_sqr()
    loading()
    print(f'{bold}{orange7} Matriz {blue1}A {white}{res}')
    print(f'{bold}{white}{m}{res}')
    if m.shape[0] == 3:
        np.set_printoptions(suppress=True)
        multiplicadores = []
        j = 0
        k = 1
        contador = 1
        for i in range(0,2):
            if j == 0:
                multiplicadores.append(m[k, j] / m[j, j])
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc3 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador} {res}')
                print(f'{bold}{white}{mc3}{res}')
                print(f'{bold}{orange7} Multiplicador: {white}{multiplicadores[i]:.4f} {white}{res}')
                contador += 1
                k += 1
            if k > 2:
                j += 1
            if j == 1:
                k = 2
                multiplicadores.append(m[k, j] / m[j, j])
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc3 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                print(f'{bold}{white}{mc3}{res}')
                print(f'{bold}{orange7} Multiplicador: {white}{multiplicadores[2]:.4f} {white}{res}')
                contador += 1
                j += 1
    if m.shape[0] == 4:
        np.set_printoptions(suppress=True)
        multiplicadores = []
        j = 0
        contador = 1
        k = 1
        for i in range(0, 3):
            multiplicadores.append(m[k, j] / m[j, j])
            m = add(m, - m[k, j] / m[j, j], k, j)
            mc4 = np.around(m, 4)
            loading()
            print(f'{bold}{orange7} Passo: {white}{contador}{res}')
            print(f'{bold}{white}{mc4}{res}')
            print(f'{bold}{orange7} Multiplicador: {white}{multiplicadores[i]:.4f} {white}{res}')
            contador += 1
            k += 1
            if k > 3:
                j += 1
            if j == 1:
                k = 2
                for x in range(0, 2):
                    multiplicadores.append(m[k, j] / m[j, j])
                    m = add(m, - m[k, j] / m[j, j], k, j)
                    mc4 = np.around(m, 4)
                    loading()
                    print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                    print(f'{bold}{white}{mc4}{res}')
                    print(f'{bold}{orange7} Multiplicador: {white}{multiplicadores[3]:.4f} {white}{res}')
                    contador += 1
                    k += 1
                j += 1
            if j == 2:
                k = 3
                multiplicadores.append(m[k, j] / m[j, j])
                m = add(m, - m[k, j] / m[j, j], k, j)
                mc4 = np.around(m, 4)
                loading()
                print(f'{bold}{orange7} Passo: {white}{contador}{res}')
                print(f'{bold}{white}{mc4}{res}')
                print(f'{bold}{orange7} Multiplicador: {white}{multiplicadores[4]:.4f} {white}{res}')
                contador += 1
    mults = np.asarray(multiplicadores)
    mf = np.around(m, 4)
    loading()
    print(f'{bold}{orange7} Matriz {blue1}U {white}{res}')
    print(f'{bold}{white}{mf}{res}')
    if m.shape[0] == 3:
        l = np.identity(3)
        lu(l,mults)
        lf = np.around(l, 7)
        loading()
        print(f'{bold}{orange7} Matriz {blue1}L {white}{res}')
        print(f'{bold}{white}{lf}{res}')
        loading()
        print(f'{bold}{orange7} Multiplicadores: {white}{mults} {white}{res}')
        process = True
        while process:
            loading()
            request = input(f'{bold}{white}Valores de y no formato {orange7}({white}b1 b2 b3{orange7}){white}: {res}').split()
            if len(request) == 3:
                c1, c2, c3 = [float(value) for value in request]
                vy = np.array([[c1],[c2],[c3]])
                ly = np.hstack((l, vy))
                y1, y2, y3 = solucaop3(ly)
                loading()
                print(f'{bold}{white}[{orange7}y1{white}: {y1:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}y2{white}: {y2:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}y3{white}: {y3:.4f}]', end='\n')
                lyr = col(y1, y2, y3)
                u = np.hstack((m, lyr))
                x1, x2, x3 = Gauss_Elimination_copy(u)
                print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end='\n')
                while True:
                    loading()
                    verif = input(f'{bold}{white}Quer repetir o processo para y? (y/n): {res}')
                    if verif == 'y' or verif == 'yes' or verif == 'sim' or verif == 's':
                        process = True
                        break
                    elif verif == 'n' or verif == 'no' or verif == 'nao' or verif == 'não':
                        process = False
                        break
                    else:
                        loading()
                        print(f'{bold}{red2}Entrada Inválida!!!')
                        print(f'{bold}{red2}A escolha deve ser indicada por {white}y {red2}ou {white}n{res}')
                        continue
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devem estar no formato {orange7}({white}b1 b2 b3{orange7}){res}')
                loading()
    if m.shape[0] == 4:
        l = np.identity(4)
        lu2(l, mults)
        lf = np.around(l, 7)
        loading()
        print(f'{bold}{orange7} Matriz {blue1}L {white}{res}')
        print(f'{bold}{white}{lf}{res}')
        loading()
        print(f'{bold}{orange7} Multiplicadores: {white}{mults} {white}{res}')
        process = True
        while process:
            loading()
            request = input(f'{bold}{white}Valores de y no formato {orange7}({white}b1 b2 b3 b4{orange7}){white}: {res}').split()
            if len(request) == 4:
                c1, c2, c3, c4 = [float(value) for value in request]
                vy = np.array([[c1], [c2], [c3], [c4]])
                ly = np.hstack((l, vy))
                y1, y2, y3, y4 = solucaop4(ly)
                loading()
                print(f'{bold}{white}[{orange7}y1{white}: {y1:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}y2{white}: {y2:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}y3{white}: {y3:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}y4{white}: {y4:.4f}]', end='\n')
                lyr = col2(y1, y2, y3, y4)
                u = np.hstack((m, lyr))
                x1, x2, x3, x4 = Gauss_Elimination_copy(u)
                print(f'{bold}{white}[{orange7}x1{white}: {x1:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x2{white}: {x2:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x3{white}: {x3:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x4{white}: {x4:.4f}]', end='\n')
                while True:
                    loading()
                    verif = input(f'{bold}{white}Quer repetir o processo para y? (y/n): {res}')
                    if verif == 'y' or verif == 'yes' or verif == 'sim' or verif == 's':
                        process = True
                        break
                    elif verif == 'n' or verif == 'no' or verif == 'nao' or verif == 'não':
                        process = False
                        break
                    else:
                        loading()
                        print(f'{bold}{red2}Entrada Inválida!!!')
                        print(f'{bold}{red2}A escolha deve ser indicada por {white}y {red2}ou {white}n{res}')
                        continue
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devem estar no formato {orange7}({white}b1 b2 b3 b4{orange7}){res}')
                loading()
#Solução do sistema por Gauss-Jacobi
def Gauss_Xanosk():
    m = criar_matriz()
    if m.shape[0] == 3:
        l11 = (abs(m[0, 1]) + abs(m[0, 2]))
        l22 = (abs(m[1, 0]) + abs(m[1, 2]))
        l33 = (abs(m[2, 0]) + abs(m[2, 1]))
        c11 = (abs(m[1, 0]) + abs(m[2, 0]))
        c22 = (abs(m[0, 1]) + abs(m[2, 1]))
        c33 = (abs(m[0, 2]) + abs(m[1, 2]))
        verify = False
        if abs(c11) <= abs(m[0, 0]) and abs(c22) <= abs(m[1, 1]) and abs(c33) <= abs(m[2, 2]):
            verify = True
        elif abs(l11) <= abs(m[0, 0]) and abs(l22) <= abs(m[1, 1]) and abs(l33) <= abs(m[2, 2]):
            verify = True
        else:
            loading()
            print(f'{bold}{white}Sistema {red2}Inválido!!!')
            print(f'{red2}Critérios de convergência não atendindos!{res}')
        while verify:
            loading()
            kinicial = input(f'{bold}{white}Valores iniciais de x1, x2 e x3 no '
                             f'formato {orange7}({white}x1 x2 x3{orange7}){white}: {res}').split()
            if len(kinicial) == 3:
                x0, y0, z0 = [float(values) for values in kinicial]
                erro = float(input(f'{bold}{white}Erro Permitido: {res}'))
                k = 1
                while verify:
                    x = (m[0, 3] - (m[0, 2] * z0) - (m[0, 1] * y0)) / m[0, 0]
                    y = (m[1, 3] - (m[1, 2] * z0) - (m[1, 0] * x0)) / m[1, 1]
                    z = (m[2, 3] - (m[2, 1] * y0) - (m[2, 0] * x0)) / m[2, 2]
                    loading()
                    print(f'{bold}{orange7}Interação: {white}{k}{res}')
                    print(f'{bold}{white}[{orange7}x1{white}: {x:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x2{white}: {y:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange}x3{white}: {z:.4f}]', end='\n')
                    ex = (abs(x) - abs(x0))
                    ey = (abs(y) - abs(y0))
                    ez = (abs(z) - abs(z0))
                    print(f'{bold}{white}[{orange7}|x1({k}) - x1({k - 1})| = {abs(ex):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x2({k}) - x2({k - 1})| = {abs(ey):.4f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x3({k}) - x3({k - 1})| = {abs(ez):.8f}{white}]', end='\n')
                    if abs(ex) < erro and abs(ey) < erro and abs(ez) < erro:
                        verify = False
                    else:
                        x0 = x
                        y0 = y
                        z0 = z
                        k += 1
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devem estar no formato {orange7}({white}x1 x2 x3{orange7}){res}')
    if m.shape[0] == 4:
        l11 = (abs(m[0, 1]) + abs(m[0, 2]) + abs(m[0, 3]))
        l22 = (abs(m[1, 0]) + abs(m[1, 2]) + abs(m[1, 3]))
        l33 = (abs(m[2, 0]) + abs(m[2, 1]) + abs(m[2, 3]))
        l44 = (abs(m[3, 0]) + abs(m[3, 1]) + abs(m[3, 2]))
        c11 = (abs(m[1, 0]) + abs(m[2, 0]) + abs(m[3, 0]))
        c22 = (abs(m[0, 1]) + abs(m[2, 1]) + abs(m[3, 1]))
        c33 = (abs(m[0, 2]) + abs(m[1, 2]) + abs(m[3, 2]))
        c44 = (abs(m[0, 3]) + abs(m[1, 3]) + abs(m[2, 3]))
        verify = False
        if abs(c11) <= abs(m[0, 0]) and abs(c22) <= abs(m[1, 1]) and abs(c33) <= abs(m[2, 2]) and abs(c44) <= abs(m[3, 3]):
            verify = True
        elif abs(l11) <= abs(m[0, 0]) and abs(l22) <= abs(m[1, 1]) and abs(l33) <= abs(m[2, 2]) and abs(l44) <= abs(
                m[3, 3]):
            verify = True
        else:
            print(f'{bold}{white}Sistema {red2}Inválido!!!')
            print(f'{red2}Critérios de convergência não atendindos!{res}')
        while verify:
            kinicial = input(f'{bold}{white}Valores iniciais de x1, x2, x3 e x4 no '
                             f'formato {orange7}({white}x1 x2 x3 x4{orange7}){white}: {res}').split()
            if len(kinicial) == 4:
                x0, y0, z0, w0 = [float(values) for values in kinicial]
                erro = float(input(f'{bold}{white}Erro Permitido: {res}'))
                k = 1
                while verify:
                    x = (m[0, 4] - (m[0, 2] * z0) - (m[0, 1] * y0) - (m[0, 3] * w0)) / m[0, 0]
                    y = (m[1, 4] - (m[1, 2] * z0) - (m[1, 0] * x0) - (m[1, 3] * w0)) / m[1, 1]
                    z = (m[2, 4] - (m[2, 1] * y0) - (m[2, 0] * x0) - (m[2, 3] * w0)) / m[2, 2]
                    w = (m[3, 4] - (m[3, 1] * y0) - (m[3, 0] * x0) - (m[3, 2] * z0)) / m[3, 3]
                    loading()
                    print(f'{bold}{orange7}Interação: {white}{k}{res}')
                    print(f'{bold}{white}[{orange7}x1{white}: {x:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x2{white}: {y:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x3{white}: {z:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x4{white}: {w:.4f}]', end='\n')
                    ex = (abs(x) - abs(x0))
                    ey = (abs(y) - abs(y0))
                    ez = (abs(z) - abs(z0))
                    ew = (abs(w) - abs(w0))
                    print(f'{bold}{white}[{orange7}|x1({k}) - x1({k - 1})| = {abs(ex):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x2({k}) - x2({k - 1})| = {abs(ey):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x3({k}) - x3({k - 1})| = {abs(ez):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x4({k}) - x4({k - 1})| = {abs(ew):.8f}{white}]', end='\n')
                    if abs(ex) < erro and abs(ey) < erro and abs(ez) < erro and abs(ew) < erro:
                        verify = False
                    else:
                        x0 = x
                        y0 = y
                        z0 = z
                        w0 = w
                        k += 1
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devem estar no formato {orange7}({white}x1 x2 x3 x4{orange7}){res}')
#Solução do sistema por Gauss-Seidel
def Gauss_Seidel():
    m = criar_matriz()
    if m.shape[0] == 3:
        l11 = (abs(m[0, 1]) + abs(m[0, 2]))
        l22 = (abs(m[1, 0]) + abs(m[1, 2]))
        l33 = (abs(m[2, 0]) + abs(m[2, 1]))
        c11 = (abs(m[1, 0]) + abs(m[2, 0]))
        c22 = (abs(m[0, 1]) + abs(m[2, 1]))
        c33 = (abs(m[0, 2]) + abs(m[1, 2]))
        verify = False
        if abs(c11) <= abs(m[0, 0]) and abs(c22) <= abs(m[1, 1]) and abs(c33) <= abs(m[2, 2]):
            verify = True
        elif abs(l11) <= abs(m[0, 0]) and abs(l22) <= abs(m[1, 1]) and abs(l33) <= abs(m[2, 2]):
            verify = True
        else:
            print(f'{bold}{white}Sistema {red2}Inválido!!!')
            print(f'{red2}Critérios de convergência não atendindos!{res}')
        while verify:
            loading()
            kinicial = input(f'{bold}{white}Valores iniciais de x1, x2 e x3 no '
                             f'formato {orange7}({white}x1 x2 x3{orange7}){white}: {res}').split()
            if len(kinicial) == 3:
                x0, y0, z0 = [float(values) for values in kinicial]
                erro = float(input(f'{bold}{white}Erro Permitido: {res}'))
                k = 1
                while verify:
                    x = (m[0, 3] - (m[0, 2] * z0) - (m[0, 1] * y0)) / m[0, 0]
                    y = (m[1, 3] - (m[1, 2] * z0) - (m[1, 0] * x)) / m[1, 1]
                    z = (m[2, 3] - (m[2, 1] * y) - (m[2, 0] * x)) / m[2, 2]
                    loading()
                    print(f'{bold}{orange7}Interação: {white}{k}{res}')
                    print(f'{bold}{white}[{orange7}x1{white}: {x:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x2{white}: {y:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x3{white}: {z:.4f}]', end='\n')
                    ex = (abs(x) - abs(x0))
                    ey = (abs(y) - abs(y0))
                    ez = (abs(z) - abs(z0))
                    print(f'{bold}{white}[{orange7}|x1({k}) - x1({k - 1})| = {abs(ex):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x2({k}) - x2({k - 1})| = {abs(ey):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x3({k}) - x3({k - 1})| = {abs(ez):.8f}{white}]', end='\n')
                    if abs(ex) < erro and abs(ey) < erro and abs(ez) < erro:
                        verify = False
                    else:
                        x0 = x
                        y0 = y
                        z0 = z
                        k += 1
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devem estar no formato {orange7}({white}x1 x2 x3{orange7}){res}')
    if m.shape[0] == 4:
        l11 = (abs(m[0, 1]) + abs(m[0, 2]) + abs(m[0, 3]))
        l22 = (abs(m[1, 0]) + abs(m[1, 2]) + abs(m[1, 3]))
        l33 = (abs(m[2, 0]) + abs(m[2, 1]) + abs(m[2, 3]))
        l44 = (abs(m[3, 0]) + abs(m[3, 1]) + abs(m[3, 2]))
        c11 = (abs(m[1, 0]) + abs(m[2, 0]) + abs(m[3, 0]))
        c22 = (abs(m[0, 1]) + abs(m[2, 1]) + abs(m[3, 1]))
        c33 = (abs(m[0, 2]) + abs(m[1, 2]) + abs(m[3, 2]))
        c44 = (abs(m[0, 3]) + abs(m[1, 3]) + abs(m[2, 3]))
        verify = False
        if abs(c11) <= abs(m[0, 0]) and abs(c22) <= abs(m[1, 1]) and abs(c33) <= abs(m[2, 2]) and abs(c44) <= abs(
                m[3, 3]):
            verify = True
        elif abs(l11) <= abs(m[0, 0]) and abs(l22) <= abs(m[1, 1]) and abs(l33) <= abs(m[2, 2]) and abs(l44) <= abs(
                m[3, 3]):
            verify = True
        else:
            print(f'{bold}{white}Sistema {red2}Inválido!!!')
            print(f'{red2}Critérios de convergência não atendindos!{res}')
        while verify:
            kinicial = input(f'{bold}{white}Valores iniciais de x1, x2, x3 e x4 no '
                             f'formato {orange7}({white}x1 x2 x3 x4{orange7}){white}: {res}').split()
            if len(kinicial) == 4:
                x0, y0, z0, w0 = [float(values) for values in kinicial]
                erro = float(input(f'{bold}{white}Erro Permitido: {res}'))
                k = 1
                while verify:
                    x = (m[0, 4] - (m[0, 2] * z0) - (m[0, 1] * y0) - (m[0, 3] * w0)) / m[0, 0]
                    y = (m[1, 4] - (m[1, 2] * z0) - (m[1, 0] * x) - (m[1, 3] * w0)) / m[1, 1]
                    z = (m[2, 4] - (m[2, 1] * y) - (m[2, 0] * x) - (m[2, 3] * w0)) / m[2, 2]
                    w = (m[3, 4] - (m[3, 1] * y) - (m[3, 0] * x) - (m[3, 2] * z)) / m[3, 3]
                    loading()
                    print(f'{bold}{orange7}Interação: {white}{k}{res}')
                    print(f'{bold}{white}[{orange7}x1{white}: {x:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x2{white}: {y:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x3{white}: {z:.4f}]', end=' ')
                    print(f'{bold}{white}[{orange7}x4{white}: {w:.4f}]', end='\n')
                    ex = (abs(x) - abs(x0))
                    ey = (abs(y) - abs(y0))
                    ez = (abs(z) - abs(z0))
                    ew = (abs(w) - abs(w0))
                    print(f'{bold}{white}[{orange7}|x1({k}) - x1({k - 1})| = {abs(ex):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x2({k}) - x2({k - 1})| = {abs(ey):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x3({k}) - x3({k - 1})| = {abs(ez):.8f}{white}]', end='\n')
                    print(f'{bold}{white}[{orange7}|x4({k}) - x4({k - 1})| = {abs(ew):.8f}{white}]', end='\n')
                    if abs(ex) < erro and abs(ey) < erro and abs(ez) < erro and abs(ew) < erro:
                        verify = False
                    else:
                        x0 = x
                        y0 = y
                        z0 = z
                        w0 = w
                        k += 1
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devem estar no formato {orange7}({white}x1 x2 x3 x4{orange7}){res}')
#Solução do sistema pelo Método da Relaxação
def Relaxação():
    global b, x
    m = criar_matriz()
    erro = float(input(f'{bold}{white}Erro Permitido: {res}'))
    if m.shape[0] == 3:
        verify = True
        while verify:
            kinicial = input(f'{bold}{white}Valores iniciais de x1, x2 e x3 no '
                             f'formato {orange7}({white}x1 x2 x3{orange7}){white}: {res}').split()
            k = [float(values) for values in kinicial]
            if len(k) == 3:
                a = np.asarray(k)
                counter = 1
                while True:
                    r1 = ((m[0, 0] * a[0]) + (m[0, 1] * a[1]) + (m[0, 2] * a[2]) + m[0, 3])
                    r2 = ((m[1, 0] * a[0]) + (m[1, 1] * a[1]) + (m[1, 2] * a[2]) + m[1, 3])
                    r3 = ((m[2, 0] * a[0]) + (m[2, 1] * a[1]) + (m[2, 2] * a[2]) + m[2, 3])
                    if abs(r1) < erro and abs(r2) < erro and abs(r3) < erro:
                        loading()
                        print(f'{bold}{orange7}Interação Final{res}')
                        print(f'{bold}{white}[{orange7}r1{white}: {r1:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r2{white}: {r2:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r3{white}: {r3:.4f}]', end='\n')
                        break
                    else:
                        loading()
                        print(f'{bold}{orange7}Interação: {white}{counter}{res}')
                        print(f'{bold}{white}[{orange7}r1{white}: {r1:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r2{white}: {r2:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r3{white}: {r3:.4f}]', end='\n')
                        if abs(r1) > abs(r2) and abs(r1) > abs(r3):
                            x = np.argmax(abs(m[0, 0:3:1]))
                            if x == 0:
                                b = round((-((m[0, 1] * a[1]) + (m[0, 2] * a[2]) + m[0, 3]) / m[0, 0]), 4)
                            elif x == 1:
                                b = round((-((m[0, 0] * a[0]) + (m[0, 2] * a[2]) + m[0, 3]) / m[0, 1]), 4)
                            elif x == 2:
                                b = round((-((m[0, 0] * a[0]) + (m[0, 1] * a[1]) + m[0, 3]) / m[0, 2]), 4)
                            a[x] = b
                        elif abs(r2) > abs(r3) and abs(r2) > abs(r1):
                            x = np.argmax(abs(m[1, 0:3:1]))
                            if x == 0:
                                b = round((-((m[1, 1] * a[1]) + (m[1, 2] * a[2]) + m[1, 3]) / m[1, 0]), 4)
                            elif x == 1:
                                b = round((-((m[1, 0] * a[0]) + (m[1, 2] * a[2]) + m[1, 3]) / m[1, 1]), 4)
                            elif x == 2:
                                b = round((-((m[1, 0] * a[0]) + (m[1, 1] * a[1]) + m[1, 3]) / m[1, 2]), 4)
                            a[x] = b
                        elif abs(r3) > abs(r1) and abs(r3) > abs(r2):
                            x = np.argmax(abs(m[2, 0:3:1]))
                            if x == 0:
                                b = round((-((m[2, 1] * a[1]) + (m[2, 2] * a[2]) + m[2, 3]) / m[2, 0]), 4)
                            elif x == 1:
                                b = round((-((m[2, 0] * a[0]) + (m[2, 2] * a[2]) + m[2, 3]) / m[2, 1]), 4)
                            elif x == 2:
                                b = round((-((m[2, 0] * a[0]) + (m[2, 1] * a[1]) + m[2, 3]) / m[2, 2]), 4)
                            a[x] = b
                        if x == 0:
                            print(f'{bold}{white}[{orange7}x1{white}: {b:.4f}]{res}')
                        elif x == 1:
                            print(f'{bold}{white}[{orange7}x2{white}: {b:.4f}]{res}')
                        elif x == 2:
                            print(f'{bold}{white}[{orange7}x3{white}: {b:.4f}]{res}')
                        print(f'{bold}{white}[{orange7}x1{white}: {a[0]:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}x2{white}: {a[1]:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}x3{white}: {a[2]:.4f}]', end='\n')
                        counter += 1
                print(f'{bold}{white}[{orange7}x1{white}: {a[0]:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x2{white}: {a[1]:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x3{white}: {a[2]:.4f}]', end='\n')
                verify = False
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devemm estar no formato {orange7}({white}x1 x2 x3{orange7}){res}')
                loading()
    if m.shape[0] == 4:
        verify = True
        while verify:
            kinicial = input(f'{bold}{white}Valores iniciais de x1, x2, x3 e x4 no '
                             f'formato {orange7}({white}x1 x2 x3 x4{orange7}){white}: {res}').split()
            k = [float(values) for values in kinicial]
            if len(k) == 4:
                a = np.asarray(k)
                counter = 1
                while True:
                    r1 = ((m[0, 0] * a[0]) + (m[0, 1] * a[1]) + (m[0, 2] * a[2]) + (m[0,3]*a[3]) + m[0, 4])
                    r2 = ((m[1, 0] * a[0]) + (m[1, 1] * a[1]) + (m[1, 2] * a[2]) + (m[1,3]*a[3]) + m[1, 4])
                    r3 = ((m[2, 0] * a[0]) + (m[2, 1] * a[1]) + (m[2, 2] * a[2]) + (m[2,3]*a[3]) + m[2, 4])
                    r4 = ((m[3, 0] * a[0]) + (m[3, 1] * a[1]) + (m[3, 2] * a[2]) + (m[3,3]*a[3]) + m[3, 4])

                    if abs(r1) < erro and abs(r2) < erro and abs(r3) < erro and abs(r4) < erro:
                        loading()
                        print(f'{bold}{orange7}Interação Final{res}')
                        print(f'{bold}{white}[{orange7}r1{white}: {r1:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r2{white}: {r2:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r3{white}: {r3:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r4{white}: {r4:.4f}]', end='\n')
                        break
                    else:
                        loading()
                        print(f'{bold}{orange7}Interação: {white}{counter}{res}')
                        print(f'{bold}{white}[{orange7}r1{white}: {r1:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r2{white}: {r2:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r3{white}: {r3:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}r4{white}: {r4:.4f}]', end='\n')
                        if abs(r1) > abs(r2) and abs(r1) > abs(r3) and abs(r1) > abs(r4):
                            x = np.argmax(abs(m[0, 0:4:1]))
                            if x == 0:
                                b = round((-((m[0, 1] * a[1]) + (m[0, 2] * a[2]) + (m[0,3]*a[3] )+ m[0, 4]) / m[0, 0]), 4)
                            elif x == 1:
                                b = round((-((m[0, 0] * a[0]) + (m[0, 2] * a[2])+ (m[0,3]*a[3] ) + m[0, 4]) / m[0, 1]), 4)
                            elif x == 2:
                                b = round((-((m[0, 0] * a[0]) + (m[0, 1] * a[1])+ (m[0,3]*a[3] ) + m[0, 4]) / m[0, 2]), 4)
                            elif x == 3:
                                b = round((-((m[0, 0] * a[0]) + (m[0, 1] * a[1]) + (m[0, 2] * a[2]) + m[0, 4]) / m[0, 3]), 4)
                            a[x] = b
                        elif abs(r2) > abs(r3) and abs(r2) > abs(r1) and abs(r2) > abs(r4):
                            x = np.argmax(abs(m[1, 0:4:1]))
                            if x == 0:
                                b = round(
                                    (-((m[1, 1] * a[1]) + (m[1, 2] * a[2]) + (m[1, 3] * a[3]) + m[1, 4]) / m[1, 0]), 4)
                            elif x == 1:
                                b = round(
                                    (-((m[1, 0] * a[0]) + (m[1, 2] * a[2]) + (m[1, 3] * a[3]) + m[1, 4]) / m[1, 1]), 4)
                            elif x == 2:
                                b = round(
                                    (-((m[1, 0] * a[0]) + (m[1, 1] * a[1]) + (m[1, 3] * a[3]) + m[1, 4]) / m[1, 2]), 4)
                            elif x == 3:
                                b = round(
                                    (-((m[1, 0] * a[0]) + (m[1, 1] * a[1]) + (m[1, 2] * a[2]) + m[1, 4]) / m[1, 3]), 4)
                            a[x] = b
                        elif abs(r3) > abs(r1) and abs(r3) > abs(r2) and abs(r3) > abs(r4):
                            x = np.argmax(abs(m[2, 0:4:1]))
                            if x == 0:
                                b = round(
                                    (-((m[2, 1] * a[1]) + (m[2, 2] * a[2]) + (m[2, 3] * a[3]) + m[2, 4]) / m[2, 0]), 4)
                            elif x == 1:
                                b = round(
                                    (-((m[2, 0] * a[0]) + (m[2, 2] * a[2]) + (m[2, 3] * a[3]) + m[2, 4]) / m[2, 1]), 4)
                            elif x == 2:
                                b = round(
                                    (-((m[2, 0] * a[0]) + (m[2, 1] * a[1]) + (m[2, 3] * a[3]) + m[2, 4]) / m[2, 2]), 4)
                            elif x == 3:
                                b = round(
                                    (-((m[2, 0] * a[0]) + (m[2, 1] * a[1]) + (m[2, 2] * a[2]) + m[2, 4]) / m[2, 3]), 4)
                            a[x] = b
                        elif abs(r4) > abs(r1) and abs(r4) > abs(r2) and abs(r4) > abs(r3):
                            x = np.argmax(abs(m[3, 0:4:1]))
                            if x == 0:
                                b = round(
                                    (-((m[3, 1] * a[1]) + (m[3, 2] * a[2]) + (m[3, 3] * a[3]) + m[3, 4]) / m[3, 0]), 4)
                            elif x == 1:
                                b = round(
                                    (-((m[3, 0] * a[0]) + (m[3, 2] * a[2]) + (m[3, 3] * a[3]) + m[3, 4]) / m[3, 1]), 4)
                            elif x == 2:
                                b = round(
                                    (-((m[3, 0] * a[0]) + (m[3, 1] * a[1]) + (m[3, 3] * a[3]) + m[3, 4]) / m[3, 2]), 4)
                            elif x == 3:
                                b = round(
                                    (-((m[3, 0] * a[0]) + (m[3, 1] * a[1]) + (m[3, 2] * a[2]) + m[3, 4]) / m[3, 3]), 4)
                            a[x] = b
                        if x == 0:
                            print(f'{bold}{white}[{orange7}x1{white}: {b:.4f}]{res}')
                        elif x == 1:
                            print(f'{bold}{white}[{orange7}x2{white}: {b:.4f}]{res}')
                        elif x == 2:
                            print(f'{bold}{white}[{orange7}x3{white}: {b:.4f}]{res}')
                        elif x == 3:
                            print(f'{bold}{white}[{orange7}x4{white}: {b:.4f}]{res}')
                        print(f'{bold}{white}[{orange7}x1{white}: {a[0]:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}x2{white}: {a[1]:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}x3{white}: {a[2]:.4f}]', end=' ')
                        print(f'{bold}{white}[{orange7}x4{white}: {a[3]:.4f}]', end='\n')
                        counter += 1
                print(f'{bold}{white}[{orange7}x1{white}: {a[0]:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x2{white}: {a[1]:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x3{white}: {a[2]:.4f}]', end=' ')
                print(f'{bold}{white}[{orange7}x4{white}: {a[3]:.4f}]', end='\n')
                verify = False
            else:
                loading()
                print(f'{red2}{bold}Entrada Inválida!!!')
                print(f'Valores de y devemm estar no formato {orange7}({white}x1 x2 x3 x4{orange7}){res}')
                loading()
#Cria cópias de funções com o parâmetro definido
def criar_vetor_copy(x):
    vetor = np.zeros((1,x))
    i = 0
    while i < 1:
        x = input(f'{white}{bold}Elementos do vetor: {res}').split()
        if len(x) == vetor.size:
            for i in range(0,2):
                vetor[0,0:vetor.size:1] = x
            i += 1
            realvetor = vetor.flatten()
            return realvetor
            break
        else:
            print(f'{red}{bold}Entrada Inválida!!!')
            print(f'Números de elementos entrado não compátivel com o tamanho do {white}vetor')
            print(f'Valor Entrado {white}{len(x)} {red2}Tamanho do {white}vetor {white}{vetor.size}{res}')
def produto_escalar_copy(x, y):
    while True:
        multvetor = x * y
        result = sum(multvetor)
        return result
        break
def determinante_copy(x):
    a = np.linalg.det(x)
    return a
def matriz_inversa_copy(x):
    b = determinante_copy(x)
    if b != 0:
        result = np.linalg.inv(x)
        return result
    else:
        print(f'{red}{bold}Matriz inválida!!!')
        print(f'Matriz não admite inversa{res}')
def Gauss_Elimination_copy(m):
    np.set_printoptions(suppress=True)
    if m.shape[0] == 3:
        np.set_printoptions(suppress=True)
        j = 0
        k = 1
        for i in range(0,2):
            if j == 0:
                m = add(m, - m[k, j] / m[j, j], k, j)
                k += 1
            if k > 2:
                j += 1
            if j == 1:
                k = 2
                m = add(m, - m[k, j] / m[j, j], k, j)
                j += 1
    if m.shape[0] == 4:
        np.set_printoptions(suppress=True)
        j = 0
        k = 1
        for i in range(0, 3):
            m = add(m, - m[k, j] / m[j, j], k, j)
            k += 1
            if k > 3:
                j += 1
            if j == 1:
                k = 2
                for x in range(0, 2):
                    m = add(m, - m[k, j] / m[j, j], k, j)
                    k += 1
                j += 1
            if j == 2:
                k = 3
                m = add(m, - m[k, j] / m[j, j], k, j)
    if m.shape[0] == 3:
        x1, x2, x3 = solucao3(m)
        return x1, x2, x3
    if m.shape[0] == 4:
        x1, x2, x3, x4 = solucao4(m)
        return x1, x2, x3, x4

#Interpolação
def Interpolação_Linear():
    while True:
        loading()
        npontos = input(f'{white}{bold}Pontos de x: {res}').split()
        pontos = [float(values) for values in npontos]
        n = len(pontos)
        tind = input(f'{white}{bold}Pontos de f(x): {res}').split()
        ind = [float(value) for value in tind]
        if len(pontos) == len(ind):
            coeficientes1 = []
            coeficientes2 = []
            for i in range(0,n):
                for j in range(0,n):
                    eq = pontos[i]**j
                    coeficientes1.append(eq)
                coeficientes2.append(coeficientes1)
                coeficientes1 = []
            coeficientes = np.asarray(coeficientes2)
            ti1 = np.asarray(ind)
            a = np.linalg.solve(coeficientes, ti1)
            ponto = float(input(f'{white}{bold}Calcular f(x) no ponto: {res}'))
            eq1 = 0
            for i in range(0,n):
                eq2 = eq1 + a[i]*(ponto**i)
                eq1 = eq2
            for i in range(0,n):
                print(f'{bold}{white}[{orange7}a{i}{white}: {a[i]:.4f}]', end=' ')
            print(end='\n')
            print(f'{bold}{white}[{orange7}f(x){white}= {eq2:.4f}]', end='\n')
            break
        else:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'Número de pontos x diferente do número de pontos de y{res}')
            print(f'{bold}{white}[{orange7}Número de pontos de x{white}: {len(pontos)}]', end=' ')
            print(f'{bold}{white}[{orange7}Número de pontos f(x){white}: {len(ind)}]', end='\n')
def Interpolação_Quadratica():
    while True:
        loading()
        npontos = input(f'{white}{bold}Pontos de x: {res}').split()
        pontos = [float(values) for values in npontos]
        n = len(pontos)
        tind = input(f'{white}{bold}Pontos de f(x): {res}').split()
        ind = [float(value) for value in tind]
        if len(pontos) == len(ind):
            coeficientes1 = []
            coeficientes2 = []
            for i in range(0, n):
                for j in range(0, n):
                    eq = pontos[i] ** j
                    coeficientes1.append(eq)
                coeficientes2.append(coeficientes1)
                coeficientes1 = []
            coeficientes = np.asarray(coeficientes2)
            ti1 = np.asarray(ind)
            ti = ti1.reshape(n, 1)
            matriz = np.hstack((coeficientes, ti))
            a = Gauss_Elimination_copy(matriz)
            ponto = float(input(f'{white}{bold}Calcular f(x) no ponto: {res}'))
            eq1 = 0
            x = 0
            for i in range(0, n):
                eq2 = eq1 + a[x] * (ponto ** i)
                eq1 = eq2
                x += 1
            for i in range(0, n):
                print(f'{bold}{white}[{orange7}a{i}{white}: {a[i]:.4f}]', end=' ')
            print(end='\n')
            print(f'{bold}{white}[{orange7}f(x){white}= {eq2:.4f}]', end='\n')
            break
        else:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'Número de pontos x diferente do número de pontos de y{res}')
            print(f'{bold}{white}[{orange7}Número de pontos de x{white}: {len(pontos)}]', end=' ')
            print(f'{bold}{white}[{orange7}Número de pontos f(x){white}: {len(ind)}]', end='\n')

def Interpolação_Lagrange():
    while True:
        loading()
        npontos = input(f'{white}{bold}Pontos de x: {res}').split()
        pontos = [float(values) for values in npontos]
        n = len(pontos)
        tind = input(f'{white}{bold}Pontos de f(x): {res}').split()
        ind = [float(value) for value in tind]
        if len(ind) == len(pontos):
            ponto = float(input(f'{white}{bold}Calcular f(x) no ponto: {res}'))
            eq = 1
            u = 1
            l1 = []
            for i in range(0, n):
                for j in range(0, n - 1):
                    if i == j:
                        lu = eq * (ponto - pontos[j + 1]) / (pontos[i] - pontos[j + 1])
                        eq = lu
                        u = 1
                    else:
                        lu = eq * (ponto - pontos[j + u]) / (pontos[i] - pontos[j + u])
                        eq = lu
                print(f'{bold}{white}[{orange7}L{i}{white}: {lu:.4f}]', end=' ')
                l1.append(lu)
                u = 0
                eq = 1
            l = np.asarray(l1)
            z = []
            for i in range(0, n):
                x = ind[i] * l[i]
                z.append(x)
            z1 = np.asarray(z)
            y = np.sum(z1)
            print(end='\n')
            print(f'{bold}{white}[{orange7}f(x){white}= {y:.4f}]', end='\n')
            break
        else:
            loading()
            print(f'{red2}{bold}Entrada Inválida!!!')
            print(f'Número de pontos x diferente do número de pontos de y{res}')
            print(f'{bold}{white}[{orange7}Número de pontos de x{white}: {len(pontos)}]', end=' ')
            print(f'{bold}{white}[{orange7}Número de pontos f(x){white}: {len(ind)}]', end='\n')
#sla
def matmult():
    while True:
        a = criar_matriz()
        loading()
        b = criar_matriz()
        if a.shape[1] == b.shape[0]:
            c = np.matmul(a,b)
            return c
            break
        else:
            loading()
            print(f'{bold}{red2}Número de {white}Linhas {red2}da matriz {white}A {red2}é diferente do número de {white}colunas {red2}da matriz '
                  f'{white}B{res}')
            print(f'{bold}{white}Matriz A: {a.shape} | Matriz B: {b.shape}{res}')
            loading()

#Regressão Linear
def mmq():
    while True:
        x1 = input(f'{white}{bold}Valores de X: {res}').split()
        x_value = [float(value) for value in x1]
        y1 = input(f'{white}{bold}Valores de Y: {res}').split()
        y_value = [float(values) for values in y1]
        x = np.array(x_value)
        y = np.array(y_value)
        if len(x) == len(y):
            x_med = np.sum(x)
            x_med = x_med / (len(x))
            y_med = np.sum(y)
            y_med = y_med / (len(y))
            dx_list = []
            dy_list = []
            for i in range(len(x)):
                n = x[i] - x_med
                dx_list.append(n)
            for j in range(len(x)):
                m = y[j] - y_med
                dy_list.append(m)
            dx = np.array(dx_list)
            dy = np.array(dy_list)
            dx_dy = dx * dy
            sum_dxdy = np.sum(dx_dy)
            x_sqr_list = []
            for k in range(len(dx)):
                r = dx[k] * dx[k]
                x_sqr_list.append(r)
            x_sqr = np.array(x_sqr_list)
            sum_x_sqr = np.sum(x_sqr)
            coeficiente = sum_dxdy / sum_x_sqr
            intercep = y_med - (coeficiente * x_med)
            loading()
            print(f'{bold}{green5}Coef. Angular: {white}{coeficiente:.6f} {blue3}Coef. Linear: {white}{intercep:.6f}{res}')
            break

        elif len(x) < len(y):
            loading()
            print(f'{bold}{red2}Quantidade de {white}pontos {red2}não compatível {white}x {red2}< {white}y')
            print(f'{orange7}x:{white}{orange}[ {white}{len(x)}{orange} ] {orange7}y:{orange}[ {white}{len(y)}{orange} ]{res}')
            loading()
        elif len(x) > len(y):
            loading()
            print(f'{bold}{red2}Quantidade de {white}pontos {red2}não compatível {white}y {red2}< {white}x')
            print(f'{orange7}x:{white}{orange}[ {white}{len(x)}{orange} ] {orange7}y:{orange}[ {white}{len(y)}{orange} ]{res}')
            loading()

#0 de funções
#Bhaskara
def raiz_grau2():
    while True:
        coef = input(f'{bold}{white}Coeficientes na forma {orange7}({white}a b c{orange7}){white}: {res}').split()
        x_list = [float(values) for values in coef]
        x = np.array(x_list)
        if len(x) == 3:
            delta = (x[1] * x[1]) - (4 * x[0] * x[2])
            if delta > 0:
                delta = delta ** 0.5
                x1 = (-x[1] + delta) / (2 * x[0])
                x2 = (-x[1] - delta) / (2 * x[0])
                loading()
                print(f'{bold}{orange7}x₁{orange}[{white}{x1:.6f}{orange}] {orange7}x₂{orange}[{white}{x2:.6f}{orange}]{res}')
                break
            elif delta == 0:
                x1 = (-x[1]) / (2 * x[0])
                loading()
                print(f'{bold}{orange7}x₁{orange}[{white}{x1:.6f}{orange}]{res}')
                break
            else:
                loading()
                print(f'{bold}{red2}Não possui raiz {white}Real{res}')
                break
        else:
            print(f'{bold}{red2}Entrada Inválida!{res}')

#loading
def loading():
    for i in range(8):
        print(f'{bold}{gray}-=-', end='', flush=True)
        sleep(0.03)
        print(f'{bold}{gray}=-', end='', flush=True)
    print(f'{res}', end='\n')

#Title
title = lambda text: print(f'{bold}{sub}{text}{res}')

#Tecla
tecla = lambda funçao, text: print(f'{bold}{moss1}{funçao} {orange7}[{white} {text} {orange7}]{res}')

#seletor inter
def interpolação():
    while True:
        sleep(0.3)
        loading()
        tecla('Interpolação Linear', 'L')
        tecla('Interpolação Quadratica', 'Q')
        tecla('Interpolação Lagrange', 'G')
        x = input(f'{bold}{white}Operação: {res}').lower().replace(' ', '')
        if x == 'l':
            loading()
            title('Interpolação Linear')
            Interpolação_Linear()
            break
        if x == 'q':
            loading()
            title('Interpolação Quadratica')
            Interpolação_Quadratica()
            break
        if x == 'g':
            loading()
            title('Interpolação Lagrange')
            Interpolação_Lagrange()
            break
#Seletor
def seletor():
    while True:
        sleep(0.3)
        tecla('Produto Vetorial', 'V')
        tecla('Produto Escalar', 'E')
        tecla('Produto Misto', 'M')
        tecla('Sistemas Lineares', 'X')
        tecla('Multiplicação de Matriz', 'Z')
        tecla('Determinante', 'D')
        tecla('Matriz Inversa', 'W')
        tecla('Regressão Linear - MMQ', 'R')
        tecla('Equação 2° Grau', '2')
        tecla('Gauss-Jordan', 'G')
        tecla('Eliminação de Gauss', 'H')
        tecla('Eliminação de Gauss (c/ Troca de Linha)', 'T')
        tecla('Fatoração LU', 'L')
        tecla('Gauss-Jacobi', 'J')
        tecla('Gauss-Seidel', 'S')
        tecla('Método da Relaxação', 'O')
        tecla('Interpolação', 'I')
        tecla('Sair', 'Q')

        x = input(f'{bold}{white}Operação: {res}').lower().replace(' ', '')
        if x == 'v' or x == 'produtovetorial' or x == 'vetorial':
            loading()
            title('Produto Vetorial')
            loading()
            a = produto_vetorial()
            loading()
            print(f'{bold}{green5}Vetor AxB{white}: {res}', end=' ')
            print(f'{bold}{orange}[{white}{a[0]:.6f}{orange}]{orange7}x{white}', end=' ')
            print(f'{bold}{orange}[{white}{a[1]:.6f}{orange}]{orange7}y{white}', end=' ')
            print(f'{bold}{orange}[{white}{a[2]:.6f}{orange}]{orange7}z{white}', end='\n')
            loading()
        elif x == 'e' or x == 'produtoescalar' or x == 'escalar':
            loading()
            title('Produto Escalar')
            loading()
            b = produto_escalar()
            loading()
            print(f'{white}{bold}{green5}Resultado{white}: {b:.6f}{res}')
            loading()
        elif x == 'm' or x == 'produtomisto' or x == 'misto':
            loading()
            title('Produto Misto')
            loading()
            c = produto_misto()
            loading()
            print(f'{bold}{green5}Resultado{white}: {c:.6f}{res}')
            loading()
        elif x == 'x' or x == 'sistemas' or x == 'sistemalinear' or x == 'sistema' or x == 'sistemaslinear' or x == 'sistemaslineares':
            loading()
            title('Sistemas Lineares')
            loading()
            d = soluçao_do_sistema()
            loading()
            if len(d) == 0:
                print(f'{red2}{bold}Sistema {white}Impossível {red2}ou {white}Possível e Indeterminado{res}')
                loading()
            else:
                for index1 in range(len(d)):
                    print(f'{white}{bold}{orange7}Variável {index1 + 1}:{orange}[{white}'
                          f'{d[index1]:.6f}{orange}]{res}', end=f'  ')
                print(end='\n')
                loading()
        elif x == 'd' or x == 'determinante' or x == 'det':
            loading()
            title('Determinante')
            loading()
            e = determinante()
            loading()
            print(f'{white}{bold}{green5}DeterminanteΔ{white}: {e:.0f}{res}')
            loading()
        elif x == 'w' or x == 'matrizinversa' or x == 'inversa':
            loading()
            title('Matriz Inversa')
            loading()
            f = matriz_inversa()
            loading()
            print(f'{white}{bold}{green5}Matriz{white}: {f}{res}')
            loading()
        elif x == 'r' or x == 'mmq':
            loading()
            title('Regressão Linear - MMQ')
            loading()
            mmq()
            loading()
        elif x == '2' or x == 'segundograu' or x == 'raiz':
            loading()
            title('Equação 2° Grau')
            loading()
            raiz_grau2()
            loading()
        elif x == 'z' or x == 'mm' or x == 'matmult' or x == 'matmul':
            loading()
            title('Multiplicação de Matriz')
            loading()
            g = matmult()
            print(f'{bold}{white}{g}{res}')
            loading()
        elif x == 'g' or x == 'gauss-jordan' or x == 'gaussjordan' or x == 'gj':
            loading()
            title('Gauss-Jordan')
            loading()
            Gauss()
            loading()
        elif x == 'h' or x == 'eg'  or x == 'gauss' or x == 'eliminaçãodegauss' or x == 'eliminacaodegauss':
            loading()
            title('Eliminação de Gauss')
            loading()
            Gauss_Elimination()
            loading()
        elif x == 't' or x == 'gausslinha' or x == 'gauss 2':
            loading()
            title('Eliminação de Gauss (c/ Troca de Linha)')
            loading()
            Gauss_Elimination_L()
            loading()
        elif x == 'l' or x == 'lu' or x == 'fatoraçaolu' or x == 'fatoraçãolu':
            loading()
            title('Fatoração LU')
            loading()
            Fatoracao_LU()
            loading()
        elif x == 'j' or x == 'jacobi' or x =='gauss-jacobi' or x == 'gaussjacobi' or x == 'jacas' \
                or x== 'xanosk' or x == 'gaussxanosk' or x == 'gauss-xanosk' or x == 'schanoski':
            loading()
            title('Gauss-Jacobi')
            loading()
            Gauss_Xanosk()
            loading()
        elif x =='s' or x == 'seidel' or x == 'gauss-seidel' or x == 'gaussseidel':
            loading()
            title('Gauss-Seidel')
            loading()
            Gauss_Seidel()
            loading()
        elif x == 'o' or x == 'relaxaçao' or x == 'relaxacao' or x == 'relaxação' or x == 'relaxacão':
            loading()
            title('Método da Relaxação')
            loading()
            Relaxação()
            loading()
        elif x == 'i' or x == 'inter' or x == 'interpolaçao' or x == 'interpolação':
            interpolação()
            loading()

        elif x == 'q':
            break
        else:
            loading()
            print(f'{bold}{red2}Entrada Inválida!{res}')
            loading()

if __name__ == '__main__':
    seletor()
