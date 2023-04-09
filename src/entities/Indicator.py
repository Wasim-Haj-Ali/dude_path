from pydantic import BaseModel

class Indicator(BaseModel):
    slug: str
    content: str