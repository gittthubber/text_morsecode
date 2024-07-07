MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' / '  # Lo spazio tra le parole è rappresentato da uno slash
}


def text_to_code():
    morse_code = ""

    text = input("Inserisci il testo da convertire in codice Morse: ")
    for n in text.upper():
        if n in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[n]+MORSE_CODE_DICT[' ']
    print(f"Codice Morse: {morse_code}")

if __name__ == "__main__":
    text_to_code()