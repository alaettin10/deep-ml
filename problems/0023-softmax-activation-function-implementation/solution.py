import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    M = max(scores)
    exp_scores = [math.exp(x-M)for x in scores]
    total = sum(exp_scores)
    return [val / total for val in exp_scores ]

    pass