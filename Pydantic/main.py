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