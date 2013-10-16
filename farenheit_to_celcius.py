def farenheit_to_celsius(f):
    return ((f-32)*5/9)

f = 70
print(str(f) + 'F -> ' + '%2.1f' % (farenheit_to_celsius(f)) + 'C') # => 70F -> 21.1C
