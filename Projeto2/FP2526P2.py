#ist1117729

from platform import node


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
    """
    Função que cria uma casa do tabuleiro e representa a num tuplo(linha, coluna)

    Args:
        l (int): linha do tabuleiro (1 a 15)
        c (int): coluna do tabuleiro (1 a 15)

    Returns:
        tuplo: (l, c) representando a casa

    Raise:
        ValueError: se os números recebidos não forem inteiros
                    se os números recebidos forem menores que 1 e maiores que 15
    """
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
    if not isinstance(arg, tuple) or len(arg) != 2:
        return False
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
    if not type(s) == int or s < 0:
        return c

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
    if nivel not in ('FACIL', 'MEDIO', 'DIFICIL'):
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
    
    lista_letras.sort(key=lambda x: ABECEDARIO.index(x))
    
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
    if not isinstance(v, tuple) or not len(v) >= 1:
        raise ValueError("cria_vocabulario: argumento inválido")
    vocabulario_final = {}
    for palavra in v:
        if not isinstance(palavra, str):
            raise ValueError("cria_vocabulario: argumento inválido")

        if not (2 <= len(palavra) <= TAMANHO_DO_TABULEIRO):
            raise ValueError("cria_vocabulario: argumento inválido")

        for i in range(len(palavra)):
            if palavra[i] not in ABECEDARIO:
                raise ValueError("cria_vocabulario: argumento inválido")
        
        
        comprimento = len(palavra)
        letra_inicial = palavra[0] 
        pontuacao = sum(pontos[letra] for letra in palavra)
        chave = (comprimento, letra_inicial)
        
        
        if chave not in vocabulario_final:
            vocabulario_final[chave] = []
        vocabulario_final[chave].append((palavra, pontuacao))
    
    for chave in vocabulario_final: 
        vocabulario_final[chave] = sorted(vocabulario_final[chave], key = lambda x:(-x[1], [ABECEDARIO.index(letra) for letra in x[0]]))
        vocabulario_final[chave] = tuple(vocabulario_final[chave])
    
    return vocabulario_final

# Seletores
def obtem_pontos(vocabulario, palavra):
    chave = (len(palavra), palavra[0])
    if chave in vocabulario:
        # Percorre o tuplo de palavras para encontrar a correspondente
        for p, pontuacao in vocabulario[chave]:
            if p == palavra:
                return pontuacao  # Retorna a pontuação pré-calculada
    return 0  # Retorna 0 se a palavra não for encontrada

def obtem_palavras(vocabulario, comp, letra):
    chave = (comp, letra)
    if chave not in vocabulario:
        return ()
    return vocabulario[chave]

# Teste
def testa_palavra_padrao(vocabulario, palavra, padrao, conj):
    resultado = testa_palavra_padrao_auxiliar(vocabulario, palavra, padrao, conj)
    return len(resultado) > 0

def testa_palavra_padrao_auxiliar(vocabulario, palavra, padrao, conj):
    if len(palavra) != len(padrao):
        return []
    
    chave = (len(palavra), palavra[0])

    if chave in vocabulario:
        if not (any(p[0] == palavra for p in vocabulario[chave])):
            return []
    else:
        return []

    conjunto_letras = {}
    for letra in conj:
        if letra not in conjunto_letras:
            conjunto_letras[letra] = 1
        else:
            conjunto_letras[letra] += 1

    letras_usadas = []
    for i in range(len(palavra)):
        letra_palavra = palavra[i]
        letra_padrao = padrao[i]
        
        if letra_padrao == '.': 
            # Verificar se a letra está no cojunto e se existem occorrencias suficientes para usar
            if letra_palavra not in conjunto_letras or conjunto_letras[letra_palavra] == 0:
                return []

            
            conjunto_letras[letra_palavra] -= 1
            letras_usadas.append(palavra[i])
        else:
            # Se o padrão tiver uma letra têm de coincidir com a letra da palavra
            if letra_palavra != letra_padrao:
                return []
    
    return letras_usadas

