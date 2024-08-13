class Emp:
    name="Raja"

    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i

e=Emp()
print(e.name)
print(len(e))