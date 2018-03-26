import re
import sys
pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'

opstack = []

dictstack = []


def opPop():
    if len(opstack) == 0:
        print("Error mate nothign in da stackahz")
    else:
        return opstack.pop() #return theend of the list

def opPush(value):
    if isinstance(value, str) and not isinstance(value, list):
        if len(dictStack) > 0 and value in dictStack[-1]: #check if it is a variable and look it up
            item = lookup(value)
                opstack.append(item)
        else:
            opstack.append(value)
    else:
        opstack.append(value)

def dictPop():
    if len(dictstack) == 0:
        print("Error nothing in the dict")
    else:
        return dictstack.pop()

def dictPush(d):
     dictstack.append(d) # check if dictionary already exists

def define(name,value):
    if len(dictStack) > 0:
        dictstack[-1][name] = value
    else:
        dictstack.append({name:value})

def lookup(name):
    if (name in dictstack[-1]): #check if the current dictionary
        return dictstack[-1][name]
    else:
        print("not in dict")


def popNum():
    x = opPop()
    if isNumber(x) == False:
        print("Error mate not a numba or doesnt exist")
    return x;

def pop2():
    if len(opstack) >1:
        return (popNum(),popNum());
    else:
        print ("Not enough items")


# add, sub, mul, div ,mod

def add():
    n1,n2 = pop2()
    if isinstance(n1, str):
        n1 = lookup(n1)
    if isinstance(n2, str):
        n2 = lookup(n2)
    pAns = n1+n2
    opPush(pAns)

def sub():
    n1,n2 = pop2()
    if isinstance(n1, str):
        n1 = lookup(n1)
    if isinstance(n2, str):
        n2 = lookup(n2)
    pAns = n1-n2
    opPush(pAns)

def mul():
    n1,n2 = pop2()
    if isinstance(n1, str):
        n1 = lookup(n1)
    if isinstance(n2, str):
        n2 = lookup(n2)
    pAns = n1*n2
    opPush(pAns)

def div():
    n1,n2 = pop2()
    if isinstance(n1, str):
        n1 = lookup(n1)
    if isinstance(n2, str):
        n2 = lookup(n2)
    pAns = n1/n2
    opPush(pAns)

def mod():
  n1,n2 = pop2()
  if isinstance(n1, str):
      n1 = lookup(n1)
  if isinstance(n2, str):
      n2 = lookup(n2)
  pAns = n1%n2
  opPush(pAns)

# length, get

def length ():
     opPush(len(opPop()))

def get():
    ind = opPop()
    ry = opPop()
    if isinstance(array, list) and ind < len(ry):
        opPush(ry[ind])
    else:
        print("error")


# dup, exch, pop, roll, copy, clear, stack

def dup():
    if len(opstack) > 0:
        opstack.append(opstack[-1])

def exch():
    if len(opstack) > 1:
        top = opPop()
        top2 = opPop()
        opPush(top)
        opPush(top2)

def pop():
    opPop()

def roll():
    amt = opPop() #amount
    indices = opPop() # roll indices
    if amt <= len(opstack):
        temp = opstack[len(opstack)-indices:] # simple sublist
        for x in range(indices):
            opPop()
        if amt <0: # other way
            for y in range(indices):
                temp2 = temp[0] # get the front
                temp.append(temp2) #add to back
                temp.remove(temp2) #remove from front remove only does on the first instance
        else: #normal roll
            for z in range(indices):
                t = temp.pop()
                temp.insert(0,temp) #put in front
        for xyz in range(len(temp))
            opPush(temp[xyz])



def copy():
    top = opPop()
    if len(opStack) >= toCopy:
        for i in range(top):
            opPush(top)

def clear():
    opstack.clear()
    dictstack.clear()

def stack():
  print(opstack)

#psDict, begin, end, psDef

def psDict():
    opPop()
    opPush({})

def begin():
    dct = opPop()
    if isinstance(dct, dict):
        dictStack.append(dct)


def end():
        if len(dictStack) > 0:
        dictPop()

def psDef():
    val = opPop()
    d = opPop()
    d = d[1:] #remove the / part of the name
    dictPush(define(d,val))


#------- Part 1 TEST CASES--------------
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testMod():
    opPush(10)
    opPush(3)
    mod()
    if opPop() != 1:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True


def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv),  ('mod', testMod), \
                ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll), ('copy', testCopy), \
                ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')



main_part1()
