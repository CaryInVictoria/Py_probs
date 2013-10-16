def is_a_vowel(c):
    return c.lower() in "aeiou"

or
def is_a_vowel(c):
    return "aeiou".find(c.lower()) != -1

or
def is_a_vowel(c):
    import re # Can be before def
    regexp = re.compile(".*[aeiou].*")
    if regexp.search(c.lower()):
        return True
    else:
        return False

def report_if_vowel(c):
    if is_a_vowel(c):
        print('Yup, \'' + c + '\' is a vowel')
    else:
        print('Nope, \'' + c + '\' ain\'t no vowel')

report_if_vowel('i') # => Yup, 'i' is a vowel
report_if_vowel('E') # => Yup, 'E' is a vowel
report_if_vowel('s') # => Nope, 's' ain't no vowel
report_if_vowel('J') # => Nope, 'J' ain't no vowel
report_if_vowel('%') # => Nope, '%' ain't no vowel
