class FileUtils:
    @staticmethod
    def getProjectRootDir():
        abspath = os.path.abspath('..')
        return abspath