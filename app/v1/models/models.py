

class Parties:

    def __init__(self, id=None, name=None, hq_address=None, logo_url=None, chairperson=None):
        self.id  = id
        self.name = name
        self.hq_address = hq_address
        self.logo_url = logo_url
        self.chairperson = chairperson

    def __setitem__(self, k, v):
        self.k = v

    def __getitem__(self, item):
        return getattr(self, item)
    
    def __len__(self):
        return 0

    def __repr__(self):
        return repr(self.__dict__)


class Offices:
    
    def __init__(self, id, name, type):
        self.id  = id
        self.name = name
        self.type = type

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return repr(self.__dict__)



    