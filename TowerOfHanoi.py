def TowerOfHanoi(n, a, b, c):
    if n == 1:
        print("pindahkan piring 1 dari",a,"ke",b)
        return
    TowerOfHanoi(n-1, a, c, b)
    print("pindahkan piring",n,"dari",a,"ke",b)
    TowerOfHanoi(n-1, c, b, a)
          
n = 2
TowerOfHanoi(n,'A','B','C') 