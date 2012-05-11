#-*-coding: utf-8 *-*
'''
Created on 11 mai 2012

@author: Askylh Snake
'''
import poker


print poker.one_round7()

print poker.eval7(['Jd', 'Td','Js', '7h', 'Qc']), ' h1'
print poker.eval7(['Jd', 'Tc','4s', '7h', 'Qc'])
''' 
comment utiliser cette algo pour réaliser un ev d'un board inconnu ?
    faire un deck
    le shuffle
    enlever la main de hero du deck
    prendre les 5 prem cartes
    print hand, board, eval
comment utiliser cette algo pour réaliser un ev sur un % de main du vilain ?
'''