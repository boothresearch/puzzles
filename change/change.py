def find_fewest_coins(coins, target):

    #Define change left
    changeLeft = target

    output = []
    
    while changeLeft>0:
        #Number of coins required for that ammount
        neededCoins=[i for i in coins if changeLeft>=i]

        #Only if number of coins is positive
        biggestCoin = max(neededCoins)

        #How much of the biggest coin we require
        countBiggestCoin = changeLeft//biggestCoin

        #Output
        output += [biggestCoin]*countBiggestCoin
        
        #Substract change
        changeLeft -= biggestCoin*countBiggestCoin

    return(sorted(output))