"""LIVE CODING"""
# PROBLEM 1
def factors(m):
    f = []
    for i in range (1,m+1):
        if m%i==0:
            f.append(i)
def prime(m):
    flag = True
    for i in range(2,m):
        if m%i==0:
            flag = False
            break
        else:
            flag = True
    return flag
def prime_factors(m):
    l = []
    for i in range(1,m+1):
        if prime(i):
            l.append(i)
    return l
    
def prime_product(num):
    flag = False
    temp = prime_factors(num)
    for i in range(len(temp)):
        for j in range(i+1):
            if (i<len(temp)-1) and (temp[i]*temp[j]==num):
               flag = True
               break
            """else:
                flag = False"""
        if flag == True:
            break
    return flag              
    
n = int(input())
print(prime_product(n))


#PROBLEM 2
def del_char(s,c):
    t =''
    if len(c)==1:
        for i in range(len(s)):
            if s[i]!=c:
                t=t+s[i]
        return t
    else:
        return s
            
s = input()
c = input()
print(del_char(s,c))


#PROBLEM 3
def shuffle(l1, l2):
    m = len(l1)
    n = len(l2)
    mini = min(m,n)
    l=[]
    if m==n:
        for i in range(m):
            l.append(l1[i])
            l.append(l2[i])
    else:
        i = 0
        while (i<=m-1 and i<=n-1):
            l.append(l1[i])
            l.append(l2[i])
            i = i + 1
        if mini == m:
            for j in range(i,n):
                l.append(l2[j])
        elif mini == n:
            for j in range(i,m):
                l.append(l1[j])
    return l
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))


#PROBLEM 4
def expanding(l):
    diff = 0
    for i in range(len(l)-1):
        difft = abs(l[i]-l[i+1])
        if difft<=diff:
            return False
        else:
            diff = difft
    return True
L = eval(input())
print(expanding(L))


#PROBLEM 5
def sumsquare(l):
    se = 0
    so = 0
    for x in l:
        if x%2==0:
            se = se + x**2
        else:
            so = so + x**2
    return [so,se]
L = eval(input())
print(sumsquare(L))


#PROBLEM 6
def histogram(l):
    d = {}
    s = []
    for x in l:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    for i in d:
        t = tuple([i,d[i]])
        s.append(t)
        
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i][1] > s[j][1]:
                t = s[i]
                s[i] = s[j]
                s[j] = t
            elif s[i][1] == s[j][1]:
                if s[i]>s[j]:
                    p = s[i]
                    s[i] = s[j]
                    s[j] = p            
    return s
  
L=eval(input())
print(histogram(L))



#PROBLEM 7
def Min_X(n,m):
    if n%3==0 or m%3==0:
        return (n*m)//3
    if n%3==1 and m%3==1:
        maxi = max(n,m)
        mini = min(n,m)
        t = (maxi//3) * mini + (mini//3 + 1)
        return t
    if n%3==2 and m%3==2:
        maxi = max(n,m)
        mini = min(n,m)
        t = (maxi//3) * mini + (mini//3 + 1)*2
        return t 
    if n%3==1 and m%3==2:
        return (m//3 * n + n//3 * 2 + 1)
    if m%3==1 and n%3==2:
        return (n//3 * m + m//3 * 2 + 1)



#PROBLEM 8
