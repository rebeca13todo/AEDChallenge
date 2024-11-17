<div align="center">
    <img src="public/aed_logo.png" width="200" alt="AED logo" />
    <h1>Repte AED - Datathon FME 2024</h1>
</div>

## Resum

En el marc del *Datathon FME 2024*, el repte AED proposa desenvolupar un sistema innovador que ajudi els futurs participants a trobar els companys de equip perfectes, basant-se en les seves habilitats tècniques i objectius del hackathon. L'objectiu és facilitar la connexió entre els participants amb interessos similars i millorar l'experiència del *Datathon*.

Aquesta solució transformarà la manera com les generacions futures d'entusiastes de dades es connecten i col·laboren en equip. Amb aquest sistema, busquem que cada participant pugui trobar el seu equip ideal per aconseguir els seus objectius, ja sigui per guanyar premis o per aprendre noves habilitats.

🔗 Repositori del repte: [AED Challenge Repository](https://github.com/data-students/AEDChallenge)

## Resolució del repte

# Plantejament
A l'hora de plantejar el problema, vam començar amb una pluja d'idees sobre com haruiem de llegir les dades, quines característiques tenir en compte, com repartir el treball... 

A la primera conclusió que varem arribar va ser que la millor manera de poder relacionar a les persones entre sí tenint en compte els seus atributs va ser mitjançant un graf on cada node representesi una persona i cada aresta la relació d'un participant amb l'altre. El pes de cada aresta es calcularia en funció dels atributs coincidents.

Amb això ja podiem posar-nos a treballar.

# Creació del graf
Crear un graf on cada persona fos un node va ser fàcil al igual que afegir una aresta entre cada participant. El que va requerir una mica més de feina va ser el fet de calcular el pes de cada aresta. Havíem de plantejar-nos què tenir en compte a l'hora de designar una importància a cada atribut i com detectar si aquest era coincident per cada dos participants diferents.

Com tot requeria d'una funció massa llarga vam decidir començar-la en un fitxer diferent al principal. 

La nostra idea principal va ser crear una variable *d* que simbolitzaria el pes de la aresta. S'inicialitzaria nul·la i a mesura que anèssim comparant atributs, aniria augmentant el valor o es quedaria igual. 

Vam definir els valors de la següent manera:
``` bash
# Valors personalitzables que marquen la importància de cada atribut en una escala
# de l'1 al 5.
# ----------------------------------------------------------------#
AGE_COEFICIENT = 0
YOS_COEFICIENT = 4
UNIVERSITY_COEFICIENT = 1
EXPERIENCE_COEFICIENT = 5
INTERESTS_COEFICIENT = 2
DIFERENT_ROLES_COEFICIENT = 3
SAME_OBJECTIVE_COEFICIENT = 5
HACKATONS_COUNT_COEFICIENT = 1
FRIENDS_COEFICIENT = 5
INTERESTS_CHALLENGES_COEFICIENT = 4
LANGUAGES_COEFICIENT = 4
PROGRAMMING_SKILL_COEFFICIENT = 3
AVAILABILITY_COEFFICIENT = 2
# ----------------------------------------------------------------#
```
Òbviament aquests són valors arbitraris basats en el nostre criteri. Ens agradaba especialment la idea de que els valors d'aquests coeficients siguin fàcils de trobar i personalitzables per si fos necessari canviar-los més endavant.

A continuació vam fer la nostra funció principal del fitzer, que iterava amb *d* i retornava el seu valor final. Cal destacar la forma de sumar valors a la variable: multiplicar el valor del coeficient per un decimal de 0 a 1 en base a l'afinitat entre dos participants segons l'atribut que estiguessim comparant en aquella linia.

# Creació dels equips
Per a la creació del graf es va emplear un algorisme de *clustering* amb una limitació: el tamany dels equips. Per tal de que cada equip tingués quatre integrants i no més, vam haver de modificar l'algorisme per complir aquests requeriments. 

# Creació de la interfície
Després d'investigar una mica sobre l'eina de Streamlit, vam aconseguir finalitzar el projecte amb un plot senzill en una taula amb una fila per equip.