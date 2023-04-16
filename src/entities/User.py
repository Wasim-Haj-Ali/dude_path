import uuid
import re
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

    def __init__(self, slug: str, username: str, password: list):
        super().__init__(slug=slug, username=username, password=password)
        
        unique_suffix = str(uuid.uuid4())

        # regex that accepts only letters and numbers
        pattern = r"^[a-zA-Z0-9]+$"

        username_sanitized = re.sub(pattern, "", self.username).lower()
         
        self.slug = username_sanitized + '-' + unique_suffix