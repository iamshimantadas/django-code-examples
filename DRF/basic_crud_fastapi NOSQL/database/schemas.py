from pydantic import BaseModel


class Students(BaseModel):
    name : str
    phone : int
    address : str
    email : str

class UpdateStudent(BaseModel):
    name : str | None = None
    phone : int  | None = None
    address : str | None = None
    email : str | None = None
    
