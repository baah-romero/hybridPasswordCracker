'''
Fichero donde se recogen las acciones de conversión de caracteres
'''
def dicCon( a):#Retorna el caracter en ASCII
    car=a
    car=ord(car)
    return car

'''Función que se pasa un valor ascii de caracter y saca la minuscula'''
def mayToMin(a):
    ncmin=a
    ncmin+=32
    ncmin=chr(ncmin)
    return ncmin

'''Función que se pasa un valor ascii de caracter y saca la Mayuscula'''
def minToMay(a):
    ncmay=a
    ncmay-=32
    ncmay=chr(ncmay)
    return ncmay

'''Función que se pasa un valor ascii de caracter y saca el número'''
def chrToNum(a):
    nctnum=chr(a)
    return nctnum

'''Función para cambiar de carácter a número'''
def charToNum(a):
    ctna=a
    if ctna==65 or ctna==97:#Si es 'A' o 'a' retornar '4'
        ctna=52#ctna valdrá '4'
        return ctna
    elif ctna==73 or ctna==76  or ctna==105  or ctna==108:#Si es 'I' o 'i' o 'L' o 'l' retornar '1'
        ctna=49#ctna valdrá '1'
        return ctna
    elif ctna==69 or ctna==101:#Si es 'E' o 'e' retornar '3'
        ctna=51#ctna valdrá '3'
        return ctna
    elif ctna==79 or ctna==111:#Si es 'O' o 'o' retornar '0'
        ctna=48#ctna valdrá '0'
        return ctna
    elif ctna==83 or ctna==115:#Si es 'S' o 's' retornar '5'
        ctna=53#ctna valdrá '5'
        return ctna
    elif ctna==71 or ctna==103:#Si es 'G' o 'g' retornar '6'
        ctna=54#ctna valdrá '6'
        return ctna
    elif ctna==84 or ctna==116:#Si es 'T' o 't' retornar '7'
        ctna=55#ctna valdrá '7'
        return ctna
    elif ctna==66 or ctna==98:#Si es 'B' o 'b' retornar '8'
        ctna=56#ctna valdrá '8'
        return ctna
    elif ctna==90 or ctna==122:#Si es 'Z' o 'z' retornar '2'
        ctna=50#ctna valdrá '2'
        return ctna
    elif ctna==80 or ctna==112:#Si es 'P' o 'p' retornar '9'
        ctna=57#ctna valdrá '9'
        return ctna

