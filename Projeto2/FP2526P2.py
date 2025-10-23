#ist1117729

ABECEDARIO = {
    'A': 1, 'B': 2, 'C': 3, 'Ç': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 
    'I': 10, 'J': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'X': 23, 'Z': 24
    }

pontos = {  'A':1, 'B': 3,'C': 2,'Ç':3, 'D':2, 'E':1,
            'F':4, 'G': 4,'H': 4,'I': 1,'J': 5,'L': 2,
            'M':1, 'N': 3,'O': 1,'P': 2,'Q': 6,'R': 1,
            'S':1, 'T': 1,'U': 1,'V': 4,'X': 8,'Z': 8
            }

NUM_LETRAS_JOGADOR = 7
NUM_MAX_JOGADORES = 4
NUM_MIN_JOGADORES = 2
TAMANHO_DO_TABULEIRO = 15

# ----------------------------------- TAD CASA ----------------------------------- #

# Construtores
def cria_casa(lin, col):
    """
    Recebe 2 inteiros e devolve a casa correspondente no tabueliro
    
    Args:
        lin (int): linha do tabuleiro (1 a 15)
        col (int): coluna do tabuleiro (1 a 15)

    Returns:
        casa: O TAD casa

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
    """
    Devolve a coluna de uma casa

    Args:
        c (casa): O TAD casa

    Returns:
        int: número da coluna
    """
    return casa[1]
    
def obtem_lin(casa):
    """
    Devolve a linha de uma casa

    Args:
        c (casa): O TAD casa

    Returns:
        int: número da linha
    """
    return casa[0]

# Reconhecedor  
def eh_casa(arg):
    """
    Verifica se o argumento é um TAD casa válido

    Args:
        arg (universal): O argumento a verificar

    Returns:
        bool: True se o argumento for um TAD casa, False caso contrário
    """
    if not isinstance(arg, tuple) or len(arg) != 2:
        return False
    lin, col = arg
    return (type(lin) == int and type(col) == int 
    and 1 <= lin <= TAMANHO_DO_TABULEIRO 
    and 1 <= col <= TAMANHO_DO_TABULEIRO)

# Teste
def casas_iguais(c1, c2):
    """
    Verifica se duas casas são iguais

    Args:
        c1 (universal): O primeiro argumento
        c2 (universal): O segundo argumento

    Returns:
        bool: True se as casas forem iguais, False caso contrário
    """
    return (obtem_lin(c1) == obtem_lin(c2) 
            and obtem_col(c1) == obtem_col(c2))

# Transformador
def casa_para_str(c):
    """
    Converte um TAD casa para uma representação em string

    Args:
        c (casa): O TAD casa a converter

    Returns:
        str: representação da casa como string
    """
    return '(' + str(obtem_lin(c)) + ',' + str(obtem_col(c)) + ')'
    
def str_para_casa(s):
    """
    Converte uma string para um TAD casa

    Args:
        s (str): string que representa a casa

    Returns:
        casa: o TAD casa correspondente
    """
    s = s.strip('()')
    lin, col = map(int, s.split(','))
    return cria_casa(lin, col)

# Função de alto nível
def incrementa_casa(c, d, s):
    """
    Incrementa uma casa numa dada direção e numa dada distância

    Args:
        c (casa): O TAD casa inicial
        d (str): A direção ('H' para horizontal, 'V' para vertical)
        s (int): A distância a incrementar

    Returns:
        casa: O novo TAD casa, ou o original se a nova posição for inválida
    """
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

# --------------------------------- TAD JOGADOR ---------------------------------- #

# Construtores
def cria_humano(nome):
    """
    Cria um jogador humano

    Args:
        nome (str): O nome para o jogador

    Returns:
        jogador: O TAD que representa o jogador humano

    Raises:
        ValueError: Se o nome não for uma string não vazia
    """
    if type(nome) != str or nome == "":
        raise ValueError("cria_humano: argumento inválido")
    return {'nome': nome, 'pontos': 0, 'letras':{}}

def cria_agente(nivel):
    """
    Cria um jogador agente

    Args:
        nivel (str): O nível de dificuldade do bot

    Returns:
        jogador: O TAD que representa o jogador agente

    Raises:
        ValueError: Se o nível for inválido
    """
    if nivel not in ('FACIL', 'MEDIO', 'DIFICIL'):
        raise ValueError("cria_agente: argumento inválido")
    return {'nivel': nivel, 'pontos': 0, 'letras':{}}

# Seletores
def jogador_identidade(j):
    """
    Devolve a identidade de um jogador, ou seja, nome para humano e nível para agente

    Args:
        j (jogador): O TAD jogador

    Returns:
        str: O nome ou o nível do jogador
    """
    if 'nome' in j:
        return j['nome']
    else:
        return  j['nivel']
    
def jogador_pontos(j):
    """
    Devolve os pontos de um jogador

    Args:
        j (jogador): O TAD jogador

    Returns:
        int: A pontuação do jogador
    """
    return j['pontos']

def jogador_letras(j):
    """
    Devolve uma string com as letras de um jogador, ordenadas alfabeticamente

    Args:
        j (jogador): O TAD jogador

    Returns:
        str: Uma string com as letras do jogador
    """
    lista_letras = []
    res = ''
    for letra, occ in j['letras'].items():
        lista_letras.extend(letra * occ)
    
    lista_letras.sort(key=lambda x: ABECEDARIO[x])
    
    for i in range(len(lista_letras)):
        res += lista_letras[i]
    
    return res

# Modificadores
def recebe_letra(j, l):
    """
    Adiciona uma letra as letras do jogador (modifica destrutivamente)

    Args:
        j (jogador): O TAD jogador
        l (str): A letra a ser adicionada

    Returns:
        jogador: O TAD jogador modificado
    """
    if l in j['letras']:
        j['letras'][l] += 1
    else:
        j['letras'][l] = 1
    return j

def usa_letra(j, l):
    """
    Remove uma letra das letras do jogador (modifica destrutivamente)

    Args:
        j (jogador): O TAD jogador
        l (str): A letra a ser removida

    Returns:
        jogador: O TAD jogador modificado
    """
    if l in j['letras']:
        j['letras'][l] -= 1
        if j['letras'][l] <= 0:
            del j['letras'][l]
        return j
    else:
        return j
    
def soma_pontos(j, p):
    """
    Adiciona pontos à pontuação do jogador (modifica destrutivamente)

    Args:
        j (jogador): O TAD jogador
        p (int): Os pontos a serem adicionados

    Returns:
        jogador: O TAD jogador modificado
    """
    j['pontos'] += p
    return j

# Reconhecedor
def eh_jogador(arg):
    """
    Verifica se o argumento é um TAD jogador válido

    Args:
        arg (universal): O argumento a ser verificado

    Returns:
        bool: True se for um jogador, False caso contrário
    """
    if type(arg) != dict:
        return False
    else: 
        return ('nome' in arg or 'nivel' in arg)

def eh_humano(arg):
    """
    Verifica se o argumento é um TAD jogador humano

    Args:
        arg (universal): O argumento a ser verificado

    Returns:
        bool: True se for um jogador humano, False caso contrário
    """
    if not eh_jogador(arg):
        return False
    return 'nome' in arg

def eh_agente(arg):
    """
    Verifica se o argumento é um TAD jogador agente

    Args:
        arg (universal): O argumento a ser verificado

    Returns:
        bool: True se for um jogador agente, False caso contrário
    """
    if not eh_jogador(arg):
        return False
    return 'nivel' in arg

# Teste
def jogadores_iguais(j1, j2):
    """
    Verifica se dois jogadores são iguais

    Args:
        j1 (jogador): O primeiro TAD jogador
        j2 (jogador): O segundo TAD jogador

    Returns:
        bool: True se os jogadores forem iguais, False caso contrário
    """
    if not(eh_jogador(j1) and eh_jogador(j2)):
        return False
    if eh_humano(j1) != eh_humano(j2):
        return False
    return ((jogador_identidade(j1) == jogador_identidade(j2))
            and jogador_pontos(j1) == jogador_pontos(j2)
            and jogador_letras(j1) == jogador_letras(j2))

# Transformador
def jogador_para_str(j):
    """
    Converte um TAD jogador para a sua representação em string

    Args:
        j (jogador): O TAD jogador

    Returns:
        str: A representação do jogador como string
    """
    # Formata a pontuação para ter sempre 3 espaços
    if jogador_pontos(j) < 10:
            pontos = "  " + str(jogador_pontos(j))
    elif jogador_pontos(j) < 100:
            pontos = " " + str(jogador_pontos(j))
    else:
            pontos = str(jogador_pontos(j))
    
    if eh_jogador(j):
        prefixo = str(jogador_identidade(j)) + ' (' + pontos + '):'
    if eh_agente(j):
        prefixo = 'BOT(' + str(jogador_identidade(j)) + ') (' + pontos + '):'
    
    return prefixo + "".join([' ' + letra for letra in jogador_letras(j)])

# Função de alto-nível
def distribui_letras(jog, saco, num):
    """
    Distribui um número de letras do saco para a mão de um jogador

    Args:
        jog (jogador): O TAD jogador
        saco (list): A lista de letras disponíveis (pilha)
        num (int): O número de letras a distribuir

    Returns:
        jogador: O TAD jogador modificado
    """
    if num <= len(saco):
        for _ in range(num):
            letra = saco.pop()
            recebe_letra(jog, letra)
    else:
        for _ in range(len(saco)):
            letra = saco.pop()
            recebe_letra(jog, letra)
    return jog

# ------------------------------- TAD VOCABULARIO -------------------------------- #

# Construtores
def cria_vocabulario(v):
    """
    Cria um TAD vocabulario a partir de um tuplo de palavras

    Args:
        v (tuple): um tuplo de palavras para criar o vocabulario

    Returns:
        vocabulario: o TAD vocabulario

    Raise:
        ValueError: 


    """
    if not isinstance(v, tuple) or v == () or len(v) != len(set(v)):
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
        vocabulario_final[chave] = sorted(vocabulario_final[chave], key = lambda x:(-x[1], [ABECEDARIO[letra] for letra in x[0]]))
        vocabulario_final[chave] = tuple(vocabulario_final[chave])
    return vocabulario_final

# Seletores
def obtem_pontos(vocabulario, palavra):
    """
    Devolve a pontuação de uma palavra que está no vocabulario

    Args:
        vocabulario (universal): o TAD vocabulario onde se vai procurar
        palavra (str): a palavra para saber os pontos

    Returns:
        int: os pontos da palavra, ou 0 se não existir
    """
    chave = (len(palavra), palavra[0])
    if chave in vocabulario:
        # Percorre o tuplo de palavras para encontrar a correspondente
        for p, pontuacao in vocabulario[chave]:
            if p == palavra:
                return pontuacao  # Retorna a pontuação pré-calculada
    return 0  # Retorna 0 se a palavra não for encontrada

def obtem_palavras(vocabulario, comp, letra):
    """
    Devolve um tuplo com as palavras com um certo tamanho e letra inicial

    Args:
        vocabulario (universal): o TAD vocabulario onde de vai buscar as palavras
        comp (int): o comprimento das palavras
        letra (str): a letra com que as palavras devem começar

    Returns:
        tuple: um tuplo com as palavras encontradas, ou um tuplo vazio se não encontrar nenhuma
    """
    chave = (comp, letra)
    if chave not in vocabulario:
        return ()
    return vocabulario[chave]

# Teste
def testa_palavra_padrao(vocabulario, palavra, padrao, conj):
    """
    Vê se uma palavra pode ser formada num padrão, usando as letras que o jogador tem e se a palavra existe no vocabulario

    Args:
        vocabulario (universal): o TAD vocabulario para ver se a palavra é válida
        palavra (str): a palavra que se quer testar
        padrao (str): o padrão do tabuleiro onde se quer jogar
        conj (str): uma string com as letras que o jogador tem na mão

    Returns:
        bool: True se der para formar a palavra, False se não der

    """
    if len(palavra) != len(padrao) or obtem_pontos(vocabulario, palavra) == 0:
        return False
    
    letras_disponiveis = {}
    for letra in conj:
        if letra not in letras_disponiveis:
            letras_disponiveis[letra] = 1
        else:
            letras_disponiveis[letra] += 1

    for i in range(len(palavra)):
        letra_palavra = palavra[i]
        letra_padrao = padrao[i]
        
        if letra_padrao == '.': 
            # Verificar se a letra está no cojunto de letras disponiveis 
            # e se existem occorrencias suficientes para usar
            if letra_palavra not in letras_disponiveis or letras_disponiveis[letra_palavra] == 0:
                return False
            letras_disponiveis[letra_palavra] -= 1

        else:
            # Se o padrão tiver uma letra têm de coincidir com a letra da palavra
            if letra_palavra != letra_padrao:
                return False
    
    return True

def ficheiro_para_vocabulario(nome_fich):
    """
    Lê um ficheiro de texto e cria um TAD vocabulario com as palavras válidas

    Args:
        nome_fich (str): o nome do ficheiro para ler

    Returns:
        vocabulario: o TAD vocabulario criado a partir do ficheiro
    """
    palavras_validas = []
    with open(nome_fich, 'r', encoding='utf-8') as f:
        for linha in f:
            palavra = linha.strip().upper()
            if 2 <= len(palavra) <= TAMANHO_DO_TABULEIRO and all(letra in ABECEDARIO for letra in palavra):
                palavras_validas.append(palavra)
    return cria_vocabulario(tuple(set(palavras_validas)))

def vocabulario_para_str(vocabulario):
    """
    Transforma o TAD vocabulario numa string legível

    Args:
        vocabulario (universal): o TAD vocabulario que se quer converter

    Returns:
        str: uma string com todas as palavras do vocabulario, uma por linha

    """
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
    """
    Procura a melhor palavra que encaixa num padrão, usando as letras do jogador e que tenha uma pontuação mínima

    Args:
        vocabulario (universal): o TAD vocabulario para procurar palavras
        padrao (str): o padrão do tabuleiro onde se quer jogar
        letras (str): uma string com as letras que o jogador tem na mão
        min_pontos (int): a pontuação mínima que a palavra tem de ter

    Returns:
        tuple: um tuplo com a melhor palavra e a sua pontuação, ou ('', 0) se não encontrar nada

    """
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
        possivel_primeira_letras = sorted(list(set(letras)), key=lambda x: ABECEDARIO[x])

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
    
# --------------------------------- TAD TABULEIRO -------------------------------- #

# Construtor
def cria_tabuleiro():
    """"
    cria um tabuleiro de jogo vazio

    Args:
        Nenhum

    Returns:
        tabuleiro: um tabuleiro 15x15 vazio, só com pontos

    """
    tab = []
    
    for _ in range(TAMANHO_DO_TABULEIRO):
        linha = ['.'] * TAMANHO_DO_TABULEIRO
        tab.append(linha)
    
    return tab

# Seletores
def obtem_letra(t, c):
    """
    Devolve a letra que está numa casa do tabuleiro

    Args:
        t (universal): o TAD tabuleiro
        c (casa): o TAD casa que se pretende obter a letra

    Returns:
        str: a letra que está na casa, ou uma string vazia se estiver livre
    """
    lin = obtem_lin(c)
    col = obtem_col(c)
    if t[lin - 1][col - 1] == '.':
        return ''
    else:
        return t[lin - 1][col - 1]

# Modificadores
def insere_letra(t, c, l):
    """
    Insere uma letra numa casa do tabuleiro (modificando destrutivamente)

    Args:
        t (universal): o TAD tabuleiro que vai ser modificado
        c (casa): o TAD casa onde a letra vai ser inserida
        l (str): a letra para inserir

    Returns:
        tabuleiro: tabuleiro modificado
    """
    lin = obtem_lin(c)
    col = obtem_col(c)
    t[lin - 1][col - 1] = l
    return t

# Reconhecedor
def eh_tabuleiro(arg):
    """
    Vê se o argumento é um TAD tabuleiro

    Args:
        arg (universal): o argumento para verificar

    Returns:
        bool: True se for um tabuleiro, False se não for
    """
    if type(arg) != list:
        return False
    else:
        for i in range(1, TAMANHO_DO_TABULEIRO + 1):
            for j in range(1, TAMANHO_DO_TABULEIRO + 1):
                letra = obtem_letra(arg, cria_casa(i, j))
                if letra != '' and letra not in ABECEDARIO:
                    return False
        return True

def eh_tabuleiro_vazio(arg):
    """
    Vê se um tabuleiro vazio

    Args:
        arg (universal): o TAD tabuleiro para verificar

    Returns:
        bool: True se o tabuleiro estiver vazio, False caso contrário
    """
    if type(arg) != list:
        return False
    else:
        for i in range(1, TAMANHO_DO_TABULEIRO +1):
            for j in range(1, TAMANHO_DO_TABULEIRO + 1):
                if obtem_letra(arg, cria_casa(i, j)) != '':
                    return False
        return True



# Teste
def tabuleiros_iguais(t1, t2):
    """
    Vê se dois tabuleiros são iguais

    Args:
        t1 (universal): o primeiro TAD tabuleiro
        t2 (universal): o segundo TAD tabuleiro

    Returns:
        bool: True se forem iguais, False se não forem
    """
    if type(t1) != list or type(t2) != list:
        return False
    else:
        for linha in range(1, TAMANHO_DO_TABULEIRO + 1):
            for coluna in range(1, TAMANHO_DO_TABULEIRO + 1):
                casa = cria_casa(linha, coluna)
                if obtem_letra(t1, casa) != obtem_letra(t2, casa):
                    return False
        return True

# Transformador
def tabuleiro_para_str(tab):
    """
    Converte o tabuleiro numa representação string legível

    Args:
        tab (universal): o TAD tabuleiro

    Returns:
        str: a string que representa o tabuleiro
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

