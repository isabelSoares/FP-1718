#Palavra Guru Multi Jogador
#Projeto parte 2
#Isabel Soares, 89466

from parte1 import e_palavra
import itertools

def num_letras(cad):
    """
    Recebe um 'cad' como cadeira de carateres ou tuplo e retorna um dicionario 
    cujas as chaves sao as letras e os valores sao numeros correspondentes a 
    essas chaves.
    """
    dic = {} 
    for c in cad:
        if c in dic:
            dic[c] = dic[c] + 1
        else:
            dic[c] = 1
    return dic 


def cria_palavra_potencial(cad, conjunto):
    """
    Recebe um 'cad' como cadeira de carateres e um 'conjunto' como tuplo e 
    retorna uma palavra potencial.
    cria_palavra_potencial: cad.carateres x tuplo de letras ---> palavra_potencial
    """      
    if isinstance(cad, str) and isinstance(conjunto, tuple):
        for l in conjunto + tuple(cad):
            if not ('A' <= l <= 'Z'):
                #verifica se ha letras maiusculas no conjunto
                raise ValueError('cria_palavra_potencial:argumentos invalidos.')
    else:
        raise ValueError('cria_palavra_potencial:argumentos invalidos.')

    contagem_cad = num_letras(cad)
    contagem_conjunto = num_letras(conjunto)
    
    for l in contagem_cad:
        if l not in contagem_conjunto or contagem_cad[l] > contagem_conjunto[l]:
            #se a letra nao esta no conjunto e se a cadeia de carateres contenha mais 
            #letras existentes no conjunto de letras em jogo, ou letras ou letras 
            #diferentes daquelas            
            raise ValueError('cria_palavra_potencial:a palavra nao e valida.')
    return [cad, conjunto]

def palavra_tamanho(pal):
    """
    Recebe um 'pal' como palavra potencial e retorna o seu tamanho.
    palavra_tamanho: palavra_potencial---> inteiro
    """ 
    return len(pal[0])

def e_palavra_potencial(arg):
    """
    Recebe um argumento e verifica se e do tipo palavra_potencial, retornando
    o valor logico dessa comparacao.
    e_palavra_potencial: universal ---> logico
    """      
    return isinstance(arg, list) and len(arg) == 2 and \
           isinstance(arg[0], str) and isinstance(arg[1], tuple)
    
def palavras_potenciais_iguais(pal1,pal2):
    """
    Recebe dois argumentos do tipo palavra_potencial e verifica se sao iguais,
    retornando o valor logico dessa comparacao.
    palavras_potenciais_iguais: palavra_potencial x palavra_potencial---> logico
    """     
    return pal1[0] == pal2[0]
    
def palavra_potencial_menor(pal1,pal2):
    """
    Recebe dois argumentos do tipo palavra_potencial e verifica se o primeiro 
    argumentorepresenta uma palavra alfabeticamente anterior a palavra
    representada pelo segundo argumento, retornando o valor logico 
    dessa comparacao.
    palavra_potencial_menor: palavra_potencial x palavra_potencial---> logico
    """    
    return pal1[0] < pal2[0]

def palavra_potencial_para_cadeia(pal):
    """
    Recebe um argumento do tipo palavra_potencial, retornando uma cadeira de 
    carateres que corresponde a essa palavra.
    palavra_potencial_para_cadeia: palavra_potencial ---> cad.carateres
    """  
    return pal[0]

def cria_conjunto_palavras():
    """
    Recebe um 'conjunto_pal' como lista e retorna um conjunto de palavras.
    ---> conjunto_palavras
    """     
    return {}

def numero_palavras(conjunto_pal):
    """
    Recebe um 'conjunto_pal' como conjunto_palavras e retorna o seu tamanho.
    numero_palavras: conjunto_palavras ---> inteiro
    """
    contador = 0
    for tamanho in conjunto_pal:
        contador = contador + len(conjunto_pal[tamanho])
    return contador