'''Función para pasar de letra a caracter'''
def charToChar(a):
    ctnc=a
    if ctnc==66 or ctnc==98:#Si es 'B' o 'b' retornar 'v'
        ctnc=118#ctnc valdrá 'v'
        return ctnc
    elif ctnc==86 or ctnc==118:#Si es 'V' o 'v' retornar 'b'
        ctnc=98#ctnc valdrá 'b'
        return ctnc
    elif ctnc==71 or ctnc==103:#Si es 'G' o 'g' retornar 'j'
        ctnc=106#ctnc valdrá 'j'
        return ctnc
    elif ctnc==74 or ctnc==106:#Si es 'J' o 'j' retornar 'g'
        ctnc=103#ctnc valdrá 'g'
        return ctnc
    elif ctnc==67 or ctnc==99:#Si es 'C' o 'c' retornar 'k'
        ctnc=107#ctnc valdrá 'k'
        return ctnc
    elif ctnc==81 or ctnc==113:#Si es 'Q' o 'q' retornar 'k'
        ctnc=107#ctnc valdrá 'k'
        return ctnc
    elif ctnc==75 or ctnc==107:#Si es 'K' o 'k' retornar 'q'
        ctnc=113#ctnc valdrá 'q'
        return ctnc
    elif ctnc==87 or ctnc==119:#Si es 'W' o 'w' retornar 'v'
        ctnc=118#ctnc valdrá 'v'
        return ctnc
    elif ctnc==89 or ctnc==121:#Si es 'Y' o 'y' retornar 'i'
        ctnc=105#ctnc valdrá 'i'
        return ctnc
    elif ctnc==77 or ctnc==109:#Si es 'M' o 'm' retornar 'n'
        ctnc=110#ctnc valdrá 'n'
        return ctnc
    elif ctnc==78 or ctnc==110:#Si es 'N' o 'n' retornar 'm'
        ctnc=109#ctnc valdrá 'm'
        return ctnc
    elif ctnc==42:#Si es '*' retornar 'x'
        ctnc=120#ctnc valdrá 'x'
        return ctnc
    elif ctnc==88 or ctnc==120:#Si es 'X' o 'x' retornar '*'
        ctnc=42#ctnc valdrá '*'
        return ctnc
    elif ctnc==124:#Si es '|' retornar 'o'
        ctnc=111#ctnc valdrá 'o'
        return ctnc
    elif ctnc==79 or ctnc==111:#Si es 'O' o 'o' retornar '|'
        ctnc=124#ctnc valdrá '|'
        return ctnc
    elif ctnc==73 or ctnc==105:#Si es 'I' o 'i' retornar 'y'
        ctnc=121#ctnc valdrá 'y'
        return ctnc
    elif ctnc==38:#Si es '&' retornar 'y'
        ctnc=121#ctnc valdrá 'y'
        return ctnc
    elif ctnc==41:#Si es ')' retornar '('
        ctnc=40#ctnc valdrá '('
        return ctnc
    elif ctnc==40:#Si es '(' retornar ')'
        ctnc=41#ctnc valdrá ')'
        return ctnc
    elif ctnc==34:#Si es '"' retornar "'"
        ctnc=39#ctnc valdrá "'"
        return ctnc
    elif ctnc==39:#Si es "'" retornar '"'
        ctnc=34#ctnc valdrá '"'
        return ctnc
    elif ctnc==63:#Si es "?" retornar '¿'
        ctnc=191#ctnc valdrá '¿'
        return ctnc
    elif ctnc==191:#Si es "¿" retornar '?'
        ctnc=63#ctnc valdrá '?'
        return ctnc
    elif ctnc==161:#Si es "¡" retornar '!'
        ctnc=33#ctnc valdrá '!'
        return ctnc
    elif ctnc==33:#Si es "!" retornar '¡'
        ctnc=161#ctnc valdrá '¡'
        return ctnc


'''Construir toda la función'''
def morech(a):
        moch=0
        if a== 66 or a ==86:#Si es B o V
            moch=87
            return moch #Retorna W
        elif a==73 or a==89:#Si es I o Y
            moch=38
            return moch #Retorna &
        elif a==38:#Si es &
            moch=73
            return moch #Retorna I
        elif a==87:#Si es W
            moch=66#Retorna B
            return moch


def chchar(a):#Comprueba con el ASCII que tipo de caracter es
    char=a
    if char in range(65,91):#Es Mayuscula
        nchar=mayToMin(char)#Convertir a minuscula el ASCII
        return nchar
    elif char in range(97,123):#Es Minuscula
        nchar=minToMay(char)#Convertir a mayuscula el ASCII
        return nchar
    elif char==32:#Es un espacio
        nchar=chr(95)#Retorna '_'
        return nchar

def chchnum(a):#Realizar la función que compruebe letras y retorne true.
    cctn=a
    #cctn=dicCon(cctn)#Convierto a ASCII el valor
    if (cctn>=65 and cctn<91) or (cctn>=97 or cctn<123):
        return True #Si es una letra mayus o minus retorna true
    elif (cctn>=48 and ccnt<58):
        return False #Si no es un número.
        '''Programar futuramente las acciones a la inversa en caso de ser número.'''

def enList(a):#Función para acabar la lista
    a=a
    if a==':wq':
        return True
    else:
        return False

def countList(a):
    cnt=0
    for i in range(len(a)):
        cnt+=1
    return cnt
