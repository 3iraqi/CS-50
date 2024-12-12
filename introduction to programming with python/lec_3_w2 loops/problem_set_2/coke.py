amount_due=50


while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin=int(input("Insert Coin: "))
    
    if coin in [25,10,5]and coin <= amount_due:
        amount_due-=coin
        print(f"Change Owed: {amount_due}")
        
    elif  coin in [25,10,5] and coin > amount_due:
        change_owed=coin-amount_due 
        print(f"Change Owed: {change_owed}")
        break
    


