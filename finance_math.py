# A vector of daily market returns (positives and negatives)
market_returns = [0.01, -0.02, -0.07, 0.03, -0.01, -0.06, 0.02]

for r in market_returns:
    if r < -0.05:
        print("Crash detected:")
        print(r)