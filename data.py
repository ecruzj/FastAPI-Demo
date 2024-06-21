import sys
import uuid

from models.user_address import UserAddress

sys.path.append("..") # Adds higher directory to python modules path.

from models.company import Company
from models.user import User
from models.user_poc import UserPoc
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

def generate_user_poc_data():
    return [
        UserPoc('0bb05161-0ac1-4dea-9d94-76cfb4901e77', 'ecruzj@outlook.com', '123', 'Josue', 'Cruz', 'C0876620',
                'BN00873', 'GSIC', '455-873-9873', '222 Jarvis St.', '263 Monte Carlo Drive.'),
        UserPoc('0bb05161-0ac1-4dea-9d94-76cfb4901e2e', 'john.doe@example.com', 'securepassword1', 'John', 'Doe', '123456789', 'BN00001', 'Doe Enterprises', '123-456-7890', '123 Business St.', '456 Mailing Ave.'),
        UserPoc('24d89db3-f4ba-4ede-a336-aa115bc4f195', 'jane.doe@example.com', 'securepassword2', 'Jane', 'Doe', '987654321', 'BN00002', 'Doe Industries', '321-654-0987', '124 Business St.', '457 Mailing Ave.'),
        UserPoc('2be40cb6-4bfe-490d-a21a-62aab0f424a2', 'alice.smith@example.com', 'securepassword3', 'Alice', 'Smith', '234567890', 'BN00003', 'Smith LLC', '456-789-0123', '125 Business St.', '458 Mailing Ave.'),
        UserPoc('3381fe80-a101-43bb-9324-7e064bf0547c', 'bob.johnson@example.com', 'securepassword4', 'Bob', 'Johnson', '345678901', 'BN00004', 'Johnson Corp.', '567-890-1234', '126 Business St.', '459 Mailing Ave.'),
        UserPoc('3d47f066-49ae-48c1-ae80-e855f4948361', 'charlie.brown@example.com', 'securepassword5', 'Charlie', 'Brown', '456789012', 'BN00005', 'Brown & Co.', '678-901-2345', '127 Business St.', '460 Mailing Ave.'),
        UserPoc('57784562-5a72-4a91-be4e-4b8d070e467b', 'diana.ross@example.com', 'securepassword6', 'Diana', 'Ross', '567890123', 'BN00006', 'Ross Inc.', '789-012-3456', '128 Business St.', '461 Mailing Ave.'),
        UserPoc('578079ea-1c13-4546-ba4e-458b82c96d86', 'edward.king@example.com', 'securepassword7', 'Edward', 'King', '678901234', 'BN00007', 'King Enterprises', '890-123-4567', '129 Business St.', '462 Mailing Ave.'),
        UserPoc('85527d7e-17aa-44bb-9f7a-c88b652c827c', 'fiona.hill@example.com', 'securepassword8', 'Fiona', 'Hill', '789012345', 'BN00008', 'Hill Ltd.', '901-234-5678', '130 Business St.', '463 Mailing Ave.'),
        UserPoc('8d8b13f5-fdfd-4711-9cfb-d4719843ca6b', 'vladberest@gmail.com', 'securepassword9', 'Vladyslav', 'Berestetskyi', '890123456', 'BN00009', 'Washington Group', '012-345-6789', '131 Business St.', '464 Mailing Ave.'),
        UserPoc('b01656c0-5621-4427-afe4-2e19d8656e1a', 'henry.adams@example.com', 'securepassword10', 'Henry', 'Adams', '901234567', 'BN00010', 'Adams & Partners', '123-456-7891', '132 Business St.', '465 Mailing Ave.'),
    ]

USERS_POC = generate_user_poc_data()

def get_new_user_id_poc(new_userpoc: UserPoc):
    new_userpoc.userid = str(uuid.uuid4())
    return new_userpoc

def generate_user_address_data():
    return [
        UserAddress('0bb05161-0ac1-4dea-9d94-76cfb4901e2e', '101', '456', 'Maple Street', 'PO1234', '12345',
                    'Springfield', 'Illinois', 'USA', '555-1234', '101', '555-5678'),
        UserAddress('24d89db3-f4ba-4ede-a336-aa115bc4f195', '102', '457', 'Oak Street', 'PO1235', '12346',
                    'Shelbyville', 'Indiana', 'USA', '555-1235', '102', '555-5679'),
        UserAddress('2be40cb6-4bfe-490d-a21a-62aab0f424a2', '103', '458', 'Pine Street', 'PO1236', '12347',
                    'Capital City', 'Ohio', 'USA', '555-1236', '103', '555-5680'),
        UserAddress('3381fe80-a101-43bb-9324-7e064bf0547c', '104', '459', 'Cedar Street', 'PO1237', '12348',
                    'Ogdenville', 'Kentucky', 'USA', '555-1237', '104', '555-5681'),
        UserAddress('3d47f066-49ae-48c1-ae80-e855f4948361', '105', '460', 'Birch Street', 'PO1238', '12349',
                    'North Haverbrook', 'Missouri', 'USA', '555-1238', '105', '555-5682'),
        UserAddress('57784562-5a72-4a91-be4e-4b8d070e467b', '106', '461', 'Elm Street', 'PO1239', '12350', 'Brockway',
                    'Michigan', 'USA', '555-1239', '106', '555-5683'),
        UserAddress('578079ea-1c13-4546-ba4e-458b82c96d86', '107', '462', 'Willow Street', 'PO1240', '12351', 'Monroe',
                    'Georgia', 'USA', '555-1240', '107', '555-5684'),
        UserAddress('85527d7e-17aa-44bb-9f7a-c88b652c827c', '108', '463', 'Ash Street', 'PO1241', '12352',
                    'Springfield', 'California', 'USA', '555-1241', '108', '555-5685'),
        UserAddress('8d8b13f5-fdfd-4711-9cfb-d4719843ca6b', '109', '464', 'Cherry Street', 'PO1242', '12353',
                    'Springfield', 'Nevada', 'USA', '555-1242', '109', '555-5686'),
        UserAddress('b01656c0-5621-4427-afe4-2e19d8656e1a', '110', '465', 'Peach Street', 'PO1243', '12354',
                    'Springfield', 'Texas', 'USA', '555-1243', '110', '555-5687'),
    ]

USERS_ADDRESS = generate_user_address_data()