# Funções de alto-nível
def obtem_padrao(tab, i, f):
    """
    Devolve o padrão de letras e pontos entre duas casas

    Args:
        tab (universal): o TAD tabuleiro
        i (casa): a casa inicial
        f (casa): a casa final

    Returns:
        str: o padrão de letras e pontos
    """
    padrao = ''
    distancia = 0
    direcao = None
    linha_inicial, coluna_inicial = obtem_lin(i), obtem_col(i)
    linha_final, coluna_final = obtem_lin(f), obtem_col(f)
    if linha_inicial == linha_final:
        direcao = 'H' 
        distancia = coluna_final - coluna_inicial
    elif coluna_inicial == coluna_final:
        direcao = 'V'
        distancia = linha_final - linha_inicial
    else:
        pass

    for d in range(0, distancia + 1):
        nova_casa = incrementa_casa(i, direcao, d)
        if obtem_letra(tab, nova_casa) == '':
            padrao += '.'
        else:
            padrao += obtem_letra(tab, nova_casa)
    return padrao

def insere_palavra(tab, casa, direcao, palavra):
    """
    insere uma palavra no tabuleiro a partir de uma casa e direção,
    modificando destrutivamente o tabuleiro

    Args:
        tab (tabuleiro): o TAD tabuleiro
        casa (casa): a casa onde a palavra começa
        direcao (str): 'H' para horizontal ou 'V' para vertical
        palavra (str): palavra a inserir

    Returns:
        tabuleiro: tabuleiro modificado

    Raise:
        ValueError: se a palavra não couber dentro dos limites do tabuleiro
                    se a direção for diferente de 'H' ou
    """
    linha = obtem_lin(casa)
    coluna = obtem_col(casa)

    if direcao == 'H' and coluna + len(palavra) - 1 > TAMANHO_DO_TABULEIRO:
        raise ValueError("insere_palavra: argumentos inválidos")
    if direcao == 'V' and linha + len(palavra) - 1 > TAMANHO_DO_TABULEIRO:
        raise ValueError("insere_palavra: argumentos inválidos")

    inc_linha = 0
    inc_coluna = 0
    
    if direcao == 'H':
        inc_coluna = 1
    elif direcao == 'V':
        inc_linha = 1
    else:
        return tab
    
    for i in range(len(palavra)):
        nova_casa = cria_casa(linha + inc_linha * i, coluna + inc_coluna * i)
        tab = insere_letra(tab, nova_casa, palavra[i])
    
    return tab

