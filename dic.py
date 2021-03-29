class DIC:
    def __init__(self, dddd, fun, var):
        self.fun = fun
        self.typ = ['_','obj','fun']

        self.key = list(map(lambda x: x[0], filter(lambda x: x[0][0] != 'fun', dddd.items())))


        self.f = {}
        self.d = {}
        self.var = var 

        for key in dddd:
            if key[0] != 'fun': self.d[key] = dddd[key]
            else: self.f[key] = dddd[key]
        #self.d = dict(zip(self.typ, dddd))
        self.isvalid =  dict(zip(self.typ,map(lambda x: len(x) != 0,dddd)))

        if self.isvalid['_']: self.nth = self.d[('_', '_')]



    def value(self, token):
        typ, val = token
        if typ in self.typ:
            if typ == '_': return self.nth
            if typ == 'fun': return self.tofun(token)
            if token in self.d.keys():
                return self.d[token]
            else: return token
            if not self.isvalid(typ):
                raise Exception ('Cannot Recieve type ', typ, 'as input')
        else: raise Exception ('Cannot Recieve type ', typ, 'as input')

    def update(self, exp, src,tar):
        rest = []
        for e in exp:
            if type(e) == list:
                rest.append(self.update(e,src,tar))
            elif type(e) == tuple:
                if e == src: rest.append(tar)
                else: rest.append(e)
        return rest
    def tofun(self, token):
        print('UPDATE: expression from',self.var,'->',token)
        return self.update(self.f[self.var], self.var, token)

    def __str__(self): return str(self.d)

    ''''
    def fakeout(self,inp):
        typ, val = inp
        if val == '_': return self.nth['_']
        if typ == 'obj':
            if val in self.obj.keys(): return self.obj['inp']
            elif len(self.fun) == 0: return inp
        els: self.fun[inp]

    def realout(self, out): pass

    def totyp(self,typ): 
        sth = self.d 
        self.d = dict(filter(lambda e:e[0][0] == typ,self.d.items()))
        return list(filter(lambda e:e[0][0] == typ,sth.items()))
    def getval(self,sth): return dict(map(lambda x: (x[0][1], x[1][1]), sth))'''