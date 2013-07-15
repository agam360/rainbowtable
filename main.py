'''
RainbowHash Table example,
as described:
http://stichintime.wordpress.com/2009/04/09/rainbow-tables-part-1-introduction/
Code created by: Agam More
'''
import math
import pickle

def hash(p):
    '''The Multiplication Method'''
    s = int(p) * 6.213335
    x = int((s%1.0) * 10e3)
    m = 0.5*(math.sqrt(5)-1)
    ret = int(math.floor(x*m))
    return ret# if len(str(ret)) == 4 else '0'+str(ret)

def reduce1(h):
    '''Reduce function 1'''
    return int(str(h)[-2:])

def reduce2(h):
    '''Reduce function 2'''
    return int(str(h)[:2])

def save(path, data):
    ''' Save data to a .pkl file in specific path '''
    output = open(path, 'w')
    pickle.dump(data, output)
    output.close()
    
def load(path):
    ''' Load .pkl file from path '''
    pkl = open(path, 'r')
    data = pickle.load(pkl)
    pkl.close()
    return data

'''
Test
savedata ="agam, this works"
save("agam.pkl", savedata)
print load("agam.pkl")'''

def createRainbowTable(minn, maxn):
    '''Create rainbow table chains'''
    inc = (maxn-minn)/6 # incremental step
    chains = [[]]*inc
    for i in range(len(chains)):
        a0 = minn
        a1 = hash(a0)
        a2 = reduce1(a1)
        a3 = hash(a2)
        a4 = reduce2(a3)
        
        chains[i] = [a0,a1,a2,a3, a4,hash(a4)]
        minn += 6
    return chains

def createLookupTable(chains):
    '''Create a simple lookup table from chains of rainbow table '''
    return [[i[0],i[-1]] for i in chains]

def findChainByHash(lookup, h):
    '''Find starting chain by last element in chain'''
    for i in lookup:
        if(i[-1] == h):
            return i[0]
    return -1

def findPlainFromChain(chainStart, h):
    h = int(h)
    if(hash(chainStart) == h):
        return chainStart
    a0 = reduce1(hash(chainStart))
    if (hash(a0) == h):
        return a0
    a1 = reduce2(hash(a0))
    if (hash(a1) == h):
        return a1
    return -1

def findPlain(h, lookup):
    '''Reduce h until found in findChainByHash, then go though that chain'''
    h = int(h)
    #Search if in starting chain
    for i in lookup:
        if hash(i[0]) == h:
            return i[0]

    chain = -1
    hTemp = h
    #reduce and search
    for i in lookup:
        a0 = reduce2(hTemp)
        c = findChainByHash(lookup, hash(a0))
        if c != -1:
            chain = c
            break
        a1 = reduce1(hTemp)
        c = findChainByHash(lookup, hash(a1))
        if c != -1:
            chain = c
            break
        #if not found =>
        hTemp = hash(a1)

    if chain != -1:
        return "Found! in chain->" +str(findPlainFromChain(chain,h))
    else:
        return "Not found"
    #if found chain, reduce until hash(a[i])==h
    #else return not found

print createRainbowTable(1,99)
save("rainbowTable.pkl", createLookupTable(createRainbowTable(1,99)))
print findPlain(2636, load("rainbowTable.pkl"))

'''
def findPlainText(h, minn, maxn):
    h = int(h)
    chains = load("rainbowTable.pkl")
    lookup = createLookupTable(chains)
    for i in lookup:
        if hash(i[0]) == h:
            return i[0]
    c = 0
    while (maxn-minn >= c):
        a0 = reduce2(h)
        if hash(a0) == h:
            return a0
        a1 = reduce1(h)
        if hash(a1) == h
            return a1
        for i in lookup:
            if hash(i[0]) == hash(a0) and hash(i[0]) == h:
                return a0
        a1 = reduce1(h)
        for i in lookup:
            if hash(i[0]) == hash(a1) and hash(i[0]) == h:
                return i[0], a1
        c+=1
    return "Number not in lookup talbe"'''





'''
1. Find the hashed value in the lookup table.  If you find it, go to step 2.
  If not:
  1a. Starting with the last reduction function (e.g., R2), "reduce" the
      hashed value to get a new plaintext number. Every time you repeat
      step 1, you go to the next lowest reduction function (e.g., R2,
      then R1).
  1b. Hash the new plaintext number and repeat step 1 from he beginning
      with this new hash value.
2. Take the plaintext value and hash it.
3. Does that hash match the hash we have?
   If so, stop. The value you just hashed is the value you're looking for.
4. If not, apply the reduction function to get a new plaintext value, and
   go back to step 2.
   '''