def obtem_subpadroes(tab, i, f, l):
    """
    Devolve todos os subpadrões válidos entre duas casas

    Args:
        tab (universal): o TAD tabuleiro
        i (casa): a casa inicial da linha/coluna
        f (casa): a casa final da linha/coluna
        l (int): o número de letras que o jogador tem

    Returns:
        tuple: um tuplo com os subpadrões e outro com as casas iniciais correspondentes
    """
    # Determina a direção e obtem o padrão principal
    direcao = 'H' if obtem_lin(i) == obtem_lin(f) else 'V'
    padrao = obtem_padrao(tab, i, f)
    
    casas_inicias = []
    sub_padroes = []

    # Define o início do subpadrão(índice 'j')
    for j in range(len(padrao)):
        # Define o fim do subpadrão (índice `k`)
        # Decresnte para começar nos padrões menores
        for k in range(len(padrao), j, -1):
            sub_padrao = padrao[j:k]
            
            espacos_livres = sub_padrao.count('.')   
            tem_espaco = espacos_livres > 0
            tem_letra = any(caractere != '.' for caractere in sub_padrao)
            toca_letra_antes = False
            toca_letra_depois = False
            if j > 0:
                if padrao[j - 1] != '.':
                    toca_letra_antes = True
            if k < len(padrao) :
                if padrao[k] != '.':
                    toca_letra_depois = True

            if tem_letra and tem_espaco and espacos_livres <= l:
                if not (toca_letra_antes or toca_letra_depois):
                    sub_padroes.append(sub_padrao)
                    casa_inicial = incrementa_casa(i, direcao, j)
                    casas_inicias.append(casa_inicial)
    return tuple(sub_padroes), tuple(casas_inicias)

