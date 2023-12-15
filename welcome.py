class Welcome:

    @staticmethod
    def sayWelcome():
        f = open("README.md", "r", encoding="utf-8")
        print(f.read())