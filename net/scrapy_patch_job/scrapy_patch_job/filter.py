class Filter:
    def __init__(self):
        self.title_ins=[]
        self.title_outs = ["技术","英文","销售","运营"]
        self.location_ins = ["海淀"]
        # self.money_rang=[3000]
        self.money_rang=[15000, 20000]
        self.treatement_outs=["绩效"]
        self.treatment_ins=[]
        self.description_ins=[]
        self.description_outs=["本科","形象","气质","销售","跟单","弹性工作"]
        self.company_description_size_range=[50,1000]
        self.company_description_nature_outs=[]
        self.company_description_nature_ins=["国企","企事业单位"]

    def filterTitleIn(self, str=str()):
        for cur in self.title_ins:
            if cur in str:
                return True
            else:
                pass
        return False

    def filterTitleOut(self, str=str()):
        for cur in self.title_outs:
            if cur in str:
                return False
            else:
                pass
        return True

    def filterLocation(self, str=str()):
        for cur in self.location_ins:
            if cur in str:
                return True
            else:
                pass
        return False

    def filterMoney(self, str=str(), containNone=True):
        if "面议" in str:
            return containNone
        low=int(str.split("-")[0].strip())
        high=int(str.split("-")[1].rstrip("元/月").strip())
        if low>=self.money_rang[0]:
            if len(self.money_rang)>1:
                if high<=self.money_rang[1]:
                    return True
                else:
                    return False
            else:
                return True
        else:
            if len(self.money_rang)>1:
                if high<=self.money_rang[1]:
                    return False
                else:
                    return False
            else:
                return False

    def filterTreatment(self, str=str()):
        is_contain=True
        for cur in self.treatement_outs:
            if cur in str:
                is_contain=False
                break
            else:
                pass
        for cur in self.treatment_ins:
            if cur in str:
                pass
            else:
                is_contain=False
                break
        return is_contain

    def filterDescription(self, str=str()):
        is_contain = True
        for cur in self.description_outs:
            if cur in str:
                is_contain = False
                break
            else:
                pass
        for cur in self.description_ins:
            if cur in str:
                pass
            else:
                is_contain = False
                break
        return  is_contain


    def filterCompanySize(self, str=str(), containNone=True):
        if "null" in str:
            return containNone
        try:
            low = int(str.split("-")[0].strip())
            high = int(str.split("-")[1].rstrip("人").strip())
            if low >= self.company_description_size_range[0]:
                if len(self.company_description_size_range) > 1:
                    if high <= self.company_description_size_range[1]:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                if len(self.company_description_size_range) > 1:
                    if high <= self.company_description_size_range[1]:
                        return False
                    else:
                        return False
                else:
                    return False
        except IndexError:
            low = int(str.rstrip("人").strip())
            if low >= self.company_description_size_range[0]:
                return True
            else:
                return False

    def filterCompanyNature(self, str=str()):
        is_contain = True
        for cur in self.company_description_nature_outs:
            if cur in str:
                is_contain = False
                break
            else:
                pass
        for cur in self.company_description_nature_ins:
            if cur in str:
                pass
            else:
                is_contain = False
                break
        return is_contain