def gera_todos_padroes(tab, l):
    """
    Gera todos os padrões possíveis no tabuleiro inteiro

    Args:
        tab (universal): o TAD tabuleiro
        l (int): o número de letras que o jogador tem

    Returns:
        tuple: um tuplo com todos os padrões, um com as casas iniciais e outro com as direções

    """
    todos_padroes = []
    todas_casas = []
    todas_direcoes = []

    for linhas in range(1, TAMANHO_DO_TABULEIRO + 1):
        casa_inicial_h = cria_casa(linhas, 1)
        casa_final_h = cria_casa(linhas, TAMANHO_DO_TABULEIRO)
        sub_padroes_h, casas_inicias_h = obtem_subpadroes(tab, casa_inicial_h, casa_final_h, l)
        todos_padroes.extend(sub_padroes_h)
        todas_casas.extend(casas_inicias_h)
        todas_direcoes.extend(['H'] * len(sub_padroes_h))

    for colunas in range(1, TAMANHO_DO_TABULEIRO + 1):
        casa_inicial_v = cria_casa(1, colunas)
        casa_final_v = cria_casa(TAMANHO_DO_TABULEIRO, colunas)
        sub_padroes_v, casas_inicias_v = obtem_subpadroes(tab, casa_inicial_v, casa_final_v, l)
        todos_padroes.extend(sub_padroes_v)
        todas_casas.extend(casas_inicias_v)
        todas_direcoes.extend(['V'] * len(sub_padroes_v))

    return tuple(todos_padroes), tuple(todas_casas), tuple(todas_direcoes)

