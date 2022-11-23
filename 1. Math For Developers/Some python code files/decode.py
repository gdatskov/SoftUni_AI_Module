from collections import deque


def decode(text):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    entry = deque(text)
    decoded = []

    while entry:
        symbol = entry.popleft()

        if entry[0].isdigit():
            number = int(entry.popleft())
        else:
            number = 1

        decoded.extend(symbol*number)

    return "".join(decoded)




print(decode(input()))
