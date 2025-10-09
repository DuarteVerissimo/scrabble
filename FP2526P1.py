# This is the Python script for your project

ABECEDARIO = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O',
                  'P','Q','R','S','T','U','V','X','Z')

pontos = {  
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
                    se alguma das letras do tuplo 'let' é repetida
                    se o número de occorências de uma letra não for inteiro maior que 0
    """
    if not isinstance(let, tuple) or not isinstance(occ, tuple):
        raise ValueError("cria_conjunto: argumentos inválidos")
    
    if len(let) != len(occ):
        raise ValueError("cria_conjunto: argumentos inválidos")
    
    letras_vistas = []
    d = {}
    for i in range(len(let)):
        letra = let[i]
        numero = occ[i]

        if not isinstance(letra, str) or len(letra) != 1:
            raise ValueError("cria_conjunto: argumentos inválidos")
        letra = letra.upper()
        
        if letra not in ABECEDARIO:
            raise ValueError("cria_conjunto: argumentos inválidos")

        if letra in letras_vistas:
            raise ValueError("cria_conjunto: argumentos inválidos")
        letras_vistas += letra
        
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
    for letra in ABECEDARIO:
        if letra in conj:
            lista_letras.extend([letra] * conj[letra])
    
    permuta_letras(lista_letras, estado)
    
    return lista_letras



def testa_palavra_padrao(palavra, padrao, conj):
    """
    Função que verifica, usando a função auxiliar testa_palavra_padrao_auxiliar, se é possível formar uma 
    palavra substituindo os '.' e as letras do padrão por letras contidas no conjunto de letras

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
    """
    Função auxiliar que caso seja possível substituir uma palavra num padrão, que contem '.' e letras,
    por letras contidas num conjunto de letras devolve uma lista com as letras usadas. Caso contrário,
    devolve uma lista vazia

    Args:
        palavra (str): palavra que se pretende escrever
        padrao (str): string do mesmo comprimento que a palavra, composta por letras e '.'
        conj (dict): dicionário de letras de formato {letra: ocorrências}

    Return:
        list: lista vazia caso não dê para substituir a palavra no padrão ou então devolve uma lista 
              que contém as letras substituidas no padrão
    """
    if len(palavra) != len(padrao):
        return []
    
    ocorrencias = conj.copy()
    letras_usadas = []
    for i in range(len(palavra)):
        letra_palavra = palavra[i]
        letra_padrao = padrao[i]
        
        if letra_padrao == '.': 

            # Verificar se a letra está no cojunto e se existem occorrencias suficientes para usar
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
        list: lista de 15 listas, cada uma com 15 elementos
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
        tuplo: (l, c) representando a casa

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



def cria_jogador(ordem, pontos, conj_letras):
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
        jog (dict): dicionário que representa o jogador {'id', 'pontos', 'letras'}

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
    """"
    Função que, se não sair do tabuleiro e respeitar as regras do jogo, forma uma palavra no tabuleiro
    com um conjunto de letras e devolve um tuplo com as letras usadas por ordem alfabética. Caso não 
    consiga jogar a palavra devolve um tuplo vazio

    Args:
        tab (list): tabuleiro 15x15
        palavra (str): palavra a inserir        
        casa (tuple): (linha, coluna), entre 1 e 15
        direcao (str): 'H' para horizontal ou 'V' para vertical
        conj_letras (dict): conjunto de letras do jogador
        primeira (bool): boleano que identifica se é a primeira jogada

    Return:
        tuplo: tuplo com as letras usadas por ordem alfabética. Caso contrário,
               devolve um tuplo vazio

    """
    letras_usadas = ()
    linha, coluna = casa
    
    if primeira:
        for i in range(len(palavra)):
            if direcao == 'H' and (linha, coluna + i) == (8, 8):
                break
            if direcao == 'V' and (linha + i, coluna) == (8, 8):
                break
        else:
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
    """"
    Função que processa o turno completo de um jogador, até ele inserir uma jogada válida. Recebe um input com a 
    jogada desejada pelo jogador, se for 'P' passa e devolve False, se for 'T <seq_letras>' devolve True e altera
    o conjunto de letras e a pilha e se for 'J <linha> <coluna> <dir> <palavra>' joga uma palavra, atualiza o 
    tabuleiro, o conjunto de letras do jogador, a sua pontuação e pilha
    
    Args:
        tab (list): tabuleiro de jogo 15x15
        jog (dict): dicionário que representa o jogador
        pilha (list): lista de letras disponíveis (saco)
        pontos (dict): dicionário com as pontuações de cada letra
        primeira (bool): True se for a primeira jogada do jogo

    Return:
        bool: True se a jogada for válida, False caso contrário
    """
    while True:
        jogada = input("Jogada J" + str(jog['id']) + ": ")
        jogada_recebida = jogada.split()
        
        if jogada_recebida[0] == 'P':
            if len(jogada_recebida ) == 1:
                return False

        elif jogada_recebida[0] == 'T':
            try:
                if len(jogada_recebida) > 1 and processa_troca(jogada_recebida, jog, pilha):
                    return True
            except:
                continue
        
        elif jogada_recebida[0] == 'J':
            try:
                if type(jogada_recebida[1]) != int or type(jogada_recebida[2]) != int:
                    continue
                if len(jogada_recebida) == 5 and jogar(tab, jog, pilha, jogada_recebida, primeira):
                    return True
            except:
                continue



def processa_troca(jogada_recebida, jog, pilha):
    """
    Função auxiliar que caso o jogador decida trocar as letras do seu conjunto('T'), troca as letras escolhidas
    pelas as ultimas da pilha

    Args:
        jogada_recebida (list): lista que contem o input com as informações necessárias
        jog (dict): dicionário que representa o jogador {'id', 'pontos', 'letras'}
        pilha (list): lista de letras disponíveis (saco)

    Return:
        bool: retorna True caso a jogada seja válida e False caso seja inválida
    """
    letras_para_troca = jogada_recebida[1:]
    
    for letra in letras_para_troca:
        if letra not in jog['letras'] or jog['letras'][letra] < letras_para_troca.count(letra):
            return False
    
    if len(pilha) >= 7:
        for l in letras_para_troca:
            jog['letras'][l] -=1
            if jog['letras'][l] == 0:
                del jog['letras'][l]
            
            distribui_letra(pilha, jog)
        return True

    return False



def jogar(tab, jog, pilha, jogada_recebida, primeira):
    """
    Função auxiliar que caso o jogador decida jogar('J') e a jogada seja válida, insere a palavra no tabuleiro,
    atualiza o conunto de letras do jogador e atualiza também a pontuação do jogador

    Args:
        tab (list): tabuleiro 15x15
        jog (dict): dicionário que representa o jogador {'id', 'pontos', 'letras'}
        pilha (list): lista de letras disponíveis (saco)
        jogada_recebida (list): lista que contem o input com as informações necessárias
        primeira (bool): bool que identifica se é a primeira jogada

    Return:
        bool: retorna True caso a jogada seja válida e False caso seja inválida
    """
    linha = int(jogada_recebida[1])
    coluna = int(jogada_recebida[2])
    casa = cria_casa(linha, coluna)
    direcao = jogada_recebida[3]
    palavra = jogada_recebida[4]
    letras_usadas = list(joga_palavra(tab, palavra, casa, direcao, jog['letras'], primeira))

    if len(letras_usadas) == 0 :
        return False
    
    for l in letras_usadas:
        jog['letras'][l] -=1
        if jog['letras'][l] == 0:
            del jog['letras'][l]
        
        distribui_letra(pilha, jog)
    palavra = list(palavra)

    jog['pontos'] += pontuar_lista_de_letras(palavra)
    
    return True



def pontuar_lista_de_letras(lista_de_letras):
    """"
    Função auxiliar que recebe uma lista de letras e determina a pontução dela

    Args:
        lista_de_letras (list): lista de letras

    Return:
        int: pontuação total das letras dessa lista
    """
    pontuacao = 0
    for letra in lista_de_letras:
        pontuacao += pontos[letra]
    return pontuacao



def scrabble(jogadores, saco, pontos, estado):
    """"
    Função principal que permite jogar o jogo com 2 a 4 jogadores    
    Args:
        jogadores (int): número de jogadores no jogo
        saco (dict): conjunto de todas as letras do jogo
        pontos (dict): dicionário com as pontuações de cada letra
        estado (int): estado do gera_numeros_aleatorios

    Return:
        tuplo: devolve um tuplo com as pontuações dos jogadores

    Raise:
        ValueError: se o número de jogadores não for inteiro ou não for igual a 2,3 ou 4
                    se o estado não for inteiro positivo
    """
    print("Bem-vindo ao SCRABBLE.")
    tab=cria_tabuleiro()
    
    if len(saco)==0:
        raise ValueError('scrabble: argumentos inválidos')
    if type(jogadores) != int or jogadores not in(2, 3, 4):
        raise ValueError('scrabble: argumentos inválidos')
    if type(estado) != int or estado < 0:
        raise ValueError('scrabble: argumentos inválidos')
    for letra in ABECEDARIO:
        if letra not in pontos:
            raise ValueError('scrabble: argumentos inválidos')

    pilha = baralha_conjunto(saco, estado)
    
    lista_jogadores = []
    # Distribuir 7 peças por cada jogador
    for i in range(1, jogadores + 1):
            jog=cria_jogador(i, 0, {})
            for _ in range(7):
                distribui_letra(pilha, jog)
            lista_jogadores.append(jog)
    
    # Ciclo de jogadas depois da primeiras
    passagens_seguidas = 0
    jogo_continua = True
    primeira = True
    while jogo_continua:
        for jog in lista_jogadores:
            print(tabuleiro_para_str(tab))
            for j in range(jogadores):
                print(jogador_para_str(lista_jogadores[j]))
            
            res = processa_jogada(tab, jog, pilha, pontos, primeira)
            
            if primeira == True:
                primeira = False

            if res == False:
                passagens_seguidas += 1
            else:
                passagens_seguidas = 0

            if passagens_seguidas== jogadores:
                jogo_continua = False
        
            if jog['letras'] =={} and pilha == []:
                jogo_continua = False
                break
    
    return tuple(jog['pontos'] for jog in lista_jogadores)