# ----------------------------- FUNÇÕES PRINCIPAIS DO JOGO ----------------------------- #

def gera_numero_aleatorio(estado):
    """
    gera um número pseudo-aleatório usando o algoritmo xorshift

    Args:
        estado (int): estado atual do gerador

    Returns:
        int: número pseudo-aleatório(novo estado do gerador)
    """
    # Algoritmo xorshift32 (32 bits)
    estado ^= (estado << 13) & 0xFFFFFFFF
    estado ^= (estado >> 17) & 0xFFFFFFFF
    estado ^= (estado << 5) & 0xFFFFFFFF

    return estado

def permuta_letras(letras, estado):
    """
    altera a ordem das letras na lista, destrutivamente usando
    o gerador de números aleatórios

    Args:
        letras (list): lista de letras (strings de 1 caractere)
        estado (int): estado inicial do gerador de numeros aleatórios

    Returns:
        None: não devolve nada, só mexe na lista
    """
    n = len(letras)
    for i in range(n - 1, 0, -1):
        estado = gera_numero_aleatorio(estado)
        j = estado % (i + 1)
        letras[i], letras[j] = letras[j], letras[i]
        
def baralha_saco(estado):
    """
    Cria a pilha de letras do jogo e baralha-a

    Args:
        estado (int): o estado para o gerador de números aleatórios

    Returns:
        list: a lista de letras do saco, toda baralhada
    """
    saco = {
            'A':14, 'B': 3,'C': 4,'Ç':2, 'D':5, 'E':11,
            'F':2, 'G': 2,'H': 2,'I': 10,'J': 2,'L': 5,
            'M':6, 'N': 4,'O': 10,'P': 4,'Q': 1,'R': 6,
            'S':8, 'T': 5,'U': 7,'V': 2,'X': 1,'Z': 1}
    
    lista_letras = []
        
    # Ordenar pela ordem alfabética
    for letra in saco:
            lista_letras.extend([letra] * saco[letra])
    
    lista_letras.sort(key=lambda x: ABECEDARIO[x])

    permuta_letras(lista_letras, estado)
        
    return lista_letras

