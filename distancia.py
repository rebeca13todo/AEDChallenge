
import participant as p

def distancia(p1:p.Participant, p2:p.Participant):
    '''Recibe dos participantes y devuelve una distancia que es menor cuanto más similares/afines son'''

    atr_iguals(p1.age, p2.age, 1)
    ...

def atr_iguals(p, r, punt: int) -> int: