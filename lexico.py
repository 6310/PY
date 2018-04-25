#Tokens
# Delimitadores: '(', ')', '.', '\n', '\t', '\r', ' ', '{', '}', '[', ']', ';';
# Números: [0-9];
# Letras maiúsculas: [A-Z];
# Letras minúsculas: [a-z];
# Identificadores: palavras formadas por Letras maiúsculas e minúsculas;
# Operadores aritméticos: '+', '-', '*', '/', '^', cada operador precisa de um identificador
# Operadores Relacionais: '>', '>=', '<', '<=', '==', '<>',
# Atribuição: '=';
# Palavras reservadas: 'var', 'int', 'real', 'while', 'if', 'else', '', '', ;

#Tokens ID
# Delimitadores = DELIM
# Números = NUM
# Letras maiúsculas = LETM
# Letras minúsculas = LETMIN
# Identificadores = IDENT
# Operador '+' = OP_ADD
# Operador '-' = OP_SUB
# Operador '*' = OP_MUL
# Operador '/' = OP_DIV
# Operador '^' = OP_POT
# Operador Relacional '>'  = OP_MAI
# Operador Relacional '<'  = OP_MEN
# Operador Relacional '==' = OP_IGU
# Operador Relacional '>=' = OP_MIG
# Operador Relacional '<=' = OP_MEI
# Operador Relacional '<>' = OP_DIF
# Atribuição '=' = ATR
# Palavras reservadas: 'var', 'int', 'real', 'while', 'if', 'else', 'break', 'for'; = RES
import re


arqTemp = 'tempo.txt'
arqFinal = 'programafinal.txt'
arqBase = 'programa.txt'
arqFinalTeste = 'arqfinalteste.txt'
arqFinalTesteTempo = 'arqfinaltestetempo.txt'
def m():
    a = open(arqFinal, 'r')
    t = a.read()
    print(t)
pass

