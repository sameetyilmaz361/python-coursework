number=int(input("Enter a number: "))
def reverse_number(n):
    reversed_n = 0
    while n > 0:
        last = n % 10
        reversed_n = (reversed_n * 10) + last
        n = n // 10 
    return reversed_n


print("Reversed number:", reverse_number(number))
