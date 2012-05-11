'''
Created on 11 mai 2012

@author: Askylh
'''

from pokereval import PokerEval


Peval = PokerEval()
iteration=100000
ev = Peval.poker_eval(game='holdem', pockets=[["tc", "ts"], ["kd", "ad"]], board=["__", "__", "__", "__", "__"], iterations=iteration)

print ev['eval']