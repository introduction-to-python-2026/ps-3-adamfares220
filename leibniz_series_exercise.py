def approximate_pi(n_terms):
   
    pi_estimate = 0.0
    sign = 1.0
    for n in range(n_terms):
        denominator = 2 * n + 1
        pi_estimate += sign / denominator
        sign = -sign
    return 4 * pi_estimate
