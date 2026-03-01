from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

@field_validator("account_id")
def validate_account_id(cls, value):
    if value <= 0:
        raise ValueError(f"account_id must be positive: {value}")
    return value

user = User(name = 'Ali', email = 'ali', account_id = -12)
print(user)

# Convert from Model to JSON
user_json_str = user.model_dump_json()
print(user_json_str)

# Converting from JSON to Model
json_str = {"name": "Ali", "email": "ali@gmail.com", "account_id": 1234}
user = user.parse_raw(json_str)