def CF(a,b):
       if b<=2:
              return [0,a,a*a][b]
       else:
              result=CF(a,b//2)*CF(a,b//2)
              return [result,result*a][b%2]

print(CF(2,1))