def jogada_humano(tab, jog, vocab, pilha):
    """
    Processa a jogada de um jogador humano, lendo o que ele escreve

    Args:
        tab (universal): o TAD tabuleiro do jogo
        jog (universal): o TAD jogador que vai jogar
        vocab (universal): o TAD vocabulario com as palavras
        pilha (list): a pilha de letras 

    Returns:
        bool: True se a jogada for válida (jogou ou trocou), False se passou a vez

    """
    # Até as instruções serem válidas
    while True:
        # Recebe um input com as instruções do jogador
        jogada = input("Jogada " + str(jogador_identidade(jog)) + ": ")
        if '  'in jogada:
            continue
        jogada_recebida = jogada.strip().split()                                ####TENTATIVA TestScrabble2::test_4
        
        if len(jogada_recebida) == 0:
            continue

        # Caso o jogador queira passar
        if jogada_recebida[0] == 'P':
            if len(jogada_recebida) == 1:
                return False

        # Caso o jogador queira trocar letras
        elif jogada_recebida[0] == 'T':
            if processa_troca(jogada_recebida, jog, pilha):
                return True

        # Caso o jogador queira jogar uma palavra
        elif jogada_recebida[0] == 'J':
            if jogar(tab, jog, vocab, pilha, jogada_recebida):
                return True
            
