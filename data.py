import sys
sys.path.append("..") # Adds higher directory to python modules path.

from models.company import Company
from models.user import User
from utils import get_password_hash

USERS = [
    User(1, "ecruzj", "Josue", "Cruz", get_password_hash("testing1")),
    User(2, "kmbappe", "Kylian", "Mbappe", get_password_hash("testing2")),
    User(3, "ehaaland", "Erlin", "Haaland", get_password_hash("testing3")),
    User(4, "lukm", "Luka", "Modric", get_password_hash("testing4")),
    User(5, "fvalverde", "Fede", "Valverde", get_password_hash("testing5")),
    User(6, "tkroos", "Tonni", "Kroos", get_password_hash("testing6")),
    User(7, "cr7", "Cristiano", "Ronaldo", get_password_hash("testing7")),
    User(8, "zzidane", "Zinedine", "Zidane", get_password_hash("testing8")),
    User(9, "lsuarez", "Luis", "Suarez", get_password_hash("testing9")),
    User(10, "lmessi", "Lionel", "Messi", get_password_hash("testing10")),
]

def get_new_user_id(new_user: User):
    new_user.user_id = 1 if len(USERS) == 0 else USERS[-1].user_id + 1
    return new_user

COMPANIES = [
    Company(1, "Starbucks", "7080 Warden Ave., Markham", "L3R 5Y2"),
    Company(2, "IKEA", "15 Provost Drive, North York", "M2K 2X9"),
    Company(3, "CN TOWER", "290 Bremner Blvd, Toronto", "M5V 3L9"),
    Company(4, "Pizza Pizza", "208 Queens Quay W, Toronto", "M5J 2Y5"),
    Company(5, "Tim Hortorns", "200 Bay St, Toronto", "M5J 2J1"),
    Company(6, "Subway", "275 Dundas St W, Toronto", "M5T 3K1"),
    Company(7, "GSIC", "222 Jarvis St, Toronto, Floor 5ht", "M7A 0B6"),
    Company(8, "Scotiabank", "2900 Warden Ave, Scarborough", "M1W 2S8"),
    Company(9, "The Halal Stop", "1733 Eglinton Ave E, North York", "M4A 1J8"),
    Company(10, "Red Lobster", "3252 Sheppard Ave E, Scarborough", "M1T 3K3"),
]

def get_new_company_id(new_company: Company):
    new_company.company_id = 1 if len(COMPANIES) == 0 else COMPANIES[-1].company_id + 1
    return new_company