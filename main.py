
import participant as p

path:str = "data/datathon_participants.json"
participants = p.load_participants(path)

print(len(participants))

#print(participants)