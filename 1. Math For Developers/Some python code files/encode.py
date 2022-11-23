from collections import deque


def encode(text):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    entry = deque(text)
    encoded = []
    current_count = []

    while entry:
        current_symbol = entry.popleft()
        if current_symbol.isdigit():
            return "Digit in encode text string. Aborted."
        if len(current_count) == 0:
            current_count.append(current_symbol)
        else:
            if current_count[0] == current_symbol:
                current_count.append(current_symbol)
        if current_count[0] != current_symbol or not entry:
            encoded.append(current_count[0])
            if len(current_count) > 1:
                encoded.append(str(len(current_count)))
            current_count = [current_symbol]

    return "".join(encoded)


print(encode(input()))
