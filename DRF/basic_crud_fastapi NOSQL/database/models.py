
from beanie import Document

class Student(Document):
    name : str
    phone : int
    address : str
    email : str
    