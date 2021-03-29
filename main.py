from dic import DIC
from fun import FUN

alld = {}


alld[('fun', 'y')] = {
  ('_', '_'):('obj', 'x')
}

alld[('fun', 'A')] = {}
alld[('fun', 'A')][('fun', 'y')] = {
  ('_', '_'):('obj', 'Hello world'), 
  ('obj', 'x'):('obj', 'y'),
  ('fun', 'y'):[('fun','ADD'),
  [
        [('fun', 'MUL'),
            [
            ('fun','y'),
            ('obj','2')
            ]
        ],('obj','1')]
  ]
}
#seperate fun as input and other
#for fun, recursion until output = obj or __doc_ 
#then we will feed it into the dictionary
allfun ={
  'A': FUN(('fun', 'A'),[('fun', 'y')],alld),
  'y':FUN(('fun','y'),[],alld),
  'ADD': FUN('ADD'),
  'MUL': FUN('MUL'),
  'MOD': FUN('MOD')
}


def exp(name, arg):

    if name[1] in allfun.keys():
        print(expand(arg))
        result = allfun[name[1]].inp(arg)

        if(type(result) == tuple): return result
        elif(type(result) == list):

            return exp(result[0],result[1])
    return arg

def expand(arg):
    def isvalid(a): return sum(map(lambda x: type(x) == tuple,a)) == len(a)
    result = []
    print('arg',arg)
    if len(arg) == 2: 
        print('arg 1',arg[1], isvalid(arg[1]))
    
        if not (arg[0][0] == 'fun' and isvalid(arg[1])):
            for e in arg:
                if type(e) == list:
                    if not isvalid(e[1]):
                        result.append(expand(e))
                    else:
                        result.append(allfun[e[0]].inp(e[1]))
                elif type(e) == tuple:
                    result.append(e)
    else: return 
    return result
    print('')

#print(exp('A',[('_', '_')]))
#print(exp('A',[('obj', 'x')]))
#print(exp('A',[('fun', 'y')]))
print(exp(('fun','A'),[('obj','1')]))