def max_hamsters(S, C, hamsters):
    low = 0
    high = C
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        costs = []
        for h in hamsters:
            # h[0] - норма, h[1] - жадібність
            cost = h[0] + h[1] * (mid - 1)
            costs.append(cost)
        
        # 2. RADIX SORT
        if costs:
            max_val = max(costs)
            exp = 1
            # Поки не пройдемо всі розряди найбільшого числа
            while max_val // exp > 0:
                # Створюємо 10 кошиків (для цифр 0-9)
                buckets = [[] for _ in range(10)]
                for c in costs:
                    digit = (c // exp) % 10
                    buckets[digit].append(c)
                
                # Збираємо елементи назад у список costs
                costs = []
                for bucket in buckets:
                    costs.extend(bucket)
                
                exp *= 10
      
        total_cost = sum(costs[:mid])
        
        if total_cost <= S:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result
