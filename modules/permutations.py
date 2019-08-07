'''
Permutaciones que realiza el algoritmo
'''
import modules.convert


def palPerms(a):
    lior=[a]
    lich=[]
    linewpal=[]
    for i in range(len(lior)):#i será la posición palabra de la lista
        palabra=lior[i]#palabra será el valor de la palabra en esa posicion
        #linewpal.append(palabra)#Añadir a la lista de nuevas palabras la palabra sin modificar.
        for j in range(len(palabra)):#j será la posición del caracter en la palabra
            lich=[]#Inicializar la lista vacía por cada carácter
            letra=palabra[j]#letra será el valor de la letra en esa posicion [j]
            lich.append(letra)#Almaceno el carácter de la palabra en la lista de los carácteres permutables
            '''Pasamos a comprobar los valores que podrían permutar'''
            chascii=modules.convert.dicCon(letra)#Saco ascii de la letra en [j]
            lMayMin=modules.convert.chchar(chascii)#Extraigo el opuesto(Mayus o Minus) y almaceno el valor (no el ascii)
            lich.append(lMayMin)#Almaceno el caracter opuesto en la lista
            '''Comprobarmos si se puede cambiar la letra por un número'''
            lNum=modules.convert.charToNum(chascii)#Almaceno en lNum el valor correspondiente al carácter en número
            if lNum != None: #Si se obtiene resultado en el cambio a número
                lNum=modules.convert.chrToNum(lNum)
                lich.append(lNum)#Añadir el valor numérico a la lista de permutaciones.
            '''Comporbamos si se puede cambiar por otra letra o carácter'''
            lnlch=modules.convert.charToChar(chascii)#Almaceno en lnlch el valor correspondiente a la letra
            if lnlch != None:
                lnlchletra=modules.convert.chrToNum(lnlch)
                lnlchletra1=modules.convert.chchar(lnlch)
                if lnlchletra != None:#Si hay valor para lnlchletra
                    lich.append(lnlchletra)#-> Añadir en la lista lich
                if lnlchletra1 != None:#Si hay valor para lnlchletra1
                    lich.append(lnlchletra1)#-> Añadir en la lista lich
                    lnlchletra1num=modules.convert.charToNum(lnlch)
                    if lnlchletra1num != None:
                        lnlchletra1num=modules.convert.chrToNum(lnlchletra1num)
                        lich.append(lnlchletra1num)
                    lnlmore=lnlch-32#Paso a mayuscula el valor ascii en minuscula
                    lnlmore=modules.convert.morech(lnlmore)#Ejecuto la función comprobartoria para el nuevo cambio.
                    if lnlmore != None:#Si se obtienen resultados
                        lnlmore=modules.convert.chrToNum(lnlmore)#Sacar el valor nuevo del ASCII
                        lich.append(lnlmore)#Almacenar en la lista de caracteres para esa posición
                        lnlmore=ord(lnlmore)#Lnlmore lo paso a ASCII
                        if lnlmore!=38:
                            lnlmoremin=modules.convert.mayToMin(lnlmore)#Saco la minuscula de lnlmore
                            lich.append(lnlmoremin)#Almacenar en la lista de caracteres para esa posición
            if j!=0:#Realizar las permutaciones en linewpal sobre la posicion j
                for t in range(len(linewpal)):
                    palper=linewpal[t]
                    if t>=0:
                        for z in range(len(lich)):
                            if z!=0:#Para que no se repita la primera palabra
                                clz=lich[z]#Carácter a cambiar
                                prefijo=palper[:j]#Sacar el prefijo de la palabra
                                sufijo=palabra[j:]#Sacar el sufijo de la palabra
                                newpal=sufijo.replace(f'{sufijo[0]}', f'{clz}')
                                newpaltolist=prefijo+newpal
                                linewpal.append(newpaltolist)
                            else:
                                pass
            elif j==0:#Realizar permutaciones sobre la palabra original y almacenar en linewpal
                for z in range(len(lich)):
                    clz=lich[z]#Valor del carazter en la posición z de lich
                    sufijo=palabra[j:]#Sacar el sufijo de la palabra
                    newpal=sufijo.replace(f'{sufijo[0]}', f'{clz}')
                    newpaltolist=newpal
                    linewpal.append(newpaltolist)
            for i in range(len(linewpal)):
                i+=1
        return i,linewpal

def perNum(a,b):#Añadir número a la palabra. b marca el límite.
    lipnum=[]
    b=int(b)
    for i in range(0,b):
        i=str(i)
        b=a+i
        lipnum.append(b)
    return lipnum

def perChrt(a):#Añadir carácter a la palabra
    lipcht=[]
    for i in range(30, 192):
        if (i==33 or i==34 or i==35 or i==36 or i==37 or i==38 or i==39
            or i==40 or i==41 or i==42 or i==43 or i==44 or i==45 or i==46
            or i==47 or i==58 or i==59 or i==61 or i==63 or i==64 or i==91
            or i==92 or i==93 or i==94 or i==95 or i==123 or i==124
            or i==125 or i==161 or i==168 or i==191):
            i=chr(i)
            j=str(i)
            b=a+j
            lipcht.append(b)
        else:
            pass
    return lipcht

def pnch(a,b):#Añadir número y carácter a la palabra. b marca el límite
    lipnch=[]
    b=int(b)
    for i in range(0,b):
        i=str(i)
        b=a+i
        lipnch.append(b)
        b=perChrt(b)
        lipnch.append(b)
    return lipnch
