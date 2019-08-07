# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:27:58 2019

@author: baah-romero
"""
import modules.guihpc
import modules.algact

def main():
    modules.algact.clearTerm()
    modules.guihpc.maiHead()
    modules.guihpc.maiStop()
    modules.algact.nDiList()

if __name__=='__main__':
    main()
