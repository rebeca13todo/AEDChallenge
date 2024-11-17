
import participant as p
from math import pow, e

#Valores customizables que representan la importancia de cada cosa
# ----------------------------------------------------------------#
AGE_COEFICIENT = 0
YOS_COEFICIENT = 4
UNIVERSITY_COEFICIENT = 1
EXPERIENCE_COEFICIENT = 5
INTERESTS_COEFICIENT = 2
DIFERENT_ROLES_COEFICIENT = 3
SAME_OBJECTIVE_COEFICIENT = 5
HACKATONS_COUNT_COEFICIENT = 1
TEAM_SIZE_COEFICIENT = 2
FRIENDS_COEFICIENT = 5
INTERESTS_CHALLENGES_COEFICIENT = 4
LANGUAGES_COEFICIENT = 4
PROGRAMMING_SKILL_COEFFICIENT = 3
AVAILABILITY_COEFFICIENT = 2
# ----------------------------------------------------------------#

#Estos parámetros sirven para la función
max_age_diference = 10
max_year_study_diference = 5
max_common_interests = 3
max_hackatons_done_difference = 10

def difference_01(x:float, y:float, max_referencia:float) -> float:
    """
    Retorna un valor proporcional a la diferència entre x i y entre 0 i 1. 
    A mesura que la diferència es fa gran, tendeix a 1
    """

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


def friends(p1: p.Participant, p2: p.Participant) -> int:
    """
    Funció que retorna la distància entre dos participants en funció de si són amics o no.
    """

    if p2.id in p1.friend_registration:
        return 1
    return 0

def skill(skills: dict[str, int]) -> int:
    """
    Calcula el nivell d'experiència d'una persona en diferents llenguatges de programació.
    """
    total_points = 0
    for skill, points in skills.items():
        total_points += points
    return total_points



def available(dict1: dict[str, bool], dict2: dict[str, bool]) -> float:
    """
    Calculem un percentatje en base 0-1 segons el nombre de jornades en la que
    dos participants coincideixen.
    """

    # Asegurarse de que estamos comparando solo las claves que existen en ambos diccionarios
    common_keys = set(dict1.keys()).intersection(set(dict2.keys()))

    if not common_keys:
        # Si no hay claves comunes, no se puede calcular la similitud
        return 0.0

    # Calcular cuántos valores coinciden en ambas claves comunes
    matching_count = sum(1 for key in common_keys if dict1.get(key) == dict2.get(key))
    
    # Calcular el "porcentaje" de coincidencias dividiendo por el total de claves comunes
    similarity = matching_count / len(common_keys)
    
    return similarity



def distancia(p1:p.Participant, p2:p.Participant) -> float:
    """
    Recibe dos participantes y devuelve una distancia que es menor cuanto más similares/afines son
    """

    d:float = 0

    #Age
    d += difference_01(p1.age, p2.age, max_age_diference) * AGE_COEFICIENT

    #Year of study
    d += abs( yos_to_int(p1.year_of_study) - yos_to_int(p2.year_of_study))/max_year_study_diference * YOS_COEFICIENT

    #University
    d += int( p1.university==p2.university ) * UNIVERSITY_COEFICIENT

    #Experience
    d += abs( exp_to_int(p1.experience_level) - exp_to_int(p2.experience_level))/2 * EXPERIENCE_COEFICIENT

    #Interests
    d += common_elements(p1.interests, p2.interests)/max_common_interests * INTERESTS_COEFICIENT

    #Preferred role
    d += int( p1.preferred_role != p2.preferred_role ) * DIFERENT_ROLES_COEFICIENT

    #Objective
    d += abs(skill(p1.programming_skills) - skill(p2.programming_skills)) * SAME_OBJECTIVE_COEFICIENT

    #Hackatons done
    d += difference_01(p1.hackathons_done, p2.hackathons_done, max_hackatons_done_difference) * HACKATONS_COUNT_COEFICIENT

    #Preferred team size
    #d += ((p1.preferred_team_size + p2.preferred_team_size) / max(p1.preferred_team_size, p2.preferred_team_size)*2) * TEAM_SIZE_COEFICIENT

    #Friend registration
    d += friends(p1, p2) * FRIENDS_COEFICIENT

    #Interest in challenges
    d += common_elements(p1.interest_in_challenges, p2.interest_in_challenges)/max_common_interests *  INTERESTS_CHALLENGES_COEFICIENT

    #Preferred languages
    d += common_elements(p1.preferred_languages, p2.preferred_languages) * LANGUAGES_COEFICIENT

    #Availability
    d += available(p1.availability, p2.availability) * AVAILABILITY_COEFFICIENT

    return d


# objective, availability
