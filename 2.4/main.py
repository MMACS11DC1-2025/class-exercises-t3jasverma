file = open("2.4/responses.csv")

for line in file:
    if "tejas" in line.lower():
        myline= line

    