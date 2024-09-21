


from pydantic import BaseModel


class readUserRequest(BaseModel):
    user_id: int
