#!/usr/bin/python3 

def upcase_it(x) :
    return x.upper()

print(upcase_it("hello"))


class Me :
    def upcase_it(self, x) :
        return x.upper()

m = Me()
print(m.upcase_it("hello by class"))