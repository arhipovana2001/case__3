import local
choose = int(input(local.CHOOSE))
if choose == 1:
    import local_english as lc
elif choose == 2:
    import local_russian as lc
elif choose == 3:
    import local_germany as lc
years = int(input(lc.YEARS))
while years <= 0:
    print(lc.ERROR_1, end='')
    years = int(input())

initial_capital = float(input(lc.INITIAL_CAPITAL))
while initial_capital <= 0:
    print(lc.ERROR_2, end='')
    initial_capital = int(input())

percent = float(input(lc.PERCENT))
while percent <= 0:
    print(lc.ERROR_3, end='')
    percent = int(input())

investment_infusion = float(input(lc.INVESTMENT_INFUSION))
while investment_infusion < 0:
    print(lc.ERROR_4, end='')
    investment_infusion = int(input())

PERCENT = percent / 100

if choose == 3:
    for year in range(1, years + 1):
        print(year, lc.PRINT_YEAR)
        print("----------------------------------------------")
        print("|      |","",lc.PRINT_INITIAL_CAPITAL +
              "|            |" + lc.PRINT_INVESTMENT_INFUSION
              + "|")
        print("|", lc.MONTH + "|", lc.PRINT_INVESTMENT_INFUSION
              + "|  ", lc.PRINT_INCOME, " | ",
              lc.PRINT_INVESTMENT_INFUSION_1, "|")
        print("----------------------------------------------")