def ficheiro_para_vocabulario(nome_fich):
    """
    Lê um ficheiro de texto e cria um TAD vocabulario com as palavras válidas.

    A função processa um ficheiro com uma palavra por linha, ignora linhas
    vazias, converte as palavras para maiúsculas e filtra-as de acordo
    com as regras do projeto (comprimento 2-15, letras do abecedário
    português).

    Args:
        nome_fich (str): O nome do ficheiro a ser lido.

    Returns:
        vocabulario: O TAD vocabulario criado com as palavras válidas.
    """
    palavras_validas = []
    with open(nome_fich, 'r') as f:
        for linha in f:
            palavra = linha.strip().upper()
            if 2 <= len(palavra) <= TAMANHO_DO_TABULEIRO and all(letra in ABECEDARIO for letra in palavra):
                palavras_validas.append(palavra)
            if not palavra:
                continue
            else:
                continue
    return cria_vocabulario(tuple(palavras_validas))

def vocabulario_para_str(vocabulario):
    palavras = []
    for comprimento in range(2, TAMANHO_DO_TABULEIRO + 1):
        for letra in ABECEDARIO:
            chave = (comprimento, letra)
            if chave in vocabulario:
                tuplo_palavras = obtem_palavras(vocabulario, comprimento, letra)
                for i in range(len(tuplo_palavras)):
                    palavra = tuplo_palavras[i][0]
                    palavras.append(palavra)
    return '\n'.join(palavras)

# Funcões de alto nível
def procura_palavra_padrao(vocabulario, padrao, letras, min_pontos):
    if padrao[0] != '.':
        primeira_letra = padrao[0]
        palavras_validas = obtem_palavras(vocabulario, len(padrao), primeira_letra)
        for palavra, pontuacao in palavras_validas:
            if pontuacao < min_pontos:
                break
            if testa_palavra_padrao(vocabulario, palavra, padrao, letras):
                return(palavra, pontuacao)
        return ('', 0)
    else:
        melhor_palavra = ''
        melhor_pontuacao = 0
        # Cria um conjunto de letras únicas disponíveis para a primeira posição.
        possivel_primeira_letras = sorted(list(set(letras)), key=lambda x: ABECEDARIO.index(x))

        # Itera sobre cada letra única como uma possível primeira letra.
        for possivel_letra in possivel_primeira_letras:
            palavras_validas = obtem_palavras(vocabulario, len(padrao), possivel_letra)
            for palavra, pontuacao in palavras_validas:
                if pontuacao < min_pontos:
                    break
                if testa_palavra_padrao(vocabulario, palavra, padrao, letras):
                    if pontuacao > melhor_pontuacao:
                        melhor_palavra = palavra
                        melhor_pontuacao = pontuacao
        return (melhor_palavra, melhor_pontuacao)
    
# TAD Tabuleiro
# Construtor
def cria_tabuleiro():
    """"
    Função que cria um tabuleiro vazio 15x15

    Args:
        Nenhum

    Returns:
        list: lista de 15 listas, cada uma com 15 elementos
              onde cada casa livre é rrepresentada por "."
    """
    tab = []
    
    for _ in range(TAMANHO_DO_TABULEIRO):
        linha = ['.'] * TAMANHO_DO_TABULEIRO
        tab.append(linha)
    
    return tab

# Seletores
def obtem_letra(t, c):
    """
    Função que mostra a letra que está numa casa do tabuleiro

    Args:
        tab (list): tabuleiro 15x15
        casa (tuple): (linha, coluna), entre 1 e 15

    Returns:
        str: letra ou se não estiver nenhuma letra nessa casa devolve uma string vazia
    """
    lin = obtem_lin(c)
    col = obtem_col(c)
    if t[lin - 1][col - 1] == '.':
        return ''
    else:
        return t[lin - 1][col - 1]
    
