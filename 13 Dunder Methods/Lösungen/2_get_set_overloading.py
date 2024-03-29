"""
Wir bleiben bei dem Beispiel mit unserer eigenen Liste: MyList.
Was bisher noch nicht möglich ist:
l1 = MyList()
l1 = [1, 2, 3]
l1[0] # sollte 1 liefern

Aufgabe:
Implemntiere diese beiden Funktionalitäten, indem du die __getitem__ und __setitem__ Methode
überlädst.
"""
class MyList:

    def __init__(self, l: list[int|float] = None):
        self.items = l or []

    def append(self, item):
        self.items.append(item)

    def extend(self, l: 'MyList'):
        self.items.extend(l.items)

    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, item):
        self.items[index] = item


l1 = MyList([1, 2])
assert l1[0] == 1

l1[0] = 99
assert l1[0] == 99
