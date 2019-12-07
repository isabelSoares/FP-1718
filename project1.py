#Primeiro projeto 
#Palavra Guru  
#Isabel Soares, 89466


def artigo_def(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um artigo definido segundo a gramatica.
    """
    return x== 'A' or x== 'O'

def vogal_palavra(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma vogal palavra segundo a gramatica.
    """    
    return artigo_def(x) or x=='E'

def vogal(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma vogal segundo a gramatica.
    """        
    return x=='I' or x=='U' or vogal_palavra(x)

def ditongo_palavra (x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um ditongo palavra segundo a gramatica.
    """        
    return x=='AI' or x=='AO' or x=='EU' or x=='OU'

def ditongo (x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um ditongo segundo a gramatica.
    """        
    return x=='AE' or x=='AU' or x=='EI' or x=='OE' or x=='OI' or x=='IU' or ditongo_palavra(x) 

def par_vogais (x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um par de vogais segundo a gramatica.
    """        
    return ditongo(x) or x=='IA' or x=='IO'

def consoante_freq (x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma consoante frequente segundo a gramatica.
    """        
    lst1=['D','L','M','N','P','R','S','T','V']
    for i in range(len(lst1)):
        if x== lst1[i]:
            return True 
    return False

def consoante_terminal (x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma consoante terminal segundo a gramatica.
    """        
    lst1=['L','M','R','S','X','Z']
    for i in range(len(lst1)):
        if x==lst1[i]:
            return True
    return False 

def consoante_final (x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma consoante final segundo a gramatica.
    """        
    return x=='N' or x=='P' or consoante_terminal(x)

def consoante (x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma consoante segundo a gramatica.
    """        
    lst1=['B','C','D','F','G','H','J','L','M','N','P','Q','R','S','T','V','X','Z']        
    for i in range(len(lst1)):
        if x==lst1[i]:
            return True
    return False
    
def par_consoantes(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um par de consoantes segundo a gramatica.
    """        
    if x[1] == 'R':#se o segundo carater for 'R' 
        lst1 = ['B', 'C', 'F', 'G', 'P', 'T', 'V']
        for i in range(len(lst1)): 
            #percorre a lista 1 ate encontrar uma letra dessa lista que seja igual ao 
            #primeiro carater
            if x[0] == lst1[i]:
                return True
    elif x[1] =='L':#se o segundo carater for 'L' 
        lst2 = ['B', 'C', 'F', 'G', 'P']
        for i in range(len(lst2)):
             #percorre a lista 1 ate encontrar uma letra dessa lista que seja igual ao 
            #primeiro carater
            if x[0] == lst2[i]:
                return True
    return False

def monossilabo_2(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um monossilabo com 2 carateres segundo a gramatica.
    """        
    if (x=='AR'or x=='IR'or x=='EM'or x=='UM' or ditongo_palavra(x)) or \
       (x[1] == 'S' and vogal_palavra(x[0])) or \
       (consoante_freq(x[0]) and vogal(x[1])):
        return True 
    return False
    
def monossilabo_3(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um monossilabo com 3 carateres segundo a gramatica.
    """            
    if (consoante(x[0]) and vogal(x[1]) and consoante_terminal(x[2])) or \
       (consoante(x[0]) and ditongo(x[1:])) or \
       (par_vogais(x[0:2]) and consoante_terminal(x[2])):
        return True
    return False

def e_monossilabo(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser um monossilabo segundo a gramatica.
    """            
    if not isinstance(x,str):
        raise ValueError('e_monossilabo:argumento invalido')
    elif (len(x) == 1):#se o monossilabo for constituido por 1 letra
        return vogal_palavra(x) 
    elif (len(x) == 2):#se o monossilabo for constituido por 2 letras
        return monossilabo_2(x) 
    elif (len(x) == 3):#se o monossilabo for constituido por 3 letras
        return monossilabo_3(x)
    else: 
        return False

def silaba_2(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma silaba com 2 carateres segundo a gramatica.
    """            
    if (par_vogais(x)) or \
       (consoante(x[0]) and vogal(x[1])) or \
       (vogal(x[0]) and consoante_final(x[1])):
        return True
    return False

def silaba_3(x):  
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma silaba com 3 carateres segundo a gramatica.
    """               
    lst1=['QUA','QUE','QUI','GUE','GUI']
    for i in range(len(lst1)):
        if x==lst1[i]:
            return True

    if (vogal(x[0]) and x[1:] =='NS') or \
       (consoante(x[0]) and par_vogais(x[1:3])) or \
       (consoante(x[0]) and vogal(x[1]) and consoante_final(x[2])) or \
       (par_vogais(x[0:2]) and consoante_final(x[2])) or \
       (par_consoantes(x[0:2]) and vogal(x[2])):
        return True
    return False

def silaba_4(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma silaba com 4 carateres segundo a gramatica.
    """               
    if (par_vogais(x[0:2]) and x[2:]=='NS') or \
       (par_consoantes(x[0:2]) and par_vogais(x[2:4])) or \
       (consoante(x[0]) and par_vogais(x[1:3]) and consoante_final(x[3])):
        return True
    elif consoante(x[0]) and vogal(x[1]):
        lst1 = ['NS','IS']
        for i in range(len(lst1)):
            if x[2:4] == lst1[i]:
                return True    
    return False 

def silaba_5(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma silaba com 5 carateres segundo a gramatica.
    """               
    return par_consoantes(x[0:2]) and vogal(x[2]) and x[3:]=='NS'

def silaba_final(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma silaba final segundo a gramatica.
    """               
    if (len(x)==2):#se a silaba final for constituida por 2 letras
        return monossilabo_2(x) 
    elif (len(x)==3):#se a silaba final for constituida por 3 letras
        return monossilabo_3(x)
    elif(len(x)==4):#se a silaba final for constituida por 4 letras
        return silaba_4(x)
    elif (len(x)==5):#se a silaba final for constituida por 5 letras
        return silaba_5(x)
    else:
        return False 

def e_silaba(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma silaba segundo a gramatica.
    """           
    if not isinstance(x,str):
        raise ValueError('e_silaba:argumento invalido')    
    elif (len(x) == 1):#se a silaba for constituida por 1 letra
        return vogal(x)
    elif (len(x) == 2):#se a silaba for constituida por 2 letras
        return silaba_2(x) 
    elif (len(x) == 3):#se a silaba for constituida por 3 letras
        return silaba_3(x) 
    elif(len(x) == 4):#se a silaba for constituida por 4 letras
        return silaba_4(x) 
    elif (len(x) == 5):#se a silaba for constituida por 5 letras
        return silaba_5(x)
    else: 
        return False
    
def e_palavra(x):
    """
    Recebe um 'x' como cadeira de carateres e retorna o valor logico resultante 
    da verificacao de 'x' ser uma palavra segundo a gramatica.
    """           
    if not isinstance(x,str):
        raise ValueError('e_palavra:argumento invalido')
    
    def silaba_aux(x):        
        if e_silaba(x):#se for uma silaba
            return True
        
        for i in range(0, min(5, len(x)) + 1):#percorre os 5 primeiros carateres
            if e_silaba(x[0:i]):#confirma se todos esses carateres podem ser uma
                #silaba
                if silaba_aux(x[i:]):
                    return True
        
        return False
    
    if e_monossilabo(x) or silaba_final(x):#se a cadeira de carateres
       #corresponder a um monossilabo ou a uma silaba final
        return True

    lst1 = []
    for i in range(2, min(5, len(x)) + 1):#percorre todos os tamanhos da cadeia
        #de carateres possiveis
        if silaba_final(x[len(x)-i:]):#se a silaba tem o mesmo tamanho
        #da silaba final
            lst1 = lst1 + [i]
            
    if lst1 == []:#se nao encontrar uma silaba com o tamanho da silaba final 
        return False
    else:
        for i in lst1: 
            if silaba_aux(x[0:len(x)-i]):#a silaba aux percorre da primeira
            #letra ate ao inicio da silaba final,tendo em conta so os carateres
            #que nao sejam silaba final
                return True 
        return False
                
        