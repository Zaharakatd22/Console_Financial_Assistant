from math import ceil


def main():
    print("Enter the credit principal:")
    credit_principal: int = int(input("> "))

    print("What do you want to calculate?")
    print('type "m" - for count of months,')
    print('type "p" - for monthly payment:')
    request: str = input("> ")

    if request == "m":
        print("Enter monthly payment:")
        monthly_payment: int = int(input("> "))
        months_count: int = ceil(credit_principal / monthly_payment)
        print()  # decorate separating empty line
        print(f"It takes {months_count} month to repay the credit" if months_count < 2
              else f"It takes {months_count} months to repay the credit")
    elif request == "p":
        print("Enter count of months:")
        months_count: int = int(input("> "))
        monthly_payment: int = ceil(credit_principal / months_count)
        last_month_payment: int = credit_principal - (months_count - 1) * monthly_payment
        print()
        print(f"Your monthly payment = {monthly_payment}" if last_month_payment == monthly_payment
              else f"Your monthly payment = {monthly_payment} with last month payment = {last_month_payment}.")
    else:
        print("Please input correct request.")


if __name__ == '__main__':
    main()
