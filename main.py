PERCENT = percent / 100
if choose == 2:
    for year in range(1, years + 1):
        print(year, "год")
        print("-----------------------------------------------")
        print("|       |   основа   |  сумма %   |           |")
        print("| месяц | инвестиций |  за месяц  |  капитал  |")
        print("-----------------------------------------------")

        for months in range(1, 12 + 1):
            print("|", "{:3.0f}".format(months), "  |", end="")
            print(format(initial_capital, "12.2f"), end="")
            sum_mon = initial_capital * PERCENT
            capital = initial_capital + sum_mon
            initial_capital = initial_capital + sum_mon + \
                              investment_infusion
            print('|', format(sum_mon, "11.2f"), end="")
            print('|', format(initial_capital-investment_infusion,
                              "10.2f"), end="")
            print('|')
    print("-----------------------------------------------")
elif choose == 3:
    for year in range(1, years + 1):
        print(year, "год")
        print("-----------------------------------------------")
        print("|       |   основа   |  сумма %   |           |")
        print("| месяц | инвестиций |  за месяц  |  капитал  |")
        print("-----------------------------------------------")

        for months in range(1, 12 + 1):
            print("|", "{:3.0f}".format(months), "  |", end="")
            print(format(initial_capital, "12.2f"), end="")
            sum_mon = initial_capital * PERCENT
            capital = initial_capital + sum_mon
            initial_capital = initial_capital + sum_mon + \
                              investment_infusion
            print('|', format(sum_mon, "11.2f"), end="")
            print('|', format(initial_capital - investment_infusion,
                              "10.2f"), end="")
            print('|')
    print("-----------------------------------------------")
elif choose == 1:
    for year in range(1, years + 1):
        print(year, lc.PRINT_YEAR)
        print("-----------------------------------------------")
        print("|       |"," ", lc.PRINT_INITIAL_CAPITAL, "",
              "|            |", lc.PRINT_INVESTMENT_INFUSION +
              "|")
        print("|", lc.MONTH, "|", lc.PRINT_INVESTMENT_INFUSION,
              "|  ", lc.PRINT_INCOME, "  | ",
              lc.PRINT_INVESTMENT_INFUSION_1, "|")
        print("-----------------------------------------------")

        for months in range(1, 12 + 1):
            print("|", "{:3.0f}".format(months), "  |", end="")
            print(format(initial_capital, "12.2f"), end="")
            sum_mon = initial_capital * PERCENT
            capital = initial_capital + sum_mon
            initial_capital = initial_capital + sum_mon + \
                              investment_infusion
            print('|', format(sum_mon, "11.2f"), end="")
            print('|', format(initial_capital - investment_infusion,
                              "10.2f"), end="")
            print('|')
    print("-----------------------------------------------")
