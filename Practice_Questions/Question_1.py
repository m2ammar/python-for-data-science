#You have a list of transaction amounts: [120, -45, 300, -10, 75, -200, 50] 
#(positive = deposit, negative = withdrawal). Write a function summarize(transactions)
#that returns a dictionary with three keys: total_deposits, total_withdrawals, and net_balance.


def summarize(transaction):
    
    total_deposits = 0
    total_withdrawals = 0
    for amount in transaction:
        if amount < 0:
            total_withdrawals += abs(amount)
        else:
            total_deposits += amount
        
        
    net_balance = total_deposits - total_withdrawals        
    return {
    'total_withdrawals' : total_withdrawals,
    'total_deposits' : total_deposits,
    'net_balance' : net_balance
    }      
    
transaction_amounts = [120, -45, 300, -10, 75, -200, 50]     
    
result = summarize(transaction_amounts)
print(result)

      








