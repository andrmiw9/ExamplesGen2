class A:
    perem = 1

    def __init__(self, _perem):
        self.perem = _perem
        pass

    def sayhello(self):
        print("@")
        pass


exA = A(16)
print(exA.perem)
