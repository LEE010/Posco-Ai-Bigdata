class Set:
    def __init__(self, member=[]):
        self.member = member

    def __add__(self, set):
        return self.union(set)

    def __sub__(self, set):
        #difference
        return self.difference(set)

    def __truediv__(self, set):
        #intersection
        self.intersection(set)
        return

    def append(self, a):
        if (a in self.member) == False:
            self.member.append(a)

    def delete(self, a):
        if a in self.member:
            self.member.remove(a)
        else:
            raise KeyError

    def union(self, s2):
        union = self.member
        for i in s2.member:
            if i in self.member:
                continue
            else:
                union.append(i)
        return union

    def intersection(self, s2):
        inters = []

        for i in s2.member:
            if i in self.member:
                inters.append(i)
            else:
                continue
        return inters

    def difference(self, s2):
        diff = self.member

        for i in s2.member:
            if i in diff:
                diff.remove(i)
            else:
                continue
        return diff

a = Set([1,2,3])
b = Set([2, 3, 4])

c = a.union(b)
print(c)

d = a.difference(b)
print(d)

e = a.intersection(b)
print(e)

f = a+b
print(f)

g = a-b
print(g)

h = a/b
print(h)

a.member
b.member
