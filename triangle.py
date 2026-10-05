#def triangle(n):
#    for i in range(n - 1):
 #       espace_haut = " " * (n - i - 1)
#        espace_milieu = " " * (2 * i)
#        print(espace_haut + "/" + espace_milieu + "\\")
#    if n > 0:
#        print("/" + "_" * (2 * n - 2) + "\\")

#triangle(55)

def maguendvd(n):
    for i in range(n):
        print(" " * (n - i - 1) + "/" + " " * (2 * i) + "\\")
    print("/" + "_" * (2 * n - 2) + "\\")
    print("\\" + "_" * (2 * n - 2) + "/")
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + "\\" + " " * (2 * i) + "/")

maguendvd(5)

