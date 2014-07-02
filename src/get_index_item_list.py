#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

I have a list in python and would like to know how I can get the index of an
element contained in the list?

Tengo una lista en python y quisiera saber ¿como puedo obtener el indice de un
elemento contenido en la lista?
'''

#create a list from str
lista = list('hello world')
print (lista)

#get index of the first item whose value is passed as parameter
index = lista.index('l')
print (index)

#define the index from which you want to search
index = lista.index('l', 3)
print (index)

#define the segment of the list to be searched
index = lista.index('o', 5, 8)
print (index)
