try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))

    if hours <= 40:
      total_pay = hours * rate
    else:
       
        normal_pay = 40 * rate
        extrahours = hours - 40
        extra_pay = extrahours * (rate * 1.5)
        total_pay = normal_pay + extra_pay

    print("Pay:", total_pay)

except ValueError:
    print("Error, please enter numeric input")