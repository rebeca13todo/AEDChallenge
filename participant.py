import json
import pathlib
import uuid
from dataclasses import dataclass
from typing import Dict, List, Literal


@dataclass
class Participant:
    id: uuid.UUID  # Identificador únic

    # Dades personals
    name: str
    email: str
    age: int
    year_of_study: Literal["1st year", "2nd year", "3rd year", "4th year", "Masters", "PhD"]
    shirt_size: Literal["S", "M", "L", "XL"]
    university: str
    dietary_restrictions: Literal["None", "Vegetarian", "Vegan", "Gluten-free", "Other"]

    # Habilitat programant i experiència
    programming_skills: Dict[str, int]
    experience_level: Literal["Beginner", "Intermediate", "Advanced"]
    hackathons_done: int

    # Interessos, preferències...
    interests: List[str]
    preferred_role: Literal[
        "Analysis", "Visualization", "Development", "Design", "Don't know", "Don't care"
    ]
    objective: str
    interest_in_challenges: List[str]
    preferred_languages: List[str]
    friend_registration: List[uuid.UUID]
    preferred_team_size: int
    availability: Dict[str, bool]

    # Descripció del participant
    introduction: str
    technical_project: str
    future_excitement: str
    fun_fact: str

    def __hash__(self):
        # Usem el 'id' que és únic
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Participant):
            return self.id == other.id
        return False


def load_participants(path: str) -> List[Participant]:
    if not pathlib.Path(path).exists():
        raise FileNotFoundError(
            f"The file {path} does not exist, are you sure you're using the correct path?"
        )
    if not pathlib.Path(path).suffix == ".json":
        raise ValueError(
            f"The file {path} is not a JSON file, are you sure you're using the correct file?"
        )

    return [Participant(**participant) for participant in json.load(open(path))]