def subconjunto_por_tamanho(conjunto_pal,n):
    """
    Recebe um 'conjunto_pal' como conjunto_palavras e um inteiro 'n' e retorna 
    uma lista com as palavras_potenciais de tamanho n contidas no conjunto de 
    palavras.
    subconjunto_por_tamanho: conjunto_palavras x inteiro ---> lista
    """  
    if n in conjunto_pal:
        return conjunto_pal[n]
    else:
        return []     

def acrescenta_palavra(conjunto_pal,pal):
    """
    Recebe um 'conjunto_pal' como conjunto_palavras e um 'pal' como 
    palavra_potencial e junta a palavra ao conjunto de palavras, caso esta ainda 
    nao pertenca ao conjunto.
    acrescenta_palavra: conjunto_palavras x palavra_potencial ---> 
    """
    if e_conjunto_palavras(conjunto_pal) and e_palavra_potencial(pal):
        c = palavra_tamanho(pal)
        sub = subconjunto_por_tamanho(conjunto_pal, c)
        esta_no_conj = False
        for p in sub:
            #percorre o subconjunto e verifica se esta no subconjunto
            if palavra_potencial_para_cadeia(p) == palavra_potencial_para_cadeia(pal):
                esta_no_conj = True
        if not esta_no_conj:
            #se a palavra nao estiver no conjunto e adicionada
            if c in conjunto_pal:
                #se o tamanho da palavra for uma chave do dicionario
                conjunto_pal[c].append(pal) 
            else:
                conjunto_pal[c] = [pal]                
    else:
        raise ValueError('acrescenta_palavra:argumentos invalidos.')

def e_conjunto_palavras(arg):
    """
    Recebe um argumento e verifica se e do tipo conjunto_palavras, retornando
    o valor logico dessa comparacao.
    e_conjunto_palavras: universal ---> logico
    """      
    if isinstance(arg,dict):
        for key in arg:
            if not (isinstance(key, int) and isinstance(arg[key], list)):
                return False 
        return True  
    else:
        return False    
    
def conjuntos_palavras_iguais(conjunto_pal1,conjunto_pal2):
    """
    Recebe dois argumentos do tipo conjunto_palavras e verifica se ambos conterem 
    as mesmas palavras, retornando o valor logico dessa comparacao.
    conjuntos_palavras_iguais: conjunto_palavras x conjunto_palavras---> logico
    """    
    return conjunto_pal1 == conjunto_pal2 

def conjunto_palavras_para_cadeia(conj):
    """
    Recebe um 'conj' como conjunto_palavras retornando uma cadeia de carateres 
    que o represente. As palavras sao representadas por ordem crescente e por
    cada tamanho sao ordenadas alfabeticamente.
    conjunto_palavras_para_cadeia: conjunto_palavras ---> cad. carateres
    """    
    cc = ''
    
    tamanhos = list(conj.keys()) 
    # lista que contem todas chaves correspondentes 
    # a diferentes tamanhos do conjunto_palavras
    tamanhos.sort()
    #ordena por tamanho cada palavra
    
    for tamanho in tamanhos:
        string = str(tamanho) + '->['
        lista = []
        
        for pal in conj[tamanho]:
            lista.append(palavra_potencial_para_cadeia(pal)) 
            #adiciona a palavra_potencial_para_cadeia a ultima posicao da lista
        lista.sort()
        for e in lista:
            string = string + e +', '
        
        string = string[0:-2] + ']'
        cc = cc + string + ';'
        
    return '[' + cc[0:-1] + ']'
    
def cria_jogador(nome):
    """
    Recebe uma cadeia de carateres correspondente ao nome do jogador, retornando
    um elemento do tipo 'jogador'.
    cria_jogador: cad. carateres ---> jogador
    """    
    if isinstance(nome, str):
        return [nome, 0, cria_conjunto_palavras(), cria_conjunto_palavras()]
    else:
        raise ValueError('cria_jogador:argumento invalido.')

def jogador_nome(jogador):
    """
    Recebe um elemento do tipo 'jogador' , retornando o nome do jogador.
    jogador_nome: jogador ---> cad. carateres
    """         
    return jogador[0]

