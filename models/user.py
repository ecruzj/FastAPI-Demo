import sys
sys.path.append("..") # Adds higher directory to python modules path.

from dataclasses import dataclass, field

@dataclass
class User:
    user_id: int #= field(init=False)
    user_name: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool #= field(default=True)

    def __init__(self, user_id, user_name, first_name, last_name, hashed_password):
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.hashed_password = hashed_password
        self.is_active = True
