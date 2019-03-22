# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:27:58 2019

@author: baah-romero
"""
import os
import time
class Conver:#Funciones de Conversión de caracteres
    def dicCon(self, a):#Retorna el caracter en ASCII
        self.car=a
        self.car=ord(self.car)
        return self.car

    '''Función que se pasa un valor ascii de caracter y saca la minuscula'''
    def mayToMin(self,a):
        self.ncmin=a
        self.ncmin+=32
        self.ncmin=chr(self.ncmin)
        return self.ncmin

    '''Función que se pasa un valor ascii de caracter y saca la Mayuscula'''
    def minToMay(self,a):
        self.ncmay=a
        self.ncmay-=32
        self.ncmay=chr(self.ncmay)
        return self.ncmay

    '''Función que se pasa un valor ascii de caracter y saca el número'''
    def chrToNum(self,a):
        self.nctnum=chr(a)
        return self.nctnum

    '''Función para cambiar de carácter a número'''
    def charToNum(self,a):
        self.ctna=a
        if self.ctna==65 or self.ctna==97:#Si es 'A' o 'a' retornar '4'
            self.ctna=52#ctna valdrá '4'
            return self.ctna
        elif self.ctna==73 or self.ctna==76  or self.ctna==105  or self.ctna==108:#Si es 'I' o 'i' o 'L' o 'l' retornar '1'
            self.ctna=49#ctna valdrá '1'
            return self.ctna
        elif self.ctna==69 or self.ctna==101:#Si es 'E' o 'e' retornar '3'
            self.ctna=51#ctna valdrá '3'
            return self.ctna
        elif self.ctna==79 or self.ctna==111:#Si es 'O' o 'o' retornar '0'
            self.ctna=48#ctna valdrá '0'
            return self.ctna
        elif self.ctna==83 or self.ctna==115:#Si es 'S' o 's' retornar '5'
            self.ctna=53#ctna valdrá '5'
            return self.ctna
        elif self.ctna==71 or self.ctna==103:#Si es 'G' o 'g' retornar '6'
            self.ctna=54#ctna valdrá '6'
            return self.ctna
        elif self.ctna==84 or self.ctna==116:#Si es 'T' o 't' retornar '7'
            self.ctna=55#ctna valdrá '7'
            return self.ctna
        elif self.ctna==66 or self.ctna==98:#Si es 'B' o 'b' retornar '8'
            self.ctna=56#ctna valdrá '8'
            return self.ctna
        elif self.ctna==90 or self.ctna==122:#Si es 'Z' o 'z' retornar '2'
            self.ctna=50#ctna valdrá '2'
            return self.ctna
        elif self.ctna==80 or self.ctna==112:#Si es 'P' o 'p' retornar '9'
            self.ctna=57#ctna valdrá '9'
            return self.ctna

    '''Función para pasar de letra a caracter'''
    def charToChar(self,a):
        self.ctnc=a
        if self.ctnc==66 or self.ctnc==98:#Si es 'B' o 'b' retornar 'v'
            self.ctnc=118#ctnc valdrá 'v'
            return self.ctnc
        elif self.ctnc==86 or self.ctnc==118:#Si es 'V' o 'v' retornar 'b'
            self.ctnc=98#ctnc valdrá 'b'
            return self.ctnc
        elif self.ctnc==71 or self.ctnc==103:#Si es 'G' o 'g' retornar 'j'
            self.ctnc=106#ctnc valdrá 'j'
            return self.ctnc
        elif self.ctnc==74 or self.ctnc==106:#Si es 'J' o 'j' retornar 'g'
            self.ctnc=103#ctnc valdrá 'g'
            return self.ctnc
        elif self.ctnc==67 or self.ctnc==99:#Si es 'C' o 'c' retornar 'k'
            self.ctnc=107#ctnc valdrá 'k'
            return self.ctnc
        elif self.ctnc==81 or self.ctnc==113:#Si es 'Q' o 'q' retornar 'k'
            self.ctnc=107#ctnc valdrá 'k'
            return self.ctnc
        elif self.ctnc==75 or self.ctnc==107:#Si es 'K' o 'k' retornar 'q'
            self.ctnc=113#ctnc valdrá 'q'
            return self.ctnc
        elif self.ctnc==87 or self.ctnc==119:#Si es 'W' o 'w' retornar 'v'
            self.ctnc=118#ctnc valdrá 'v'
            return self.ctnc
        elif self.ctnc==89 or self.ctnc==121:#Si es 'Y' o 'y' retornar 'i'
            self.ctnc=105#ctnc valdrá 'i'
            return self.ctnc
        elif self.ctnc==77 or self.ctnc==109:#Si es 'M' o 'm' retornar 'n'
            self.ctnc=110#ctnc valdrá 'n'
            return self.ctnc
        elif self.ctnc==78 or self.ctnc==110:#Si es 'N' o 'n' retornar 'm'
            self.ctnc=109#ctnc valdrá 'm'
            return self.ctnc
        elif self.ctnc==42:#Si es '*' retornar 'x'
            self.ctnc=120#ctnc valdrá 'x'
            return self.ctnc
        elif self.ctnc==88 or self.ctnc==120:#Si es 'X' o 'x' retornar '*'
            self.ctnc=42#ctnc valdrá '*'
            return self.ctnc
        elif self.ctnc==124:#Si es '|' retornar 'o'
            self.ctnc=111#ctnc valdrá 'o'
            return self.ctnc
        elif self.ctnc==79 or self.ctnc==111:#Si es 'O' o 'o' retornar '|'
            self.ctnc=124#ctnc valdrá '|'
            return self.ctnc
        elif self.ctnc==73 or self.ctnc==105:#Si es 'I' o 'i' retornar 'y'
            self.ctnc=121#ctnc valdrá 'y'
            return self.ctnc
        elif self.ctnc==38:#Si es '&' retornar 'y'
            self.ctnc=121#ctnc valdrá 'y'
            return self.ctnc
        elif self.ctnc==41:#Si es ')' retornar '('
            self.ctnc=40#ctnc valdrá '('
            return self.ctnc
        elif self.ctnc==40:#Si es '(' retornar ')'
            self.ctnc=41#ctnc valdrá ')'
            return self.ctnc
        elif self.ctnc==34:#Si es '"' retornar "'"
            self.ctnc=39#ctnc valdrá "'"
            return self.ctnc
        elif self.ctnc==39:#Si es "'" retornar '"'
            self.ctnc=34#ctnc valdrá '"'
            return self.ctnc
        elif self.ctnc==63:#Si es "?" retornar '¿'
            self.ctnc=191#ctnc valdrá '¿'
            return self.ctnc
        elif self.ctnc==191:#Si es "¿" retornar '?'
            self.ctnc=63#ctnc valdrá '?'
            return self.ctnc
        elif self.ctnc==161:#Si es "¡" retornar '!'
            self.ctnc=33#ctnc valdrá '!'
            return self.ctnc
        elif self.ctnc==33:#Si es "!" retornar '¡'
            self.ctnc=161#ctnc valdrá '¡'
            return self.ctnc


    '''Construir toda la función'''
    def morech(self,a):
            self.moch=0
            if a== 66 or a ==86:#Si es B o V
                self.moch=87
                return self.moch #Retorna W
            elif a==73 or a==89:#Si es I o Y
                self.moch=38
                return self.moch #Retorna &
            elif a==38:#Si es &
                self.moch=73
                return self.moch #Retorna I
            elif a==87:#Si es W
                self.moch=66#Retorna B
                return self.moch


class Checks:
    def chchar(self,a):#Comprueba con el ASCII que tipo de caracter es
        self.char=a
        if self.char in range(65,91):#Es Mayuscula
            self.nchar=conver.mayToMin(self.char)#Convertir a minuscula el ASCII
            return self.nchar
        elif self.char in range(97,123):#Es Minuscula
            self.nchar=conver.minToMay(self.char)#Convertir a mayuscula el ASCII
            return self.nchar
        elif self.char==32:#Es un espacio
            self.nchar=chr(95)#Retorna '_'
            return self.nchar

    def chchnum(self,a):#Realizar la función que compruebe letras y retorne true.
        self.cctn=a
        #self.cctn=conver.dicCon(self.cctn)#Convierto a ASCII el valor
        if (self.cctn>=65 and self.cctn<91) or (self.cctn>=97 or self.cctn<123):
            return True #Si es una letra mayus o minus retorna true
        elif (self.cctn>=48 and self.ccnt<58):
            return False #Si no es un número.
            '''Programar futuramente las acciones a la inversa en caso de ser número.'''

    def enList(self,a):#Función para acabar la lista
        self.a=a
        if self.a==':wq':
            return True
        else:
            return False

    def countList(self,a):
        self.cnt=0
        for i in range(len(a)):
            self.cnt+=1
        return self.cnt

class Perm:
    def palPerms(self,a):
        self.lior=[a]
        self.lich=[]
        self.linewpal=[]
        for i in range(len(self.lior)):#i será la posición palabra de la lista
            palabra=self.lior[i]#palabra será el valor de la palabra en esa posicion
            #self.linewpal.append(palabra)#Añadir a la lista de nuevas palabras la palabra sin modificar.
            for j in range(len(palabra)):#j será la posición del caracter en la palabra
                self.lich=[]#Inicializar la lista vacía por cada carácter
                letra=palabra[j]#letra será el valor de la letra en esa posicion [j]
                self.lich.append(letra)#Almaceno el carácter de la palabra en la lista de los carácteres permutables
                '''Pasamos a comprobar los valores que podrían permutar'''
                chascii=conver.dicCon(letra)#Saco ascii de la letra en [j]
                lMayMin=checks.chchar(chascii)#Extraigo el opuesto(Mayus o Minus) y almaceno el valor (no el ascii)
                self.lich.append(lMayMin)#Almaceno el caracter opuesto en la lista
                '''Comprobarmos si se puede cambiar la letra por un número'''
                lNum=conver.charToNum(chascii)#Almaceno en lNum el valor correspondiente al carácter en número
                if lNum != None: #Si se obtiene resultado en el cambio a número
                    lNum=conver.chrToNum(lNum)
                    self.lich.append(lNum)#Añadir el valor numérico a la lista de permutaciones.
                '''Comporbamos si se puede cambiar por otra letra o carácter'''
                lnlch=conver.charToChar(chascii)#Almaceno en lnlch el valor correspondiente a la letra
                if lnlch != None:
                    lnlchletra=conver.chrToNum(lnlch)
                    lnlchletra1=checks.chchar(lnlch)
                    if lnlchletra != None:#Si hay valor para lnlchletra
                        self.lich.append(lnlchletra)#-> Añadir en la lista self.lich
                    if lnlchletra1 != None:#Si hay valor para lnlchletra1
                        self.lich.append(lnlchletra1)#-> Añadir en la lista self.lich
                        lnlchletra1num=conver.charToNum(lnlch)
                        if lnlchletra1num != None:
                            lnlchletra1num=conver.chrToNum(lnlchletra1num)
                            self.lich.append(lnlchletra1num)
                        lnlmore=lnlch-32#Paso a mayuscula el valor ascii en minuscula
                        lnlmore=conver.morech(lnlmore)#Ejecuto la función comprobartoria para el nuevo cambio.
                        if lnlmore != None:#Si se obtienen resultados
                            lnlmore=conver.chrToNum(lnlmore)#Sacar el valor nuevo del ASCII
                            self.lich.append(lnlmore)#Almacenar en la lista de caracteres para esa posición
                            lnlmore=ord(lnlmore)#Lnlmore lo paso a ASCII
                            if lnlmore!=38:
                                lnlmoremin=conver.mayToMin(lnlmore)#Saco la minuscula de lnlmore
                                self.lich.append(lnlmoremin)#Almacenar en la lista de caracteres para esa posición
                if j!=0:#Realizar las permutaciones en self.linewpal sobre la posicion j
                    for t in range(len(self.linewpal)):
                        palper=self.linewpal[t]
                        if t>=0:
                            for z in range(len(self.lich)):
                                if z!=0:#Para que no se repita la primera palabra
                                    clz=self.lich[z]#Carácter a cambiar
                                    prefijo=palper[:j]#Sacar el prefijo de la palabra
                                    sufijo=palabra[j:]#Sacar el sufijo de la palabra
                                    newpal=sufijo.replace(f'{sufijo[0]}', f'{clz}')
                                    newpaltolist=prefijo+newpal
                                    self.linewpal.append(newpaltolist)
                                else:
                                    pass
                elif j==0:#Realizar permutaciones sobre la palabra original y almacenar en self.linewpal
                    for z in range(len(self.lich)):
                        clz=self.lich[z]#Valor del carazter en la posición z de self.lich
                        sufijo=palabra[j:]#Sacar el sufijo de la palabra
                        newpal=sufijo.replace(f'{sufijo[0]}', f'{clz}')
                        newpaltolist=newpal
                        self.linewpal.append(newpaltolist)
                for i in range(len(self.linewpal)):
                    i+=1
            return i,self.linewpal

    def perNum(self,a,b):#Añadir número a la palabra. b marca el límite.
        self.lipnum=[]
        b=int(b)
        for i in range(0,b):
            i=str(i)
            b=a+i
            self.lipnum.append(b)
        return self.lipnum

    def perChrt(self,a):#Añadir carácter a la palabra
        self.lipcht=[]
        for i in range(30, 192):
            if (i==33 or i==34 or i==35 or i==36 or i==37 or i==38 or i==39
                or i==40 or i==41 or i==42 or i==43 or i==44 or i==45 or i==46
                or i==47 or i==58 or i==59 or i==61 or i==63 or i==64 or i==91
                or i==92 or i==93 or i==94 or i==95 or i==123 or i==124
                or i==125 or i==161 or i==168 or i==191):
                i=chr(i)
                j=str(i)
                b=a+j
                self.lipcht.append(b)
            else:
                pass
        return self.lipcht

    def pnch(self,a,b):#Añadir número y carácter a la palabra. b marca el límite
        self.lipnch=[]
        b=int(b)
        for i in range(0,b):
            i=str(i)
            b=a+i
            self.lipnch.append(b)
            b=perm.perChrt(b)
            self.lipnch.append(b)
        return self.lipnch

class Fich:
    def creDict(self):
        self.dictFile=actt.adFile()
        self.dictFile=self.dictFile+'.txt'
        return self.dictFile

    def wrFil(self,a,b):
        self.wr=a
        self.ndic=b
        self.fw=open(f'{self.ndic}', 'a+')#Añade al final de la línea
        self.fw.write(f'{self.wr}\n')
        self.fw.close

class Acttion:#Clase en la que se crean las acciones del SW
    def __init__(self):
      pass

    def adNum(self):
        self.a=input(str('|----- [+] Numeros añadir: '))
        return self.a

    def adWord(self):
        self.a=input(str('|----- [+] Introduce palabra: '))
        return self.a

    def adFile(self):
        print('|---------------------------------------------------------------------------------------|')
        self.a=input(str('|----- [+] Nombre del fichero a generar: '))
        print('|---------------------------------------------------------------------------------------|')
        return self.a

    def repAct(self):#Repetir acción
        guisme.repmen()#Mostrar el menú de repetir
        self.a=input(str('\n\tEscoja Opción: '))
        return self.a

    def chRep(self,a):#Comprobar repetir
        self.a=a
        if self.a=='S' or self.a=='s':
            return True
        elif self.a=='N' or self.a=='n':
            return False
        else:
            pass#control de error


    def adSimWord(self):#Añadir 1 palabra y permutar
        self.liPer=[]
        self.word=actt.adWord()
        self.cnt,self.liPer=perm.palPerms(self.word)
        for i in range(len(self.liPer)):
            j=self.liPer[i]
            fich.wrFil(j)
        return self.cnt,self.liPer

    def perSimWord(self,a,b):#Añadir 1 palabra y permutar
        self.liPer=[]
        self.diFile=b
        for i in range(len(a)):
            self.i=a[i]
            self.cnt,self.liPer=perm.palPerms(self.i)
            for z in range(len(self.liPer)):
                w=self.liPer[z]
                fich.wrFil(w, self.diFile)
            guisme.prCntPerWor(self.i,self.cnt)

    def perPnch(self,a):#Añadir numeros ychars
        self.lipnch=[]
        for i in range(len(a)):
            self.word=a[i]
            self.lipnch=perm.perPnch(self.word,10)
            #insertar en fichero si se desea

    def adLiWord(self):#Generar una lista de palabras para el diccionario
        self.liWoPer=[]
        self.ac=True
        while self.ac!=False:
            self.nwrd=actt.adWord()
            self.b=checks.enList(self.nwrd)
            if self.b!=True:
                self.liWoPer.append(self.nwrd)
                self.ac==True
            elif self.b==True:
                self.ac==self.b
                return self.ac, self.liWoPer

    def nDiList(self):
        self.dicF=fich.creDict()
        self.a,self.b=actt.adLiWord()
        self.i=checks.countList(self.b)
        guisme.resum()
        guisme.prCnt(self.i)
        actt.perSimWord(self.b,self.dicF)
        guisme.prEndLis(self.dicF)

class Guisme:
    def resum(self):
        print('|---------------------------------------------------------------------------------------|')
        print('|--------------------------------| RESUMEN |--------------------------------------------|')
        print('|---------------------------------------------------------------------------------------|')
    def repmen(self):
       print('|----------------------------------------------------------|')
       print('|-------------- ¿Desea repetir la acción? -----------------|')
       print('|----------------------------------------------------------|')
       print('|------------ SI [(S)|(s)] | NO [(N)|(n)]  ----------------|')
       print('|----------------------------------------------------------|')

    def prCnt(self,a):
        print('|---------------------------------------------------------------------------------------|')
        print(f'|\t|------- [+] Hay un total de {a} palabras en la lista')

    def prCntPerWor(self,a,b):
        print(f'|\t\t|------- [+] Palabra que permuta: {a}')
        print(f'|\t\t\t|------- [+] Hay un total de {b} permutaciones posibles.')

    def prEndLis(self,a):
        print('|---------------------------------------------------------------------------------------|')
        print(f'|\t|------- [+] Se generó el diccionario {a}')
        print('|---------------------------------------------------------------------------------------|')

def main():
    actt.nDiList()

conver=Conver()
checks=Checks()
perm=Perm()
fich=Fich()
actt=Acttion()
guisme=Guisme()
'''
n,li=actt.adSimWord()
print(f'[+] Existen {n} permutaciones.\n')
d=actt.repAct()
b=actt.chRep(d)
if b==True:
    n,li=actt.adSimWord()
    print(f'[+] Existen {n} permutaciones.\n')
elif b==False:
    pass
num,li=perm.palPerms(a)
perm.perNum(a,b)
perm.perChrt(a)
perm.pnch(a,b)
print(f'{num} permutaciones')
'''
if __name__=='__main__':
    main()
