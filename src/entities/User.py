import uuid
import re
from pydantic import BaseModel

class User(BaseModel):
    user_name: str
    password: str

    @property
    def slug(self):
        unique_suffix = str(uuid.uuid4())

        # regex that accepts only letters and numbers
        pattern = r"^[a-zA-Z0-9]+$"

        user_name_sanitized = re.sub(r"[^a-zA-Z0-9]", "", self.user_name).lower()
         
        return user_name_sanitized + '-' + unique_suffix