from math import ceil
from math import log
import argparse


def main():
    args = argparse.ArgumentParser()
    args.add_argument("credit_type", help="type of credit", type=str, action="store_true")
    args.add_argument("credit_payment", help="credit monthly payment", type=float, action="store_true")
    args.add_argument("credit_principal", help="credit principal", type=int, action="store_true")
    args.add_argument("credit_periods", help="periods of credit", type=int, action="store_true")
    args.add_argument("credit_interest", help="credit interest", type=float, action="store_true")
    args.parse_args()

    credit_type: str = args.credit_type
    credit_principal: int = args.credit_principal
    credit_periods: int = args.credit_periods
    credit_interest: float = args.credit_interest
    i: float = (credit_interest / 100) / 12

    if credit_type == "diff":
        pass
    elif credit_type == "annuity":
        credit_annuity_payment: int = ceil(credit_principal * (i * (1 + i) ** credit_periods)
                                           / ((1 + i) ** credit_periods - 1))
        credit_overpayment: int = credit_principal - credit_annuity_payment * credit_periods
        print(f"Your annuity payment = {credit_annuity_payment}!")
        print(f"Overpayment = {credit_overpayment}")
    else:
        print("Incorrect parameters of credit type")

    # print("What do you want to calculate?")
    # print('type "n" - for count of months,')
    # print('type "a" - for annuity monthly payment,')
    # print('type "p" - for monthly payment:')
    # request: str = input("> ")
    #
    # if request == "n":
    #     print("Enter credit principal:")
    #     credit_principal: int = int(input("> "))
    #     print("Enter monthly payment:")
    #     monthly_payment: int = int(input("> "))
    #     print("Enter credit interest:")
    #     credit_interest: float = float(input("> "))
    #     i = (credit_interest / 100) / 12
    #     months_count: int = ceil(log(monthly_payment / (monthly_payment - i * credit_principal), 1 + i))
    #     years_count = months_count // 12
    #     months_count = months_count % 12
    #     if years_count > 0 and months_count > 0:
    #         if years_count == 1 and months_count > 1:
    #             print(f"You need {years_count} year and {months_count} months to repay this credit!")
    #         elif years_count > 1 and months_count == 1:
    #             print(f"You need {years_count} years and {months_count} month to repay this credit!")
    #         else:
    #             print(f"You need {years_count} years and {months_count} months to repay this credit!")
    #     else:
    #         if years_count == 0 and months_count > 0:
    #             if months_count > 1:
    #                 print(f"You need {months_count} months to repay this credit!")
    #             else:
    #                 print(f"You need {months_count} month to repay this credit!")
    #         elif years_count > 0 and months_count == 0:
    #             if years_count > 1:
    #                 print(f"You need {years_count} years to repay this credit!")
    #             else:
    #                 print(f"You need {years_count} year to repay this credit!")
    #         else:
    #             print(f"You was already repaid this credit!")
    # elif request == "a":
    #     print("Enter credit principal:")
    #     credit_principal: int = int(input("> "))
    #     print("Enter count of periods:")
    #     periods_count: int = int(input("> "))
    #     print("Enter credit interest:")
    #     credit_interest: float = float(input("> "))
    #     i = (credit_interest / 100) / 12
    #     annuity_payment: int = ceil(credit_principal * (i * (1 + i) ** periods_count) / ((1 + i) ** periods_count - 1))
    #
    # elif request == "p":
    #     print("Enter monthly payment:")
    #     monthly_payment: float = float(input("> "))
    #     print("Enter count of periods:")
    #     periods_count: int = int(input("> "))
    #     print("Enter credit interest:")
    #     credit_interest: float = float(input("> "))
    #     i = (credit_interest / 100) / 12
    #     credit_principal: int = round(monthly_payment * ((1 + i) ** periods_count - 1) / (i * (1 + i) ** periods_count))
    #     print(f"Your credit principal = {credit_principal}!")
    # else:  # incorrect input
    #     print("Please input correct request.")


if __name__ == '__main__':
    main()
