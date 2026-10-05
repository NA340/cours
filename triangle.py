def triangle(n):
    for i in range(n - 1):
        espace_haut = " " * (n - i - 1)
        espace_milieu = " " * (2 * i)
        print(espace_haut + "/" + espace_milieu + "\\")
    if n > 0:
        print("/" + "_" * (2 * n - 2) + "\\")

triangle(55)
