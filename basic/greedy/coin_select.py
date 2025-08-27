def greedy_change_verbose(amount, coins):
    answer = []
    
    if len(coins)<=0:
        return answer

    sorted_coin = sorted(coins, reverse = True)

    answer = sorted_coin[0]
    i=0
    total = sorted_coin[0]

    print(answer, i, total)

    while total <= amount:
        total = sorted_coin[i] + total
        if total > amount:
            total = total - sorted_coin[i] 
            i=i+1
        elif total < amount:
            total = sorted_coin[i] + total
            answer.append(sorted_coin[i])
        else:
            break




    return answer

coins_AU = [200, 20, 10, 5, 3]
greedy_result = greedy_change_verbose(289, coins_AU)
print("Greedy result:", greedy_result, "\n")