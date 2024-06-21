from dataclasses import dataclass

@dataclass
class UserAddress:
    userId: str
    Unit__number__mail: str
    Street__number__mail: str
    Street__name__mail: str
    PO__Box__mail: str
    Postal__zip__code__mail: str
    Citytown__mail: str
    Province__state__mail: str
    Country__mail: str
    Telephone__number__mail: str
    Extension__mail: str
    Fax__number__mail: str

    def __init__(self, userId: str, Unit__number__mail: str, Street__number__mail: str, Street__name__mail: str,
                 PO__Box__mail: str, Postal__zip__code__mail: str, Citytown__mail: str, Province__state__mail: str,
                 Country__mail: str, Telephone__number__mail: str, Extension__mail: str, Fax__number__mail: str):
        self.userId = userId
        self.Unit__number__mail = Unit__number__mail
        self.Street__number__mail = Street__number__mail
        self.Street__name__mail = Street__name__mail
        self.PO__Box__mail = PO__Box__mail
        self.Postal__zip__code__mail = Postal__zip__code__mail
        self.Citytown__mail = Citytown__mail
        self.Province__state__mail = Province__state__mail
        self.Country__mail = Country__mail
        self.Telephone__number__mail = Telephone__number__mail
        self.Extension__mail = Extension__mail
        self.Fax__number__mail = Fax__number__mail