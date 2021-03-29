from dic import DIC
class FUN:
    def __init__(self,name, var = [], dic = {}):
        self.math = {
          'ADD':lambda x,y: x+y,
          'MUL':lambda x,y: x*y,
          'DIV':lambda x,y: x/y,
          'MOD':lambda x,y: x%y,
          'AND':lambda x,y: x and y,
          'OR' :lambda x,y: x or y,
        }
        self.name = name
        self.var = var

        self.d = dic
        self.dic = {}
        for v in var:
            self.dic[v] = DIC(dic[self.name][v],self,v)
        self.n_arg = len(var)

    def inp(self,inp):
        print(self.name)
        if self.name in self.math: 
            print('is math func')
            return self.mathf(self.name,inp)
        idx = 0
        result = {}
        for var in self.dic:
            currinp = inp[idx]
            if idx == len(inp): break
            if currinp[0] == 'fun': 
                if currinp in self.d.keys():
                    
                    if len(self.d[currinp]) == 1:
                        currinp = self.d[currinp][('_','_')]
                    
                else:
                    currinp = '_'

            if currinp in self.dic[var].key:
                result[var] = self.dic[var].value(currinp)
            else:
                result[var] = self.dic[var].tofun(currinp)

            idx += 1
        return result[self.var[-1]]
    def mathf(self,name,inp):
        it = iter(inp)
        curr = next(it)
        
        result = 0 + 1* (name == 'MUL')
        while curr != None:
            result = self.math[name](result,int(curr[1]))
            try:
                curr = next(it)
            except StopIteration:
                return ('obj',str(result))

