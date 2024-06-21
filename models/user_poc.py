from dataclasses import dataclass

@dataclass
class UserPoc:
    userid: str
    email__address: str
    password: str
    first__name: str
    last__name: str
    business__operating__number: str
    business__number: str
    business__legal__name: str
    contact__number: str
    business__address: str
    mailing__address: str

    def __init__(self, userid, email__address, password, first__name, last__name, business__operating__number,
                 business__number, business__legal__name, contact__number, business__address, mailing__address):
        self.userid = userid
        self.email__address = email__address
        self.password = password
        self.first__name = first__name
        self.last__name = last__name
        self.business__operating__number = business__operating__number
        self.business__number = business__number
        self.business__legal__name = business__legal__name
        self.contact__number = contact__number
        self.business__address = business__address
        self.mailing__address = mailing__address