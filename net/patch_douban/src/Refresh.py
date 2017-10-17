class Refresh:
    def getStrFromList(self, list):
        comments = ''
        for k in range(len(list)):
            comments = comments + (str(list[k])).strip()
        return comments

