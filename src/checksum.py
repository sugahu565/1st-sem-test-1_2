def modulo11Checksum(ISBNNumber: str):

    assert len(ISBNNumber) == 10, "Invalid lenght"

    digits = [int(char) for char in ISBNNumber if char.isdigit()]

    assert (len(digits) == 9 and ISBNNumber[-1] == "X") || len(digits) == 10, "letters in number, not nums"

    if (ISBNNumber[-1] == "X"):
        #trash number
        digits += [-1]
        checkDigit = 10
    else:
        checkDigit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight

    checksum = total + checkDigit
    return checksum % 11 == 0

if __name__ == "__main__":
    while True:
        isbn = input("Enter number: ")
        if isbn == -1:
            break
        result = modulo11Checksum(isbn)
        if result:
            print("correct")
        else:
            print("incorrect")
