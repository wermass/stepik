for i in range(1, 40):
    for j in range(1, 40):
        for k in range(1, 40):
            for l in range(1, 40):
                if i != k and i != l and j != k and j != l and i ** 3 + j ** 3 == k ** 3 + l ** 3:
                    print(i ** 3 + j ** 3)