if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

l = []
for i in range(x+1):
    for j in range (y+1):
        for k in range(z+1):
            sum = 0
            sum = (i+j+k)
            if(sum!=n):
                l.append([i,j,k])
            else:
                pass
print(l)

