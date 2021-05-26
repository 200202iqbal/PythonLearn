print("""Calculator :
            1. Penjumlahan
            2. Pengurangan
            3. Perkalian
            4. Pembagian
            5. Pangkat""")

a = int(input("a :"))
b = int(input("b :"))

def penjumlahan():
    return a+b

def pengurangan():
    return a-b

def perkalian():
    return a*b

def pembagian():
    return a/b

def pangkat():
    return pow(a,b)
