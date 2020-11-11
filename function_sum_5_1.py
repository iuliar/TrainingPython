"""Write a function which computes the sum of n numbers.
n is sent as a parameter via the command line."""


def suma_of_n_nr(n):
    suma = 0
    for num in range(1, n+1, 1):
        suma = suma + num
    return suma


n = int(input("Write how many numbers should be added: "))
print("The sum is: ", suma_of_n_nr(n))


