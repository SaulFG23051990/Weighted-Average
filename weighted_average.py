def weighted_average(a,b,w1, w2):
    float(a)
    float(b)
    float(w1)
    float(w2)
    return (a*w1+b*w2)/(w1+w2)
print(weighted_average(80, 90, 1, 1))   # Expected: 85.0
print(weighted_average(70, 95, 2, 3))   # Expected: 85.0
print(weighted_average(100, 50, 4, 1))  # Expected: 90.0