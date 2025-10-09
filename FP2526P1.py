# This is the Python script for your project

ABECEDARIO = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O',
                  'P','Q','R','S','T','U','V','X','Z')

PONTOS = {  
    'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2,
    'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8}



def cria_conjunto(let, occ):
    """
    Função que cria um cojunto de letras representadas num dicionário com o seu
    número de ocorrências

    Args:
        let (tuplo): letras(strings de 1 caractere)
        occ (tuplo): tuplo de inteiros positivos, cada um representando 
                     o número de ocorrências da letra correspondente em "let"

    Return:
        dict: dicionário {letra: ocorrências}, representando o conjunto de letras
    
    Raises:
        ValueError: se os argumentos não forem tuplos
                    se os tuplos recebidos tiverem comprimentos diferentes
                    se as letras não forem strings de 1 caractere
                    se a letra não estiver no abecedário português
                    se o número de occorências de uma letra não for inteiro maior que 0
    """
    if not isinstance(let, tuple) or not isinstance(occ, tuple):
        raise ValueError("cria_conjunto: argumentos inválidos")
    
    if len(let) != len(occ):
        raise ValueError("cria_conjunto: argumentos inválidos")
    
    d = {}
    for i in range(len(let)):
        letra = let[i]
        numero = occ[i]
        
        if not isinstance(letra, str) or len(letra) != 1:
            raise ValueError("cria_conjunto: argumentos inválidos")
        letra = letra.upper()
        
        if letra not in ABECEDARIO:
            raise ValueError("cria_conjunto: argumentos inválidos")
        
        if not type(numero) == int or numero <= 0:
            raise ValueError("cria_conjunto: argumentos inválidos")
        
        d[letra] = numero
    
    return d



def gera_numero_aleatorio(estado):
    """
    Função que gera um número pseudo-aleatório usando o algoritmo xorshift

    Args:
        estado (int): estado atual do gerador

    Return:
        int: número pseudo-aleatório(novo estado do gerador)
    
    Raises:
        ValueError: se o estado não for um número inteiro positivo
    """
    if not type(estado) == int and  estado < 0 :
        raise ValueError("gera_numero_aleatorio: argumentos inválidos")
    
    # Algoritmo xorshift32 (32 bits)
    estado ^= (estado << 13) & 0xFFFFFFFF
    estado ^= (estado >> 17) & 0xFFFFFFFF
    estado ^= (estado << 5) & 0xFFFFFFFF
    
    return estado   



def permuta_letras(letras, estado):
    """
    Função que altera a ordem das letras na lista, destrutivamente usando
    o gerador de números aleatórios

    Args:
        letras (list): lista de letras (strings de 1 caractere)
        estado (int): estado inicial do gerador de numeros aleatórios

    Return:
        não retorna nada, alterando destrutivamente o argumento letras
    """
    n = len(letras)
    for i in range(n - 1, 0, -1):
        estado = gera_numero_aleatorio(estado)              # Obtém números pseudo-aleatórios chamando gera_numero_aleatorio
        j = estado % (i + 1)                                # Usa o resto da divisão (%) para garantir que 0 < j < i 
        letras[i], letras[j] = letras[j], letras[i]



def baralha_conjunto(conj, estado):
    """
    Função que constrói uma lista de letras de um conjunto e baralha-as

    Args:
        conj (dict): dicionário no formato {letra: ocorrências}
        estado (int): inteiro positivo
    
    Return:
        list: lista de letras baralhada, contendo todas as letras e as ocorrências delas
    """
    lista_letras = []
    for letra in conj:
        lista_letras.extend([letra] * conj[letra])

    permuta_letras(lista_letras, estado)
    
    return lista_letras



def testa_palavra_padrao(palavra, padrao, conj):
    """
    Função que verifica se é possível formar uma palavra substituindo os '.' e as letras do padrão 
    por letras contidas no conjunto de letras

    Args:
        palavra (str): palavra que se pretende escrever
        padrao (str): string do mesmo comprimento que a palavra, composta por letras e '.'
        conj (dict): dicionário de letras de formato {letra: ocorrências}

    Return:
        bool: True se for possível formar a palavra substituindo os '.' por letras do conjunto,
              Caso contrário, False
    """
    resultado = testa_palavra_padrao_auxiliar(palavra, padrao, conj)
    return len(resultado) > 0


def testa_palavra_padrao_auxiliar(palavra, padrao, conj):
    if len(palavra) != len(padrao):
        return []
    
    ocorrencias = conj.copy()
    letras_usadas = []
    for i in range(len(palavra)):
        letra_palavra = palavra[i]
        letra_padrao = padrao[i]
        
        if letra_padrao == '.': 

            # Verificar se a letra está no cojunto e se existem suficientes para usar
            if letra_palavra not in ocorrencias or ocorrencias[letra_palavra] == 0:
                return []
            
            ocorrencias[letra_palavra] -= 1
            letras_usadas.append(palavra[i])
        else:
            if letra_palavra != letra_padrao:
                return []
    
    return letras_usadas



def cria_tabuleiro():
    """"
    Função que cria um tabuleiro vazio 15x15

    Args:
        Nenhum

    Return:
        lista de 15 listas, cada uma com 15 elementos
        onde cada casa livre é rrepresentada por "."
    """
    tab = []
    
    for _ in range(15):
        linha = ['.'] * 15
        tab.append(linha)
    
    return tab



def cria_casa(l, c):
    """
    Função que cria uma casa do tabuleiro e representa a num tuplo(linha, coluna)

    Args:
        l (int): linha do tabuleiro (1 a 15)
        c (int): coluna do tabuleiro (1 a 15)

    Return:
        um tuplo (l, c) representando a casa

    Raise:
        ValueError: se os números recebidos não forem inteiros
                    se os números recebidos forem menores que 1 e maiores que 15
    """
    if not type(l) == int or not type(c) == int or l < 1 or l > 15 or c < 1 or c > 15:
        raise ValueError("cria_casa: argumentos inválidos")
    
    return (l, c)



def obtem_valor(tab, casa):
    """
    Função que mostra o valor que está numa casa do tabuleiro

    Args:
        tab (list): tabuleiro 15x15
        casa (tuple): (linha, coluna), entre 1 e 15

    Return:
        str: letra ou '.'
    """
    linha, coluna = casa
    
    return tab[linha - 1][coluna - 1]



def insere_letra(tab, casa, letra):
    """
    Função que insere uma letra numa casa do tabuleiro (modificando destrutivamente)

    Args:
        tab (list): tabuleiro 15x15
        casa (tuple): (linha, coluna), entre 1 e 15
        letra (str): letra a inserir

    Return:
        list: tabuleiro modificado
    """
    linha, coluna = casa    

    tab[linha - 1][coluna - 1] = letra
    return tab



def obtem_sequencia(tab, casa, direcao, tamanho):
    """
    Função que obtém uma dada sequência no tabuleiro

    Args:
        tab (list): tabuleiro 15x15
        casa (tuple): (linha, coluna), entre 1 e 15
        direcao (str): 'H' para horizontal ou 'V' para vertical
        tamanho (int): número de casas a ler

    Return:
        str: sequência de caracteres do tabuleiro

    Raise:
        ValueError: se a o tamanho da sequencia passar as bordas do tabuleiro
                    se a direção for diferente de 'H' ou 'V'
    """
    l, c = casa
    linha = l 
    coluna = c 

    if direcao == 'H' and coluna + tamanho - 1 > 15:
        raise ValueError("obtem_sequencia: argumentos inválidos")
    
    if direcao == 'V' and linha + tamanho - 1 > 15:
        raise ValueError("obtem_sequencia: argumentos inválidos")
 
    inc_linha = 0
    inc_coluna = 0
    
    if direcao == "H":
        inc_coluna = 1
    
    elif direcao == "V":
        inc_linha = 1
    
    else:
        raise ValueError("obtem_sequencia: argumentos inválidos")
    
    sequencia = ""
    for i in range(tamanho):
        
        # Dependenda da direção o incremento das linhas ou das colunas pode ser 0 ou 1*i
        nova_casa = cria_casa(linha + (inc_linha * i), coluna + (inc_coluna * i))

        sequencia += obtem_valor(tab, nova_casa)

    return sequencia




def insere_palavra(tab, casa, direcao, palavra):
    """
    Função que insere uma palavra no tabuleiro a partir de uma casa e direção,
    modificando destrutivamente o tabuleiro

    Args:
        tab (list): tabuleiro 15x15
        casa (tuple): (linha, coluna), entre 1 e 15
        direcao (str): 'H' para horizontal ou 'V' para vertical
        palavra (str): palavra a inserir

    Return:
        list: tabuleiro modificado

    Raise:
        ValueError: se a palavra não couber dentro dos limites do tabuleiro
                    se a direção for diferente de 'H' ou
    """
    linha, coluna = casa

    if direcao == 'H' and coluna + len(palavra) - 1 > 15:
        raise ValueError("insere_palavra: argumentos inválidos")
    
    if direcao == 'V' and linha + len(palavra) - 1 > 15:
        raise ValueError("insere_palavra: argumentos inválidos")

    inc_linha = 0
    inc_coluna = 0
    if direcao == 'H':
        inc_coluna = 1
    
    elif direcao == 'V':
        inc_linha = 1
    
    else:
        raise ValueError("insere_palavra: argumentos inválidos")

    for i in range(len(palavra)):
        nova_casa = cria_casa(linha + inc_linha * i, coluna + inc_coluna * i)
        
        tab = insere_letra(tab, nova_casa, palavra[i])
    
    return tab



def tabuleiro_para_str(tab):
    """
    Função que converte o tabuleiro numa representação string legível

    Args:
        tab (list): tabuleiro 15x15

    Return:
        str: representação textual do tabuleiro
    """
    tabuleiro = []
    
    numeros_das_colunas1="                       1 1 1 1 1 1"
    numeros_das_colunas2="     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5"
    
    tabuleiro.append(numeros_das_colunas1)
    tabuleiro.append(numeros_das_colunas2)
    tabuleiro.append("   +" + "-" * 31 + "+")               # Linha superior da moldura

    for i in range(15):
        if i + 1 < 10:
            numeros_das_linhas = ' ' + str(i + 1)
        
        else:
            numeros_das_linhas = str(i + 1)
    
        linha = numeros_das_linhas + " |"
        
        for j in range(15):
            linha += " " + tab[i][j]                        # Acrescenta o tabuleiro recebido
        
        linha+=" |"
        
        tabuleiro.append(linha)
    
    tabuleiro.append("   +" + "-" * 31 + "+")               # Linha inferior da moldura

    resultado=""
    for k in range(len(tabuleiro)):
        
        if k < (len(tabuleiro) -1):
            resultado += tabuleiro[k] + "\n"
        
        else:
            resultado += tabuleiro[k]
    
    return resultado



def cria_jogador(ordem,pontos,conj_letras):
    """
    Função que cria um jogador de Scrabble

    Args:
        ordem (int): número do jogador (1 a 4)
        pontos (int): pontos iniciais
        conj_letras (dict): conjunto de letras do jogador

    Return:
        dict: jogador no formato {'id': ordem, 'pontos': pontos, 'letras': conj_letras}
    
    Raise:
        ValueError: se a ordem não for 1,2,3 ou 4
                    se os pontos não forem um número inteiro positivo
                    se o conjunto de letras recebido não for um dicionário
                    se alguma letra não estiver no abecedário português
                    se o número de occorências de uma letra não for inteiro maior que 0
                    se o jogador tiver mais de 7 letras
    """

    if not type(ordem) == int or ordem not in(1,2,3,4):
        raise ValueError("cria_jogador: argumentos inválidos")
    
    if not type(pontos) == int or pontos<0:
        raise ValueError("cria_jogador: argumentos inválidos")
    
    if not isinstance(conj_letras,dict):
        raise ValueError("cria_jogador: argumentos inválidos")
    
    total = 0
    for letra in conj_letras:
        occ = conj_letras[letra]
        
        if letra not in ABECEDARIO:
            raise ValueError("cria_jogador: argumentos inválidos")
        
        if not type(occ) == int or occ <= 0:
            raise ValueError("cria_jogador: argumentos inválidos")
        total += occ

    if total > 7:
        raise ValueError("cria_jogador: argumentos inválidos")
    
    return  {'id': ordem,'pontos': pontos ,'letras': conj_letras}



def jogador_para_str(jog):
    """
    Função que converte um jogador(dicionário) numa string legível

    Args:
        jog (dict): jogador {'id', 'pontos', 'letras'}

    Return:
        str: representação textual do jogador
    """
    letras = jog['letras']

    lista = []
    
    for letra in ABECEDARIO:    
        if letra in letras:
            for _ in range(letras[letra]):
                lista.append(letra)
  
    numero_de_pontos = str(jog['pontos'])
    
    if jog['pontos'] < 10:
            pontos = "  " + numero_de_pontos
   
    elif jog['pontos'] < 100:
            pontos = " " + numero_de_pontos
    
    else:
            pontos = numero_de_pontos           

    prefixo = '#'+str(jog['id'])+' ('+pontos+'): '
    res = prefixo
    for i in range(len(lista)):
        res += lista[i]
        if i < len(lista) - 1:
            res += " "
   
    return res



def distribui_letra(letras,jogador):
    """
    Função que retira a última letra da lista e adiciona-a ao conjunto de letras do jogador e retorna True, 
    se a lista tiver vazia devolve False

    Args:
        letras (list): lista de letras (pilha)
        jogador (dict): jogador {'id', 'pontos', 'letras'}

    Return:
        bool: True se uma letra foi atribuída, False se a lista estava vazia
    """

    if len(letras) == 0:
        return False
    
    letra = letras[-1]
    
    del letras[-1]
    
    if letra in jogador['letras']:
        jogador['letras'][letra] += 1
    else:
        jogador['letras'][letra] = 1

    return True



def joga_palavra(tab, palavra, casa, direcao ,conj_letras ,primeira):
    letras_usadas = ()
    linha, coluna = casa

    if direcao == 'H' and len(palavra) + coluna - 1 > 15:
        raise ValueError("...")
    
    if direcao == 'V' and len(palavra) + linha - 1 > 15:
        raise ValueError("...")
    
    if primeira and (linha != 8 or coluna != 8):
        return ()

    padrao = obtem_sequencia(tab, casa, direcao, len(palavra))
    letras_usadas = []

    if not primeira:
        toca_letra = False
        for i in range(len(palavra)):
            
            if palavra[i] == padrao[i]:
                toca_letra = True
                break

        if not toca_letra:
            return ()

    
    if testa_palavra_padrao(palavra, padrao, conj_letras):
        insere_palavra(tab, casa, direcao, palavra)
        
        letras_usadas = testa_palavra_padrao_auxiliar(palavra, padrao, conj_letras)
        letras_usadas = sorted(letras_usadas, key= lambda x: ABECEDARIO.index(x))
                
        return tuple(letras_usadas)
    
    else:
        return ()
    

def processa_jogada(tab, jog, pilha, pontos, primeira):
    while True:
        jogada = input("Jogada J" + str(jog['id']) + ": ")
        jogada_recebida = jogada.split()
        
        if jogada_recebida[0] == 'P':
            return False

        elif jogada_recebida[0] == 'T':
            if processa_troca(jogada_recebida, jog, pilha):
                return True
            else:
                return False

        elif jogada_recebida[0] == 'J':
            if jogar(tab, jog, pilha, jogada_recebida, primeira):
                return True
            else:
                return False

def processa_troca(jogada_recebida, jog, pilha):
#converter a sequencia numa lista(.split())
#validar input(se jogador tem as letras)
#tirar do conjunto de letras as letras da sequencia
#adiciona da lista de letras as ultimas
#isto se estiverem pelo menos 7 letras no saco
#se for valida retorna true
    troca_valida = True
    letras_para_troca = jogada_recebida[1:]
    
    for letra in letras_para_troca:
        if letra not in jog['letras'] or jog['letras'][letra] < letras_para_troca.count(letra):
            troca_valida = False
    
    if troca_valida and len(pilha) >= 7:
        for l in letras_para_troca:
            jog['letras'][l] -=1
            if jog['letras'][l] == 0:
                del jog['letras'][l]
    
        letras_novas = []
        for i in range(len(letras_para_troca)):
            letras_novas.append(pilha[-1])
            del pilha[-1]
        for letra_nova in letras_novas:
            if letra_nova not in jog['letras']:
                jog['letras'][letra_nova] = jog['letras'].get(letra_nova ,0) + 1
            else:
                jog['letras'][letra_nova] += 1
        return True
    return False



def jogar(tab, jog, pilha, jogada_recebida, primeira):
    #usar funcao joga palavra para saber se e valida
    #se a jogada for valida devolve true e atualiza os pontos do jogador e retira as letras usadas
    linha = jogada_recebida[1]
    coluna = jogada_recebida[2]
    casa = cria_casa(linha, coluna)
    direcao = jogada_recebida[3]
    palavra = jogada_recebida[4:]
    letras_usadas = list(joga_palavra(tab, palavra, casa, direcao, jog['letras'], primeira))

    if len(letras_usadas) == 0:
        return False
    for l in letras_usadas:
        jog['letras'][l] -=1
        if jog['letras'][l] == 0:
            del jog['letras'][l]
    letras_novas = []
    
    for i in range(len(letras_usadas)):
        letras_novas.append(pilha[-1])
        del pilha[-1]
    
    for letra_nova in letras_novas:
        if letra_nova not in jog['letras']:
            jog['letras'][letra_nova] = jog['letras'].get(letra_nova ,0) + 1
        else:
            jog['letras'][letra_nova] += 1
    
    jog['pontos'] += pontuar_lista_de_letras(letras_usadas)
    
    return True

def pontuar_lista_de_letras(lista_de_letras):
    pontuacao = 0
    for letra in lista_de_letras:
        pontuacao += PONTOS[letra]
    return pontuacao

""""
def scrable():
    # baralha letras
    # distribui letras por jogadores
    # ... (Duarte continua!)
"""