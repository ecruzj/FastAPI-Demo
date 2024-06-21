from dataclasses import dataclass

@dataclass
class UserPoc:
    userid: str
    Email__address: str
    Password: str
    First__name: str
    Last__name: str
    Business__operating__number: str
    Business__number: str
    Business__legal__name: str
    Contact__number: str
    Business__address: str
    Mailing__address: str

    def __init__(self, userid, Email__address, Password, First__name, Last__name, Business__operating__number,
                 Business__number, Business__legal__name, Contact__number, Business__address, Mailing__address):
        self.userid = userid
        self.Email__address = Email__address
        self.Password = Password
        self.First__name = First__name
        self.Last__name = Last__name
        self.Business__operating__number = Business__operating__number
        self.Business__number = Business__number
        self.Business__legal__name = Business__legal__name
        self.Contact__number = Contact__number
        self.Business__address = Business__address
        self.Mailing__address = Mailing__address