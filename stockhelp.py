def readstockdata(filename):
    tickers = []
    prices = []
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return [], []
    else:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split()
            ticker = parts[0]
            stockprices = []

            for p in parts[1:]:
                try:
                    stockprices.append(float(p))
                except ValueError:
                    print(f"Error: Non-numeric data in {filename} for {ticker}")
            
            tickers.append(ticker)
            prices.append(stockprices)
        file.close()
        return tickers, prices


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def generatereport(tickers1, prices1, prices2, filename):
    try:
        file = open(filename, "w")
    except Exception as e:
        print(f"Error opening {filename} for writing: {e}")
        return
    else:
        file.write("Stock Report\n\n")

        for i in range(len(tickers1)):
            ticker = tickers1[i]
            avg1 = average(prices1[i])
            avg2 = average(prices2[i])

            file.write(ticker + "\n")
            file.write("day 1-20 average: " + str(round(avg1, 2)) + "\n")
            file.write("day 21-40 average: " + str(round(avg2, 2)) + "\n")

            if avg2 > avg1:
                file.write(" Recommendation: BUY\n\n")
            else:
                file.write(" Recommendation: DON'T BUY\n\n")

        file.close()
        print(f"Report successfully written to {filename}")


def main():
    tickers1, prices1 = readstockdata("Day1_20.txt")
    tickers2, prices2 = readstockdata("Day21_40.txt")

    if tickers1 and tickers2:
        generatereport(tickers1, prices1, prices2, "report.txt")


