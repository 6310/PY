#import LEXICO TODO
#import re
arqfinalteste='arqfinalteste.txt'
pikatoken

def prog():
    t = open(arqfinalteste,'r')
    global pikatoken = t.split()
    i=0
    if(DECL_VAR()):
        if(COMANDOS()):
            return True

    elif(COMANDOS()):
        return True
    return False


def DECL_VAR():
    if("var"):
        if(LISTA_TIPOS()):
            #AAAAAAAAAAAAAAAAAAAAAAAA
            return True
    return False

def LISTA_TIPOS():
    if("int"):
        if(ESTRUTURA_VAR())
            return True
    elif("real"):
        if(ESTRUTURA_VAR()):
            return True
    elif(LISTA_TIPOS());

def ESTRUTURA_VAR():
    if("var"):
        if("ponto_virgula"):
            return True;


        elif("virgula"):
                LISTA_TIPOS())
def COM_WHILE():
    if(LEX("while")):
        if (LEX("(")):
            return True
        return False
    return False




def COMANDOS():
    if(COM_IF()):
        if(COMANDOS()):
            return True


def COM_IF():
    if(LEX("if")):
        if(LEX("(")):
            if(EXP_REL())


def sintatico(tokens):
    if prog():
        print "OK"
    print "NAO"


def parser():
    input = read(arg)
    tokens = lexico(input)
    sintatico(tokens)
