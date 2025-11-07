def modulo11Checksum(ISBNNumber: str):

    assert len(ISBNNumber) == 10, "Invalid lenght"

    digits = [int(char) for char in ISBNNumber if char.isdigit()]

    checkDigit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight

    checksum = total + checkDigit
    return checksum % 11 == 0
