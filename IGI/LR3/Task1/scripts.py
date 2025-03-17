def calculate_exp(x, eps):
    """
    Calculate exp.

    Args: x (float), eps (float) : x and eps
    Returns: n (int), result (float): Count of iterations, Result of func.
    """
    sum_series = 0.0
    n = 0
    term = 1.0

    while n < 500:
        sum_series += term
        if abs(term) < eps:
            break
        n += 1
        term = term * x / n

    return n, sum_series



