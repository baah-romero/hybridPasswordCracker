import modules.algact

def creDict():
    dictFile=modules.algact.adFile()
    dictFile=dictFile+'.txt'
    return dictFile

def wrFil(a,b):
    wr=a
    ndic=b
    fw=open(f'{ndic}', 'a+')#Añade al final de la línea
    fw.write(f'{wr}\n')
    fw.close
