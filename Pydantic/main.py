from models.user import User

user0 = User(
    name = "Salah",
    email = "salah@gmail.com",
    account_id = 12345
)

# Or unpacking a dictionary

user_data = {
    'name': 'Salah',
    'email': 'salah@gmail.com',
    'account_id': 12345
}

user1 = User(**user_data)

user = User(name = 'Ali', email = 'ali', account_id = -12)
print(user)

# Convert from Model to JSON
user_json_str = user.model_dump_json()
print(user_json_str)

# Converting from JSON to Model
json_str = {"name": "Ali", "email": "ali@gmail.com", "account_id": 1234}
user = user.parse_raw(json_str)