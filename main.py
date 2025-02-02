from math_functions import sumF, diffF, sq, sq_eq, avg, mediana, moda


if __name__ == "__main__":
    numbers = [1,7,10,10,5,-3,11,11,5]
    a = 5
    b = 4

    s = sumF(a, b)
    print("Sum: ", s)

    d = diffF(a, b)
    print("Diff: ", d)

    r = sq(b)
    print("Square: ", r)

    res = sq_eq(a=1, b=2, c=-3)
    print("Square equation", res)

    r = avg(numbers)
    print("Average: ", r)

    Me = mediana(numbers)
    print("Median: ", Me)

    print("Mode: ",moda(numbers))
