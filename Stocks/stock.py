def readstockdata(filename):
    tickers = []
    prices = []
    file = open(filename,"r")
    
    for line in file:
        line = line.strip()
        if line =="":
            continue
    
        parts = line.split()
        ticker = parts[0]
        stockprices =[]
    
        for p in parts [1:]:
            stockprices.append(float(p))
        
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
    file = open (filename,"w")
    file.write("stock report\n\n")

    for i in range(len(tickers1)):
        ticker = tickers1[i]
        avg = average(prices1[i])
        avg2 = average(prices2[i])
        
        file.write(ticker + "\n")
        file.write("day 1-20 average: " + str(round(avg, 1)) + "\n")
        file.write("day 21-40 average: " + str(round(avg2, 2)) + "\n")
        
        if avg2 > avg:
            file.write(" Recommendation: buy\n\n")
        else:
            file.write(" Recommendation: Don't buy\n\n")
            
    file.close()
    
    
def main():
    tickers1, prices1 = readstockdata("Day1_20.txt")
    tickers2, prices2 = readstockdata("Day21_40.txt")
    
    generatereport(tickers1, prices1, prices2, "report.txt")
     
    main()
        