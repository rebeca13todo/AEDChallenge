from rich import print

from participant import load_participants, Participant

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

#print(participants[3].id)
#hola

#knn

def programacio(participants: list[Participant]):

    r = []

    for p in participants:
        for i in p.programming_skills:
            