def jogador_pontuacao(jogador):
    """
    Recebe um elemento do tipo 'jogador' , retornando a pontuacao obtida pelo 
    jogador ate esse momento.
    jogador_pontuacao: jogador ---> inteiro
    """    
    return jogador[1]

def jogador_palavras_validas(jogador):
    """
    Recebe um elemento do tipo 'jogador', retornando um conjunto de palavras 
    validas sugeridas pelo jogador ate esse momento.
    jogador_palavras_validas: jogador ---> conjunto_palavras
    """       
    return jogador[2]

def jogador_palavras_invalidas(jogador):
    """
    Recebe um elemento do tipo 'jogador', retornando um conjunto de palavras 
    invalidas sugeridas pelo jogador ate esse momento.
    jogador_palavras_invalidas: jogador ---> conjunto_palavras
    """   
    return jogador[3]

def adiciona_palavra_valida(jogador, p):
    """
    Recebe um  elemento do tipo 'jogador' e um 'p' como palavra_potencial, e tem 
    como objetivo adicionar a palavra p ao conjunto de palavras validas sugeridas 
    pelo jogador, atualizando, convenientemente, a pontuacao do jogador.
    adiciona_palavra_valida: jogador x palavra_potencial ---> 
    """    
    if e_jogador(jogador) and e_palavra_potencial(p):
        if not p in subconjunto_por_tamanho(jogador[2], palavra_tamanho(p)): 
            acrescenta_palavra(jogador[2],p)
            jogador[1] = jogador[1] + palavra_tamanho(p)
    else:
        raise ValueError('adiciona_palavra_valida:argumentos invalidos.')
    
def adiciona_palavra_invalida(jogador, p):
    """
    Recebe um  elemento do tipo 'jogador' e um 'p' como palavra_potencial, e tem 
    como objetivo adicionar a palavra p ao conjunto de palavras invalidas sugeridas 
    pelo jogador, atualizando, convenientemente, a pontuacao do jogador.
    adiciona_palavra_invalida: jogador x palavra_potencial ---> 
    """  
    if e_jogador(jogador) and e_palavra_potencial(p):
        if not p in subconjunto_por_tamanho(jogador[3], palavra_tamanho(p)): 
                acrescenta_palavra(jogador[3],p)
                jogador[1] = jogador[1] - palavra_tamanho(p)
    else:
        raise ValueError('adiciona_palavra_invalida:argumentos invalidos.') 
    
def e_jogador(arg):
    """
    Recebe um argumento e verifica se e do tipo jogador, retornando
    o valor logico dessa comparacao.
    e_jogador: universal ---> logico
    """       
    return isinstance (arg,list) and len(arg) == 4 and \
       isinstance(arg[0], str) and isinstance(arg[1], int) and \
       e_conjunto_palavras(arg[2]) and e_conjunto_palavras(arg[3])


def jogador_para_cadeia(jogador):
    """
    Recebe um argumento do tipo jogador, retornando uma cadeia de carateres que 
    o represente.Cada jogador e descrito pelo seu nome, seguida pela pontuacao 
    obtida e pelos conjuntos de palavras validas e invalidas.
    jogador_para_cadeia: jogador ---> cad. carateres
    """     
    return 'JOGADOR ' + jogador_nome(jogador) + \
           ' PONTOS=' + str(jogador_pontuacao(jogador)) + \
           ' VALIDAS=' + conjunto_palavras_para_cadeia(jogador_palavras_validas \
                                                       (jogador)) + \
           ' INVALIDAS=' + conjunto_palavras_para_cadeia(jogador_palavras_invalidas \
                                                         (jogador))

