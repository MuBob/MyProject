class Filter:
    def __init__(self):
        self.in_leans=["合租"]
        self.money_rang = [1000,3000]
        pass

    def filtLeanIn(self, str=str()):
        for cur in self.in_leans:
            if str.__contains__(cur):
                return True
            else:
                pass
        return False

    def filtMoney(self, str=str(), containNone=True):
        if str.__contains__("面议"):
            return containNone
        target=int(str.split("元/月")[0].strip())
        # high=int(str.split("-")[1].rstrip("元/月").strip())
        if target>=self.money_rang[0]:
            return True
        else:
            if len(self.money_rang)>1:
                if target<=self.money_rang[1]:
                    return True
                else:
                    return False
        return False


