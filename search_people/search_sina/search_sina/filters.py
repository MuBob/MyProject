class SinaFilters:
    def __init__(self):
        self.sex_in = ["女"]
        self.sex_out = ["女"]
        self.addres_in = ['浙江','上海','杭州']


    def filterSexIn(self, str=str()):
        for cur in self.sex_in:
            if str.__contains__(cur):
                return True
            else:
                pass
        return False

    def filterAddresIn(self, str=str()):
        for cur in self.addres_in:
            if str.__contains__(cur):
                return True
            else:
                pass
        return False

    def filterSexOut(self, str=str()):
        for cur in self.sex_out:
            if str.__contains__(cur):
                return False
            else:
                pass
        return True

