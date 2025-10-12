#ist1117729

ABECEDARIO = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O',
                  'P','Q','R','S','T','U','V','X','Z')

NUM_LETRAS_JOGADOR = 7
NUM_MAX_JOGADORES = 4
NUM_MIN_JOGADORES = 2
TAMANHO_DO_TABULEIRO = 15



class casa:
    def cria_casa(lin, col):
        if (not type(lin) == int or not type(col) == int 
            or not 1 <= lin <= TAMANHO_DO_TABULEIRO 
            or not 1 <= col <= TAMANHO_DO_TABULEIRO):
            raise ValueError(f"cria_casa: argumentos inválidos")
    
        return (lin, col)
    
    def obtem_col(casa):
        lin, col = casa
        return col
    
    def obtem_lin(casa):
        lin, col = casa
        return lin
    
    def eh_casa(arg):
        lin, col = arg
        return (type(lin) == int and type(col) == int 
        and 1 <= lin <= TAMANHO_DO_TABULEIRO 
        and 1 <= col <= TAMANHO_DO_TABULEIRO)

    def casas_iguais(c1, c2):
        lin1, col1 = c1
        lin2, col2 = c2

        return lin1 == lin2 and col1 == col2
    
    def casa_para_str(c):
        return str(c)
    
    def str_para_casa(s):
        s = s.strip('()')
        lin, col = map(int, s.split(','))
        return (lin, col)

    def incrementa_casa(c, d, s):
        lin, col = c

        
        inc_lin = 0
        inc_col = 0

        if d == 'H':
            inc_col = s
        if d == 'V':
            inc_lin = s

        nova_linha = lin + inc_lin
        nova_col = col + inc_col
        
        if (not 1 <= nova_linha <= TAMANHO_DO_TABULEIRO 
        or not 1 <= nova_col <= TAMANHO_DO_TABULEIRO):
            return c    
        
        return casa.cria_casa(nova_linha, nova_col)
    
