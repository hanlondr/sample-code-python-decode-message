def decode(message_file):
    with open(message_file, 'r') as file:
        text = (file.read()).split()

    # Make an empty list called pyramid, iterate through the list text, assign each word to pyramid at the correct index.
    pyramid = [""] * (len(text) // 2)
    for i in range(0, len(text), 2):
        index = int(text[i]) - 1
        word = text[i + 1]
        pyramid[index] = word

    # Iterate through the "rows" of the pyramid, add the word at the end of each row to an output string.
    decoded_message, cursor, increment = "", 0, 1
    while cursor < len(pyramid):
        decoded_message += f'{pyramid[cursor]} '
        increment += 1
        cursor += increment

    return decoded_message

message_file = "encoded_message.txt"
decoded_message = decode(message_file)
print(decoded_message)