def gera_todas_palavras_validas(tuplo):
    """
    Recebe um 'tuplo' como argumento, de modo a formar palavras e retorna um 
    conjunto de palavras, que contem todas as palavras geradas a partir das 
    letras dadas e subconjuntos das mesmas, que sao validas segundo esta gramatica
    gera_todas_palavras_validas: tuplo de letras ---> conjunto_palavras
    """
    conjunto_pal = cria_conjunto_palavras() 
    for i in range(len(tuplo) + 1):
        for subset in itertools.permutations(tuplo, i):
            #ciclo para verificar todas possiveis palavras que se podem formar 
            #a partir do tuplo de letras usando permutacoes de letras
            cadeia = ''
            for l in subset:
                cadeia = cadeia + l
            if e_palavra(cadeia):
                acrescenta_palavra(conjunto_pal, cria_palavra_potencial \
                                   (cadeia,tuplo))
                #se a palavra for valida e ainda nao se encontra no conjunto de
                #palavras validas e adicionada a esse conjunto
    return conjunto_pal

def guru_mj(tuplo):
    """
    Funcao principal do jogo.Recebe um 'tuplo' de letras como argumento e que 
    corresponde ao conjunto de letras a usar para formar as palavras. 
    O 'tuplo' de letras apresenta, tambem, o jogador vencedor ou a indicacao 
    de empate, caso exista mais do que um jogador com a melhor pontuacao.
    tuplo de letras --->
    """
    print('Descubra todas as palavras geradas a partir das letras:')
    print(tuplo)
    pal_validas = gera_todas_palavras_validas(tuplo)
    n = numero_palavras(pal_validas)
    print('Introduza o nome dos jogadores (-1 para terminar)...')
    contador = 1
    nome = ''
    list_jog = []
    while nome != '-1':
        texto ='JOGADOR '+ str(contador) + ' -> '
        nome = input(texto)
        if nome != '-1':
            list_jog = list_jog + [cria_jogador(nome)]
            #lista onde sao guardados os nomes dos jogadores
            contador = contador + 1
    
    k = 1
    list_jogadas_validas = []
    while n != 0 :
        jogador = list_jog[(k-1) % len(list_jog)]
        texto1 = 'JOGADA ' + str(k) + ' - Falta descobrir ' + str(n) +' palavras' 
        print(texto1)
        texto2 = 'JOGADOR ' + jogador_nome(jogador) + ' -> '
        #atraves da formula,consegue se saber que jogador esta a jogar a partir 
        #do numero da jogada
        jogada = cria_palavra_potencial(input(texto2), tuplo)
        if jogada in subconjunto_por_tamanho(pal_validas, \
                                             palavra_tamanho(jogada)):
            print(palavra_potencial_para_cadeia(jogada),'- palavra VALIDA')
            if palavra_potencial_para_cadeia(jogada) not in list_jogadas_validas:
                list_jogadas_validas.append(palavra_potencial_para_cadeia(jogada))
                adiciona_palavra_valida(jogador,jogada)
                n = n - 1
        else:
            print(palavra_potencial_para_cadeia(jogada),'- palavra INVALIDA')
            adiciona_palavra_invalida(jogador,jogada)       
        k = k + 1
    
    pontuacao_max =  jogador_pontuacao(list_jog[0])
    jogador_vencedor = list()
    for jogador in list_jog:
        pontuacao = jogador_pontuacao(jogador)
        if pontuacao > pontuacao_max:
            #se a pontuacao do jogador for superior a pontuacao maxima ate 
            #esse momento
            pontuacao_max = pontuacao
            jogador_vencedor = [jogador]
            #o nome do jogador e adicionada a uma lista que contem os vencedores 
        elif pontuacao == pontuacao_max:
            #se a pontuacao for igual a pontuacao maxima
            jogador_vencedor = jogador_vencedor + [jogador]
            #havera mais do que um vencedor e junta a lista dos vencedores
        
    if len(jogador_vencedor) > 1:
        print('FIM DE JOGO! O jogo terminou em empate.')
    else:
        print('FIM DE JOGO! O jogo terminou com a vitoria do jogador ' +\
                jogador_nome(jogador_vencedor[0]) + ' com ' +\
                str(jogador_pontuacao(jogador_vencedor[0])) + ' pontos.')       
            
    for jogador in list_jog:
        print(jogador_para_cadeia(jogador))