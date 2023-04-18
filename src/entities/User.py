import uuid
import re
from pydantic import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    username: str
    password: str
    slug: str = ""

    def __init__(self, username: str, password: list):
        super().__init__(username=username, password=password)
        
        unique_suffix = str(uuid.uuid1().hex)

        # # regex that accepts only letters and numbers
        # pattern = r"^[a-zA-Z0-9]+$"

        # username_sanitized = re.sub(pattern, "", self.username).lower()
        username_sanitized = self.username


        # self.slug = username_sanitized + '_' + unique_suffix
        self.slug = username_sanitized + '_' + unique_suffix