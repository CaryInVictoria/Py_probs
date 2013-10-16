def future_value(pv, r, n):
    return (pv * (1 + 0.01 * r) ** n)

pv = 100
r = 0.5
n = 12
print('future_value(pv = ' + '%5.2f' % (pv) + ', r = ' + str(r) + ', n = ' + str(n) + ') = ' +  '%5.2f' % (future_value(pv, r, n)))
  # => future_value(pv = 100.00, r = 0.5, n = 12) = 106.17
