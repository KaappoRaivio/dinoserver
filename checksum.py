luhnify = lambda digit: sum(divmod( digit*2, 10 ))

def checksum(digits):
    """Return the Luhn checksum of a sequence of digits.
    """
    digits = list(map( int, digits ))
    odds, evens = digits[-2::-2], digits[-1::-2]
    return sum( list(map(luhnify,odds)) + evens ) % 10


test = list("123")


test.append(str(checksum(test)))

print(str(checksum(test)), test)

def verify(number_sequence):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(number_sequence)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(number_sequence[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return sum % 10 == 0

print(verify(test))
