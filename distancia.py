
import participant as p
from math import pow, e

#Valores customizables que representan la importancia de cada cosa
AGE_COEFICIENT = 1
YOS_COEFICIENT = 1
UNIVERSITY_COEFICIENT = 1
INTERESTS_COEFICIENT = 1
DIFERENT_ROLES_COEFICIENT = 1
SAME_OBJECTIVE_COEFICIENT = 1
HACKATONS_COUNT_COEFICIENT = 1


#Estos parámetros sirven para la función
max_age_diference = 10
max_year_study_diference = 5
max_common_interests = 3
max_hackatons_done_difference = 10


def distancia(p1:p.Participant, p2:p.Participant):
    '''Recibe dos participantes y devuelve una distancia que es menor cuanto más similares/afines son'''
    
    d = 0

    #Age
    d += weird_difference_01(p1.age, p2.age, max_age_diference) * AGE_COEFICIENT

    #Year of study
    d += abs( yos_to_int(p1.year_of_study) - yos_to_int(p2.year_of_study))/max_year_study_diference * YOS_COEFICIENT

    #University
    d += int( p1.university==p2.university ) * YOS_COEFICIENT

    #Experience
    d += abs( exp_to_int(p1.experience_level) - exp_to_int(p2.experience_level))/2 * YOS_COEFICIENT

    #Interests
    d += common_elements(p1.interests, p2.interests)/max_common_interests * INTERESTS_COEFICIENT

    #Preferred role
    d += int( p1.preferred_role != p2.preferred_role ) * DIFERENT_ROLES_COEFICIENT

    #Objective
    d += int( p1.objective == p2.objective ) * SAME_OBJECTIVE_COEFICIENT

    #Hackatons done
    d += weird_difference_01(p1.hackathons_done, p2.hackathons_done, max_hackatons_done_difference) * HACKATONS_COUNT_COEFICIENT



    '''
    programming_skills: Dict[str, int]
    experience_level: Literal["Beginner", "Intermediate", "Advanced"]
    hackathons_done: int

    preferred_role: Literal[
        "Analysis", "Visualization", "Development", "Design", "Don't know", "Don't care"
    ]
    interest_in_challenges: List[str]
    preferred_languages: List[str]
    friend_registration: List[uuid.UUID]
    preferred_team_size: int
    availability: Dict[str, bool]

    '''



def weird_difference_01(x:float, y:float, max_referencia:float) -> float:
    '''Retorna un valor proporcional a la diferència entre x i y entre 0 i 1. A mesura que la diferència es fa gran, tendeix a 1'''

    c = 3
    dif = abs(x-y)
    return 1 - pow(e, -c*dif/max_referencia  )






def common_elements(l1:list[str], l2:list[str]) -> int:
    
    n_total = len(l1)+len(l2)
    s:set[str] = set()
    for x in l1: s.add(x) 
    for x in l2: s.add(x)

    return n_total - len(s)


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


def exp_to_int(experience:str) -> int:
    '''Transforma la variable year_of_study a un interger'''

    match experience:
        case "Beginner": return 0
        case "Intermediate": return 1
        case "Advanced": return 2
        case _: return -1