#ist1117729

ABECEDARIO = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O',
                  'P','Q','R','S','T','U','V','X','Z')

pontos = {  'A':1, 'B': 3,'C': 2,'Ç':3, 'D':2, 'E':1,
            'F':4, 'G': 4,'H': 4,'I': 1,'J': 5,'L': 2,
            'M':1, 'N': 3,'O': 1,'P': 2,'Q': 6,'R': 1,
            'S':1, 'T': 1,'U': 1,'V': 4,'X': 8,'Z': 8
            }

NUM_LETRAS_JOGADOR = 7
NUM_MAX_JOGADORES = 4
NUM_MIN_JOGADORES = 2
TAMANHO_DO_TABULEIRO = 15

# Construtores
def cria_casa(lin, col):
    if (not type(lin) == int or not type(col) == int 
        or not 1 <= lin <= TAMANHO_DO_TABULEIRO 
        or not 1 <= col <= TAMANHO_DO_TABULEIRO):
        raise ValueError(f"cria_casa: argumentos inválidos")

    return (lin, col)

# Seletores  
def obtem_col(casa):
    return casa[1]
    
def obtem_lin(casa):
    return casa[0]

# Reconhecedor  
def eh_casa(arg):
    lin, col = arg
    return (type(lin) == int and type(col) == int 
    and 1 <= lin <= TAMANHO_DO_TABULEIRO 
    and 1 <= col <= TAMANHO_DO_TABULEIRO)

# Teste
def casas_iguais(c1, c2):
    return (obtem_lin(c1) == obtem_lin(c2) 
            and obtem_col(c1) == obtem_col(c2))

# Transformador
def casa_para_str(c):
    return '(' + str(obtem_lin(c)) + ',' + str(obtem_col(c)) + ')'
    
def str_para_casa(s):
    s = s.strip('()')
    lin, col = map(int, s.split(','))
    return cria_casa(lin, col)

# Alto nível
def incrementa_casa(c, d, s):
    inc_lin = 0
    inc_col = 0

    if d == 'H':
        inc_col = s
    elif d == 'V':
        inc_lin = s
    else:
        return c

    nova_linha = obtem_lin(c) + inc_lin
    nova_col = obtem_col(c) + inc_col
        
    if (not 1 <= nova_linha <= TAMANHO_DO_TABULEIRO 
        or not 1 <= nova_col <= TAMANHO_DO_TABULEIRO):
            return c    
        
    return cria_casa(nova_linha, nova_col)

# Construtores
def cria_humano(nome):
    if nome == "":
        raise ValueError("cria_humano: argumento inválido")
    return {'nome': nome, 'pontos': 0, 'letras':{}}

def cria_agente(nivel):
    if nivel not in ('FACIL' or 'MEDIO' or 'DIFICIL'):
        raise ValueError("cria_agente: argumento inválido")
    return {'nivel': nivel, 'pontos': 0, 'letras':{}}

# Seletores
def jogador_identidade(j):
    if 'nome' in j:
        return j['nome']
    else:
        return  j['nivel']
    
def jogador_pontos(j):
    return j['pontos']

def jogador_letras(j):
    lista_letras = []
    res = ''
    for letra, occ in j['letras'].items():
        lista_letras.extend(letra * occ)
    
    lista_letras = sorted(lista_letras, key = lambda x: ABECEDARIO.index(x))
    
    for i in range(len(lista_letras)):
        res += ' ' + lista_letras[i]
    
    return res

# Modificadores
def recebe_letra(j, l):
    if l in j['letras']:
        j['letras'][l] += 1
    else:
        j['letras'][l] = 1
    return j

def usa_letra(j, l):
    if l in j['letras']:
        j['letras'][l] -= 1
        if j['letras'][l] <= 0:
            del j['letras'][l]
        return j
    else:
        return j
    
def soma_pontos(j, p):
    j['pontos'] += p
    return j

# Reconhecedor
def eh_jogador(arg):
    return ('nome' in arg or 'nivel' in arg)

def eh_humano(arg):
    return 'nome' in arg

def eh_agente(arg):
    return 'nivel' in arg

# Teste
def jogadores_iguais(j1, j2):
    return ((jogador_identidade(j1) == jogador_identidade(j2))
            and jogador_pontos(j1) == jogador_pontos(j2)
            and jogador_letras(j1) == jogador_letras(j2))

# Transformador
def jogador_para_str(j):
    
    # Formata a pontuação para ter sempre 3 espaços
    if jogador_pontos(j) < 10:
            pontos = "  " + str(jogador_pontos(j))
    elif jogador_pontos(j) < 100:
            pontos = " " + str(jogador_pontos(j))
    else:
            pontos = str(jogador_pontos(j))
    
    if 'nome' in j:
        prefixo = str(jogador_identidade(j)) + ' (' + pontos + '):'
    else:
        prefixo = 'BOT(' + str(jogador_identidade(j)) + ') (' + pontos + '):'
    
    return prefixo + jogador_letras(j)

# Alto-nível
def distribui_letras(jog, saco, num):
    if num <= len(saco):
        for _ in range(num):
            letra = saco.pop()
            recebe_letra(jog, letra)
    else:
        for _ in range(len(saco)):
            letra = saco.pop()
            recebe_letra(jog, letra)
    return jog

# Construtor
def cria_vocabulario(v):
    if not isinstance(v, tuple) and not len(v) >= 1:
        raise ValueError("cria_vocabulario: argumento inválido")
    for palavra in v:
        if not isinstance(palavra, str):
            raise ValueError("cria_vocabulario: argumento inválido")
        if not (2 <= len(palavra) <= TAMANHO_DO_TABULEIRO):
            raise ValueError("cria_vocabulario: argumento inválido")
        for i in range(len(palavra)):
            if palavra[i] not in ABECEDARIO:
                raise ValueError("cria_vocabulario: argumento inválido")
    return list(v)

# Seletores
def obtem_pontos(vocabulario, palavra):
    pontuacao = 0
    if palavra in vocabulario:
        for letra in palavra:
            pontuacao += pontos[letra]      # Soma o valor de pontos da letra
    return pontuacao

def obtem_palavras(vocabulario, comp, letra):
    res = []
    for palavra in vocabulario:
        if (len(palavra) == comp and palavra[0] == letra):
            res.append((palavra, obtem_pontos(vocabulario, palavra)),)
    
    res.sort(key=lambda x: (-x[1], x[0]))
    return res

vocab = cria_vocabulario(('AULA', 'CAO', 'ASA', 'CEGO', 'CEGA', 'CONE', 'COÇA', 'VACA', 'CASA'))
print(obtem_palavras(vocab, 4, 'C'))