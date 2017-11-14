class Filter:
    def __init__(self):
        self.title_ins=[]
        self.title_outs = ["技术","英文","销售","运营"]
        self.location_ins = ["海淀"]
        self.money_rang=[3000]
        self.treatement_outs=["绩效"]
        self.treatment_ins=[]
        self.description_ins=[]
        self.description_outs=["本科","形象","气质","销售","跟单","弹性工作"]

    def filterTitleIn(self, str=str()):
        for cur in self.title_ins:
            if str.__contains__(cur):
                return True
            else:
                pass
        return False

    def filterTitleOut(self, str=str()):
        for cur in self.title_outs:
            if str.__contains__(cur):
                return False
            else:
                pass
        return True

    def filterLocation(self, str=str()):
        for cur in self.location_ins:
            if str.__contains__(cur):
                return True
            else:
                pass
        return False

    def filterMoney(self, str=str(), containNone=True):
        if str.__contains__("面议"):
            return containNone
        low=int(str.split("-")[0].strip())
        high=int(str.split("-")[1].rstrip("元/月").strip())
        if low>=self.money_rang[0]:
            return True
        else:
            if len(self.money_rang)>1:
                if high<=self.money_rang[1]:
                    return True
                else:
                    return False
            return False

    def filterTreatment(self, str=str()):
        is_contain=True
        for cur in self.treatement_outs:
            if str.__contains__(cur):
                is_contain=False
                break
            else:
                pass
        for cur in self.treatment_ins:
            if str.__contains__(cur):
                pass
            else:
                is_contain=False
                break
        return is_contain

    def filterDescription(self, str=str()):
        is_contain = True
        for cur in self.description_outs:
            if str.__contains__(cur):
                is_contain = False
                break
            else:
                pass
        for cur in self.description_ins:
            if str.__contains__(cur):
                pass
            else:
                is_contain = False
                break
        return  is_contain