class MySingleton:
    __instance = None
    
    def __init__(self):
        if MySingleton.__instance != None:
            raise Exception("Singleton instance already exists")
        else:
            MySingleton.__instance = self
    
    @staticmethod
    def get_instance():
        if MySingleton.__instance == None:
            MySingleton()
        return MySingleton.__instance

if __name__ == '__main__':
    s1 = MySingleton.get_instance()
    s2 = MySingleton.get_instance()

    print(s1 == s2)  # Output: True
