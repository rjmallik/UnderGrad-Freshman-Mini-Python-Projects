class Tree:
    def __init__(self, key):
        self.key = key
        self.children = []
        
    def setRootKey(self, key):
        self.key = key

    def getRootKey(self):
        return self.key

    def getChildren(self):
        return self.children

    def addChild(self, node):
        self.children.append(node)

    def getChild(self, key):
        for kid in self.children:
            if kid.getRootKey() == key:
                return kid
        return None

    def __str__(self):
        x = f"{self.key}["
        for kid in self.children:
            x += str(kid) + ""
        x += "]"
        return x
    
if __name__ == '__main__':
    
    r = Tree('a')
    print(r.getRootKey())
    assert r.getRootKey() == 'a'
    print(r)
    assert str(r) == 'a[]'
    
    r.addChild(Tree('b'))
    r.addChild(Tree('c'))
    print(r)
    assert str(r) == 'a[b[]c[]]'
    
    r.getChild('b').addChild(Tree('d'))
    r.getChild('b').addChild(Tree('e'))
    r.getChild('b').addChild(Tree('f'))
    print(r)
    assert str(r) == 'a[b[d[]e[]f[]]c[]]'
    print(r.getChild('b'))
    assert str(r.getChild('b')) == 'b[d[]e[]f[]]'
    print(r.getChild('c'))
    assert str(r.getChild('c')) == 'c[]'
    print('Everythings works fine!')