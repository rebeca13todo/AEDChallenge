
import participant as p

AGE_COEFICIENT = 1
YOS_COEFICIENT = 1
UNIVERSITY_COEFICIENT = 1



def distancia(p1:p.Participant, p2:p.Participant):
    '''Recibe dos participantes y devuelve una distancia que es menor cuanto más similares/afines son'''

    
    d = 0

    #Age
    d += abs(p1.age - p2.age)*AGE_COEFICIENT

    #Year of study
    d += abs( yos_to_int(p1.year_of_study) - yos_to_int(p2.year_of_study))*YOS_COEFICIENT

    #University
    d += int( p1.university==p2.university )*YOS_COEFICIENT








def yos_to_int(year_of_study:str) -> int:
    '''Transforma la variable year_of_study a un interger'''

    match year_of_study:
        case "1st year": return 1
        case "2nd year": return 2
        case "3rd year": return 3
        case "4th year": return 4
        case "Masters": return 5
        case "PhD": return 6
        case _: return -1

