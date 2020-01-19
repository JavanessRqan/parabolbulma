def parabol(a,b,c):
    delta = b*b -4*a*c
    if delta >= 1:
        print("Parabol denklemi 2 farkli noktada keser.")

        x1 = (-b - delta**0.5)/(2*a)
        x2 = (-b + delta**0.5)/(2*a)
        return (x1,x2)
    elif delta == 0:
        print("Parabol dogruya teget gecer.")
    else:
        print("Parabol kesismez.")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

sonuc = parabol(a,b,c)
print(sonuc)