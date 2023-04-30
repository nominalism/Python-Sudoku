S = [['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*'],
     ['', '', '', '', '', '', '', '', '*']]

def exibeSudoku():
    print('  a b c  d e f  g h i')
    for linha in range(9):
        print(chr(ord('A') + linha) + ' ', end='')
        for coluna in range(9):
            print(S[linha][coluna] + ' ', end='')
            if (coluna + 1) % 3 == 0:
                print(' ', end='')
        print()
        if (linha + 1) % 3 == 0:
            print()    

def levalor():
    l, c, valor = input("Linha, Coluna, Valor: ").split()
    linha = ord(l) - ord('A')
    coluna = ord(c) - ord('a')
    if 0 <= linha <= 8:
        if 0 <= coluna <= 8:
            if valor == '*' or \
                (ord('1') <= ord(valor) <= ord('9')):
                return True, linha, coluna
            else:
                print('Valor inválido.')
                return False, 0, 0, ''
        else:
            print('Coluna inválida.')
            return False, 0, 0, ''
    else:
        print('Linha Inválida.')
        return False, 0, 0, ''

def verificaLinha(S, l, c, v):
    for i in range(9):
        if i != c and S[l][i] == v:
            return False
    return True

def verificaQuadrante(S, l, c, v):
    l_quad = int(l / 3) * 3
    c_quad = int(c / 3) * 3
    for i in range(l_quad, l_quad + 3): #l_quad <= i <
            for j in range(c_quad, c_quad + 3):
                if (i != l or j != c) and\
                S[i][j] == v:
                    return False

def lerInstanciaSudoku():
    print(' Instância Sudoku: ')
    print('  a b c d e f g h i ')
    for i in range(9):
        mensagem = chr(ord('A') + i )
        linha = input(mensagem + ' ').split()
        for k in range(9):
            S[i][k] = linha[k]
    print()

lerInstanciaSudoku()
exibeSudoku()
leituraValida = False
while not leituraValida:
    leituraValida, linha, coluna, valor = levalor()
    if leituraValida:
        if verificaLinha(S, linha, coluna, valor) and\
            verificaQuadrante(S, linha, coluna, valor):
            S[linha][coluna] = valor
exibeSudoku()