def obtem_valor_aux(t, c):
    """
    Função auxiliar que mostra o valor que está numa casa do tabuleiro

    Args:
        tab (list): tabuleiro 15x15
        casa (tuple): (linha, coluna), entre 1 e 15

    Returns:
        str: letra ou '.'
    """
    if obtem_letra(t, c) == '':
        return '.'
    else:
        return obtem_letra(t, c)

# Modificadores
def insere_letra(t, c, l):
    """
    Função que insere uma letra numa casa do tabuleiro (modificando destrutivamente)

    Args:
        tab (list): tabuleiro 15x15
        casa (tuple): (linha, coluna), entre 1 e 15
        letra (str): letra a inserir

    Returns:
        list: tabuleiro modificado
    """
    lin = obtem_lin(c)
    col = obtem_col(c)
    t[lin - 1][col - 1] = l
    return t

# Reconhecedor
def eh_tabuleiro(arg):
    for i in range(1, TAMANHO_DO_TABULEIRO + 1):
        for j in range(1, TAMANHO_DO_TABULEIRO + 1):
            letra = obtem_letra(arg, cria_casa(i, j))
            if letra not in ABECEDARIO:
                return False
            if letra == '' and obtem_valor_aux(arg, cria_casa(i, j)) != '.':
                return False
    return True

def eh_tabuleiro_vazio(arg):
    for i in range(1, TAMANHO_DO_TABULEIRO +1):
        for j in range(1, TAMANHO_DO_TABULEIRO + 1):
            if obtem_valor_aux(arg, cria_casa(i, j)) != '.':
                return False
    return True

# Teste
def tabuleiros_iguais(t1, t2):
    return t1 == t2

# Transformador
def tabuleiro_para_str(tab):
    """
    Função que converte o tabuleiro numa representação string legível

    Args:
        tab (list): tabuleiro 15x15

    Returns:
        str: representação textual do tabuleiro
    """
    tabuleiro = []
    
    # Numeração das colunas
    numeros_das_colunas1="                       1 1 1 1 1 1"
    numeros_das_colunas2="     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5"
    
    tabuleiro.append(numeros_das_colunas1)
    tabuleiro.append(numeros_das_colunas2)
    
    # Linha superior da moldura
    tabuleiro.append("   +" + "-" * 31 + "+")

    # Cada linha do tabuleiro é constitiuda pelo número da linha e o conteúdo das células
    for i in range(TAMANHO_DO_TABULEIRO):
        if i + 1 < 10:
            numeros_das_linhas = ' ' + str(i + 1)
        
        else:
            numeros_das_linhas = str(i + 1)
    
        linha = numeros_das_linhas + " |"
        
        for j in range(TAMANHO_DO_TABULEIRO):
            linha += " " + tab[i][j]
        
        linha += " |"
        
        tabuleiro.append(linha)
    
    # Linha inferior da moldura
    tabuleiro.append("   +" + "-" * 31 + "+")

    # Junta todas as linhas numa única string separada por quebras de linha
    resultado=""
    for k in range(len(tabuleiro)): 
        if k < (len(tabuleiro) -1):
            resultado += tabuleiro[k] + "\n"
        else:
            resultado += tabuleiro[k]
    
    return resultado

# Alto-nível
def obtem_padrao(tab, i, f):
    padrao = ''
    distancia = 0
    direcao = None
    linha_inicial, coluna_inicial = obtem_lin(i), obtem_col(i)
    linha_final, coluna_final = obtem_lin(f), obtem_col(f)
    if linha_inicial == linha_final:
        direcao = 'H', distancia = coluna_final - coluna_inicial
    elif coluna_inicial == coluna_final:
        direcao = 'V', distancia = linha_final - linha_inicial
    else:
        pass

    for d in range(0, distancia + 1):
        nova_casa = incrementa_casa(i, direcao, d)
        if obtem_letra(tab, nova_casa) == '':
            padrao += '.'
        else:
            padrao += obtem_letra(tab, nova_casa)
    return padrao