#isola o tab
def separadem1():
    aux = open(arqTemp, 'w')
    a = open(arqBase,'r')
    t = a.readlines()
    d = '\t'
    for linha in t:
        l = linha.replace(d, '\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#exclui nova linha
def separadem2():
    aux = open(arqFinal, 'w')
    a = open(arqTemp,'r')
    t = a.readlines()
    d = ' '
    for linha in t:
        l = linha.replace(d, '\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#isola abre conchentes
def separadem3():
    aux = open(arqTemp, 'w')
    a = open(arqFinal,'r')
    t = a.readlines()
    d = '['
    for linha in t:
        l = linha.replace(d, '\n[\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#isola fecha conchetes
def separadem4():
    aux = open(arqFinal, 'w')
    a = open(arqTemp,'r')
    t = a.readlines()
    d = ']'
    for linha in t:
        l = linha.replace(d, '\n]\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#isola abre parenteses
def separadem5():
    aux = open(arqTemp, 'w')
    a = open(arqFinal,'r')
    t = a.readlines()
    d = '('
    for linha in t:
        l = linha.replace(d, '\n(\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#isola fecha parenteses
def separadem6():
    aux = open(arqFinal, 'w')
    a = open(arqTemp,'r')
    t = a.readlines()
    d = ')'
    for linha in t:
        l = linha.replace(d, '\n)\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#isola o ponto e virgula
def separadem7():
    aux = open(arqTemp, 'w')
    a = open(arqFinal,'r')
    t = a.readlines()
    d = ';'
    for linha in t:
        l = linha.replace(d, '\n;\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#isola virgula
def separadem8():
    aux = open(arqFinal, 'w')
    a = open(arqTemp,'r')
    t = a.readlines()
    d = ','
    for linha in t:
        l = linha.replace(d, '\n,\n')
        aux.writelines(l)
    a.close()
    aux.close()
pass

#Chamada de método, isola cada char em uma linha unica. Saida: programafinal.txt
separadem1()
separadem2()
separadem3()
separadem4()
separadem5()
separadem6()
separadem7()
separadem8()
m()

#Referencia os delimitadores com seus tokens, salva como ArquivoFinalTeste
def analisadorDEM():
    a = open(arqFinal, 'r')
    aux = open(arqFinalTeste,'w')
    t = a.read()
    DEM = [',',';','(',')','{','}','[',']']
    for linha in t:
        if DEM[0] in linha:
            l = linha.replace(',','@DEM_VIRGULA\n')
            aux.writelines(l)
        elif DEM[1] in linha:
            l = linha.replace(';','@DEM_PONTO_VIRGULA\n')
            aux.writelines(l)
        elif DEM[2] in linha:
            l = linha.replace('(','@DEM_ABRE_PARENTESE\n')
            aux.writelines(l)
        elif DEM[3] in linha:
            l = linha.replace(')','@DEM_FECHA_PARENTESE\n')
            aux.writelines(l)
        elif DEM[4] in linha:
            l = linha.replace('{','@DEM_ABRE_CHAVES\n')
            aux.writelines(l)
        elif DEM[5] in linha:
            l = linha.replace('}','@DEM_FECHA_CHAVES\n')
            aux.writelines(l)
        elif DEM[6] in linha:
            l = linha.replace('[','@DEM_ABRE_CONCHETES\n')
            aux.writelines(l)
        elif DEM[7] in linha:
            l = linha.replace(']','@DEM_FECHA_CONCHETES\n')
            aux.writelines(l)
        else:
            aux.writelines(linha)
    aux.close()
    a.close()

#Referencia as palavras reservadas com seus tokens, salva como arqFinalTesteTempo
def analisadorRES():
    a = open(arqFinalTeste, 'r')
    aux = open(arqFinalTesteTempo,'w')
    t = a.readlines()
    DEM = ['var','int','real','while','if','else']
    for linha in t:
        if DEM[0] in linha:
            l = linha.replace(DEM[0],'@RES_VAR\n')
            aux.writelines(l)
        elif DEM[1] in linha:
            l = linha.replace(DEM[1],'@RES_INT\n')
            aux.writelines(l)
        elif DEM[2] in linha:
            l = linha.replace(DEM[2],'@RES_REAL\n')
            aux.writelines(l)
        elif DEM[3] in linha:
            l = linha.replace(DEM[3],'@RES_WHILE\n')
            aux.writelines(l)
        elif DEM[4] in linha:
            l = linha.replace(DEM[4],'@RES_IF\n')
            aux.writelines(l)
        elif DEM[5] in linha:
            l = linha.replace(DEM[5],'@RES_ELSE\n')
            aux.writelines(l)
        else:
            aux.writelines(linha)
    aux.close()
    a.close()


#Refencia os operadores aritmeticos com seus tokens, salva no arqFinalTeste
def analisadorOP():
    a = open(arqFinalTesteTempo, 'r')
    aux = open(arqFinalTeste,'w')
    t = a.readlines()
    DEM = ['>','<','==','>=','<=','<>','!=','+','-','*','/','^']
    for linha in t:
        if DEM[0] in linha:
            l = linha.replace(DEM[0],'@OP_MAI\n')
            aux.writelines(l)
        elif DEM[1] in linha:
            l = linha.replace(DEM[1],'@OP_MEN\n')
            aux.writelines(l)
        elif DEM[2] in linha:
            l = linha.replace(DEM[2],'@OP_IGU\n')
            aux.writelines(l)
        elif DEM[3] in linha:
            l = linha.replace(DEM[3],'@OP_MIG\n')
            aux.writelines(l)
        elif DEM[4] in linha:
            l = linha.replace(DEM[4],'@OP_MEI\n')
            aux.writelines(l)
        elif DEM[5] in linha:
            l = linha.replace(DEM[5],'@OP_DIF1\n')
            aux.writelines(l)
        elif DEM[6] in linha:
            l = linha.replace(DEM[6],'@OP_DIF2\n')
            aux.writelines(l)
        elif DEM[7] in linha:
            l = linha.replace(DEM[7],'@OP_ADD\n')
            aux.writelines(l)
        elif DEM[8] in linha:
            l = linha.replace(DEM[8],'@OP_SUB\n')
            aux.writelines(l)
        elif DEM[9] in linha:
            l = linha.replace(DEM[9],'@OP_MUL\n')
            aux.writelines(l)
        elif DEM[10] in linha:
            l = linha.replace(DEM[10],'@OP_DIV\n')
            aux.writelines(l)
        elif DEM[11] in linha:
            l = linha.replace(DEM[11],'@OP_POT\n')
            aux.writelines(l)
        else:
            aux.writelines(linha)
    aux.close()
    a.close()

#Refrencia o operador de atribuição
def analisadorATR():
    a = open(arqFinalTeste, 'r')
    aux = open(arqFinalTesteTempo,'w')
    t = a.readlines()
    DEM = ['=']
    for linha in t:
        if DEM[0] in linha:
            l = linha.replace(DEM[0],'@ATR\n')
            aux.writelines(l)
        else:
            aux.writelines(linha)
    aux.close()
    a.close()

#Referencia os numeros reais com seus tokens
def analisadorNumerosReais():
    a = open(arqFinalTesteTempo, 'r')
    aux = open(arqFinalTeste,'w')
    t = a.readlines()
    for linha in t:
        if '.' in linha:
            l = linha.replace(linha,'@NUM_REAL\n')
            aux.writelines(l)
        else:
            aux.writelines(linha)
    aux.close()
    a.close()

#Refrencia numeros inteiros com seus tokens,o regex utilizado ^\d = comço de string, numero inteiro e final sem letras
def analisadorNumerosInt():
    a = open(arqFinalTeste, 'r')
    aux = open(arqFinalTesteTempo,'w')
    t = a.readlines()
    for linha in t:
        if bool(re.search('^\d',linha)) == True:
            l = linha.replace(linha,'@NUM_INT\n')
            aux.writelines(l)
        else:
            aux.writelines(linha)
    aux.close()
    a.close()

#Referencia as variaveis com seus tokens
def analisadorVar():
    a = open(arqFinalTesteTempo, 'r')
    aux = open(arqFinalTeste,'w')
    t = a.readlines()
    z = "@"
    for linha in t:
        if z in linha:
            aux.writelines(linha)
            print(linha)
        if len(linha) == 1:
            print(linha)
        if len(linha) > 1 and z not in linha:
            l = linha.replace(linha,'@TOK_VAR\n')
            aux.writelines(l)
            print(linha)
        #print(len(linha))
    aux.close()
    a.close()



#Chamada dos metodos
analisadorDEM()
analisadorRES()
analisadorOP()
analisadorATR()
analisadorNumerosReais()
analisadorNumerosInt()
analisadorVar()


#print(bool(re.search("^\d","1")))