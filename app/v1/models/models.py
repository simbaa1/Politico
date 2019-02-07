

class Parties:

    def __init__(self, id, name, hq_address, logo_url, chairperson):
        self.id  = id
        self.name = name
        self.hq_address = hq_address
        self.logo_url = logo_url
        self.chairperson = chairperson


    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return repr(self.__dict__)



    