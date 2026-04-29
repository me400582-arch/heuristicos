from heuristicos_pkg.knapsack import mochila

def knapsack_solver(instance, idx=0, current=None, best=None):
    if current is None:
        current = []
    if best is None:
        # Initialize best with [profit, weight, selection]
        best = [0, 0, []]

    # Base Case: All items have been considered
    if idx == len(instance.weights):
        total_weight = sum(w * s for w, s in zip(instance.weights, current))
        total_profit = sum(p * s for p, s in zip(instance.profits, current))
        
        # Check if valid AND better than the current best
        if total_weight <= instance.capacity and total_profit > best[0]:
            best[0], best[1], best[2] = total_profit, total_weight, current[:]
            yield tuple(best) # Yield the new champion
    else:
        for choice in [1, 0]:
            current.append(choice)
            # Pass the same 'best' list down the recursion
            yield from knapsack_solver(instance, idx + 1, current, best)
            current.pop()

