class FileOut:
    __file__

    def __init__(self, filePath) -> None:
        super().__init__()
        self.__file__ = open(file=filePath, mode="w+", encoding='utf-8')

    def out(self, content):
        if(content!=None):
            self.__file__.write(content)
        self.__file__.close()


