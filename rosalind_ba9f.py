#rosalind_ba9f

f = open('rosalind_ba9f.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()

k = 2
x = ''
while x == '':
    for i in range(len(s)-k+1):
        if s[i:i+k] not in t:
            x = s[i:i+k]
            break    
    k += 1

print(x)