def processa_troca(jogada_recebida, jog, pilha):
    """
    Função auxiliar para tratar da troca de letras de um jogador

    Args:
        jogada_recebida (list): a lista com o comando 'T' e as letras para trocar
        jog (universal): o TAD jogador que quer trocar
        pilha (list): a pilha de letras do jogo

    Returns:
        bool: True se a troca foi bem sucedida, False se não foi

    """
    # Extrai as letras que o jogador deseja trocar
    letras_para_troca = jogada_recebida[1:]
    
    for letra in letras_para_troca:
        if letra not in jogador_letras(jog) or jogador_letras(jog).count(letra) < letras_para_troca.count(letra):
            return False
    
    if len(pilha) >= 7:
        for l in letras_para_troca:
            # Remove as letras que o jogador quer trocar
            usa_letra(jog, l)
            
            # Distribui novas letras para o jogador
            recebe_letra(jog, pilha.pop())
        return True

    return False

def jogar(tab, jog, vocab, pilha, jogada_recebida):
    """
    Função auxiliar para tratar de uma jogada de palavra

    Args:
        tab (universal): o TAD tabuleiro
        jog (universal): o TAD jogador que joga
        vocab (universal): o TAD vocabulario
        pilha (list): a pilha de letras
        jogada_recebida (list): o comando 'J' com a posição, direção e palavra

    Returns:
        bool: True se a jogada foi válida, False se não foi

    """
    if len(jogada_recebida)<5:
        return False

    # Extrai as informações para jogar
    linha = int(jogada_recebida[1])
    coluna = int(jogada_recebida[2])
    casa_inicial = cria_casa(linha, coluna)
    direcao = jogada_recebida[3]
    palavra = jogada_recebida[4]
    
    if obtem_pontos(vocab, palavra) == 0:
        return False
    casa_final = incrementa_casa(casa_inicial, direcao, len(palavra) - 1)

    if direcao not in ('H', 'V') or len(palavra) < 2:
        return False
    
    if casas_iguais(casa_final, casa_inicial) and len(palavra) > 1:
        return False
    
    padrao = obtem_padrao(tab, casa_inicial, casa_final)
    letras_jogador = jogador_letras(jog)

    if not testa_palavra_padrao(vocab, palavra, padrao, letras_jogador):
        return False
    
    primeira = eh_tabuleiro_vazio(tab)
    if primeira:
        centro = cria_casa(8, 8)
        toca_centro = False
        for i in range(len(palavra)):
            if casas_iguais(centro, incrementa_casa(casa_inicial, direcao, i)):
                toca_centro = True
                break
        if not toca_centro:
            return False
    else:
        if all(c == '.' for c in padrao):
            return False


    contar_letras_usadas = 0
    for i in range(len(palavra)):
        if padrao[i] == '.':
            usa_letra(jog, palavra[i])
            contar_letras_usadas += 1
    
    insere_palavra(tab, casa_inicial, direcao, palavra)

    # Atualiza o conjunto de letras do jogador    
    distribui_letras(jog, pilha, contar_letras_usadas)

    # Atualiza a pontuação do jogador
    soma_pontos(jog, obtem_pontos(vocab, palavra))
    
    return True

def jogada_agente(tab, jog, vocab, pilha):
    """
    Processa a jogada de um jogador agente (bot), dependendo nível acessa mais palavras

    Args:
        tab (universal): o TAD tabuleiro
        jog (universal): o TAD jogador agente
        vocab (universal): o TAD vocabulario
        pilha (list): a pilha de letras

    Returns:
        bool: True se o agente conseguiu jogar ou trocar letras, False se passou a vez
    """
    nivel = jogador_identidade(jog)
    letras_agente = jogador_letras(jog)
    numero_letras = len(letras_agente)

    if eh_tabuleiro_vazio(tab):
        print('Jogada ' + str(nivel) + ': P') 
        return False
    
    # Tentajogar
    (sub_padroes, casas_inicias, direcoes) = gera_todos_padroes(tab, numero_letras)

    if nivel == 'FACIL':
        N = 100
    elif nivel == 'MEDIO':
        N = 50
    else:
        N = 10
    
    sub_padroes_slicing = sub_padroes[::N]
    casas_inicias_slicing = casas_inicias[::N]
    direcoes_slicing = direcoes[::N]
    
    melhor_palavra = ''
    melhor_pontuacao = -1
    jogada_final = ()
    padrao_atual = ''

    for i in range(len(sub_padroes_slicing)):
        padrao_atual = sub_padroes_slicing[i]
        
        palavra, pontuacao = procura_palavra_padrao(vocab, padrao_atual, letras_agente, 0)
        
        if pontuacao > melhor_pontuacao:
            melhor_palavra = palavra
            melhor_pontuacao = pontuacao
        
            if melhor_palavra == '' and melhor_pontuacao == 0:
                jogada_final = ()
            else:
                jogada_final = (melhor_palavra, melhor_pontuacao, casas_inicias_slicing[i], direcoes_slicing[i], padrao_atual)
    
    if jogada_final != ():    
            print('Jogada ' + str(nivel) + ': J '+ str(obtem_lin(jogada_final[2])) + ' ' 
                + str(obtem_col(jogada_final[2])) + ' ' + jogada_final[3] + ' ' + jogada_final[0])
            palavra = jogada_final[0]
            
            contar_letras_usadas = 0
            for i in range(len(palavra)):
                if jogada_final[4][i] == '.':
                    usa_letra(jog, palavra[i])
                    contar_letras_usadas += 1
        
            insere_palavra(tab, jogada_final[2], jogada_final[3], palavra)

            # Atualiza o conjunto de letras do jogador    
            distribui_letras(jog, pilha, contar_letras_usadas)

            # Atualiza a pontuação do jogador
            soma_pontos(jog, jogada_final[1])
            
            return True
    
    # Trocar
    elif jogada_final == () and len(pilha) >= 7 :
        letras_a_trocar = list(letras_agente)
        for l in letras_agente:
            usa_letra(jog, l)
        
        distribui_letras(jog, pilha, len(letras_a_trocar))
        print('Jogada ' + str(nivel) + ': T ' + ' '.join(letras_a_trocar))
        return True
        
    # Passar
    else:
        print('Jogada ' + str(nivel) + ': P')
        return False
  
