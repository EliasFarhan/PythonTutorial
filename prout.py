

class Prout:
    b = 2

    def __init__(self):
        self.a = 3
        self.important = 10

    def prout(self):
        print("Prout Class "+str(self.a)+" "+str(Prout.b))

class Prout2 (Prout):

    def __init__(self):
        Prout.__init__(self)
        self.a = "Hello"

    def prout(self):
        Prout.prout(self)
        print("Prout 2")


def prout():
    print("Prout")


def divide_by_2(elem):
    return elem/2.0


if __name__ == "__main__":
    p = Prout()

    p.a = 4
    if p.a == 4:
        pass
    elif p.b == 3:
        pass
    else:
        pass
    for i in range(0,10):
        print(i)

    tab = []
    tab.append(3)
    tab.append(1.0)
    tab.append(2.5)


    for i in range(0,6):
        print(tab[i])

    print(tab)
    p.prout()
