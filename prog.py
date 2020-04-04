def get_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i

    return fact

test = int(input())
for i in range(test):
    inpu = input().split()
    n = int(inpu[0])
    k = int(inpu[1])

    factn= get_fact(n)
    pow2 = 2**k
    a = n%k
    b = k-a
    numa = int(n/k)
    numb = numa

    if(a>0):
        numa=numa+1

    facta = get_fact(a)
    factb = get_fact(b)

    pow2 = 1
    if(numa>2):
        pow2 = 2**a

    if(numb>2):
        pow2 = pow2 * (2**b)
    

    powa = numa**a
    powb = numb**b
    #print(factn, facta, factb, powa, powb)
    ans = int(factn/(facta*factb*powa*powb*pow2))

    print("Case #"+str(i+1)+": "+str(ans))



