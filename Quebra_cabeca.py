def No(tab_original):
   
    movimentos = []
    tab = eval(tab_original)
    i = 0
    j = 0
    while 0 not in tab[i]: i += 1
    j = tab[i].index(0)
    

    if i<2:        
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i>0:         
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j<2:         
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    
    if j>0:         
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movimentos

def bfs(Inicio,end):
  
    Cabeca = []
    W = [[Inicio]]
    while W:
        i = 0
        caminho = W[i]
        W = W[:i] + W[i+1:]
        final = caminho[-1]
        if final in Cabeca: 
            continue
        for movimento in No(final):
            if movimento in Cabeca:
                continue
            W.append(caminho + [movimento])
        Cabeca.append(final)
        if final == end: break
    return caminho

def h_Heuristico(tabuleiro):
    
    Heuristico = 0
    comparador = 1
    tab = eval(tabuleiro)
    for i in range(0,3):
        for j in range(0,3):
            if tab[i][j] != comparador:
                Heuristico += 1
            comparador += 1
    return Heuristico

def a_Solucao(start,end):
    
    Cabeca = []
    W = [[h_Heuristico(start),start]]
    while W:
        i = 0
        for j in range(1,len(W)):
            if (W[i][0]) > (W[j][0]):
               i = j
        caminho = W[i]
        W = W[:i] + W[i+1:]
        final = caminho[-1]
        if final in Cabeca: continue
        for movimento in No(final):
            if movimento in Cabeca: continue
            novo = [caminho[0] + h_Heuristico(movimento) + h_Heuristico(final)] + caminho[1:] + [movimento] 
            W.append(novo)
        Cabeca.append(final)
        if final == end: break
    return caminho


tabuleiro = str([
                [4,3,6],
                [8,7,1],
                [0,5,2]
            ])

obj_final = str([
                [1,2,3],
                [4,5,6],
                [7,8,0]
            ])

print("Usando Busca em Largura:")
for i in bfs(tabuleiro,obj_final):
    print(i, end="\n")

print("Usando A*:")
for i in a_Solucao(tabuleiro,obj_final):
    print(i, end=" ")



