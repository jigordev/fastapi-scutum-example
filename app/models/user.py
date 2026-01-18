from dataclasses import dataclass

@dataclass
class User:
    id: int
    email: str
    password: str
    posts: list["Post"]
    role: str = "admin"