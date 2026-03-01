from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int


user = User(name = 'Ali', email = 'ali@gmailcom', account_id = 'hello')
print(user)