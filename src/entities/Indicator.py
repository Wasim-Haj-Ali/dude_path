from pydantic import BaseModel

class Indicator(BaseModel):
    slug: str
    name: str
    userslug: str
    content: str = ""