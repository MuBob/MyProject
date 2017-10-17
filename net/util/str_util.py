class StrUtil:
    @staticmethod
    def list2Str(list, splite=""):
        desc = ""
        for str in list:
            replace = str.replace('  ','').replace('\r', '').replace('\n', '').replace('\t', '').replace('\xa0', '')
            if replace.__len__()>0:
                desc += replace+splite
            else:
                pass
        return desc
