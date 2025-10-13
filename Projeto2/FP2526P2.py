#ist1117729

ABECEDARIO = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O',
                  'P','Q','R','S','T','U','V','X','Z')

NUM_LETRAS_JOGADOR = 7
NUM_MAX_JOGADORES = 4
NUM_MIN_JOGADORES = 2
TAMANHO_DO_TABULEIRO = 15

def cria_casa(lin, col):
        if (not type(lin) == int or not type(col) == int 
            or not 1 <= lin <= TAMANHO_DO_TABULEIRO 
            or not 1 <= col <= TAMANHO_DO_TABULEIRO):
            raise ValueError(f"cria_casa: argumentos inválidos")

        return (lin, col)
    
def obtem_col(casa):
        return casa[1]
    
def obtem_lin(casa):
        return casa[0]
    
def eh_casa(arg):
        lin, col = arg
        return (type(lin) == int and type(col) == int 
        and 1 <= lin <= TAMANHO_DO_TABULEIRO 
        and 1 <= col <= TAMANHO_DO_TABULEIRO)

def casas_iguais(c1, c2):
        return c1[0] == c2[0] and c1[1] == c2[2]
    
def casa_para_str(c):
        return '(' + str(c[0]) + ',' + str(c[1]) + ')'
    
def str_para_casa(s):
        s = s.strip('()')
        lin, col = map(int, s.split(','))
        return (lin,col)

def incrementa_casa(c, d, s):
        inc_lin = 0
        inc_col = 0

        if d == 'H':
            inc_col = s
        elif d == 'V':
            inc_lin = s
        else:
               return c

        nova_linha = c[0] + inc_lin
        nova_col = c[1] + inc_col
        
        if (not 1 <= nova_linha <= TAMANHO_DO_TABULEIRO 
        or not 1 <= nova_col <= TAMANHO_DO_TABULEIRO):
            return c    
        
        return cria_casa(nova_linha,nova_col)