def scrabble2(jogadores, nome_fich, estado):
    """
    Função principal que corre o jogo Scrabble2 com 2 a 4 jogadores humanos ou agentes

    Args:
        jogadores (tuple): um tuplo com os nomes dos jogadores (humanos ou agentes)
        nome_fich (str): o nome do ficheiro do vocabulário
        estado (int): a seed para o gerador de números aleatórios

    Returns:
        tuple: um tuplo com as pontuações finais de cada jogador

    Raise:
        ValueError: 

        

    """
    print("Bem-vindo ao SCRABBLE2.")
    tab=cria_tabuleiro()
    
    if not isinstance(jogadores, tuple) or not(NUM_MIN_JOGADORES <= len(jogadores) <= NUM_MAX_JOGADORES ):
        raise ValueError("scrabble2: argumentos inválidos")
    if type(estado) != int or estado < 0 :
        raise ValueError("scrabble2: argumentos inválidos")
    if isinstance(nome_fich, str) == False:
        raise ValueError("scrabble2: argumentos inválidos")                 ### tentativa TestScrabble2Exceptions::test_6
    
    pilha = baralha_saco(estado)        
    
    lista_de_jogadores = []
    for jogador in jogadores:
        if (not(isinstance(jogador, str)) or jogador  == '' ):
            raise ValueError("scrabble2: argumentos inválidos")
        if jogador[0] == '@':
            if jogador[1:] not in ('FACIL', 'MEDIO', 'DIFICIL'):
                raise ValueError("scrabble2: argumentos inválidos")         ##### TENTATIVA TestScrabble2Exceptions::test_4
            lista_de_jogadores.append(cria_agente(jogador[1:]))
        else:
            lista_de_jogadores.append(cria_humano(jogador))
    
    for jog in lista_de_jogadores:
        distribui_letras(jog, pilha, NUM_LETRAS_JOGADOR)
    
    vocab = ficheiro_para_vocabulario(nome_fich)
    passagens_seguidas = 0
    indice_jogador_atual = 0
    jogo_continua = True
    while jogo_continua:
        print(tabuleiro_para_str(tab))
        for jog in lista_de_jogadores:
            print(jogador_para_str(jog))
        
        if eh_humano(lista_de_jogadores[indice_jogador_atual]):
            jogada = jogada_humano(tab, lista_de_jogadores[indice_jogador_atual], vocab, pilha)
        else:
            jogada = jogada_agente(tab, lista_de_jogadores[indice_jogador_atual], vocab, pilha)

        if jogada ==  False:
            passagens_seguidas += 1
        else:
            passagens_seguidas = 0
        
        if passagens_seguidas == len(lista_de_jogadores):
            jogo_continua = False
            break
        
        if (jogador_letras(lista_de_jogadores[indice_jogador_atual]) == '' 
            and pilha == []):
            jogo_continua = False
            break
        
        if indice_jogador_atual + 1 == len(lista_de_jogadores):
            indice_jogador_atual = 0        
        else:
            indice_jogador_atual += 1

    return tuple(jogador_pontos(jog) for jog in lista_de_jogadores)