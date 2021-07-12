class Supplier:
    def __init__(self, company_name, company_origin, id = None):
        self.company_name = company_name
        self.company_origin = company_origin
        self.id = id


def company_full(self):
    return f"{self.company_name} {self.company_origin}"


