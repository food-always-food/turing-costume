import tqdm, re, requests
from time import sleep

rotors = [
    "I II III",
    "I II IV",
    "I II V",
    "I III II",
    "I III IV",
    "I III V",
    "I IV II",
    "I IV III",
    "I IV V",
    "I V II",
    "I V III",
    "I V IV",
    "II I III",
    "II I IV",
    "II I V",
    "II III I",
    "II III IV",
    "II III V",
    "II IV I",
    "II IV III",
    "II IV V",
    "II V I",
    "II V III",
    "II V IV",
    "III I II",
    "III I IV",
    "III I V",
    "III II I",
    "III II IV",
    "III II V",
    "III IV I",
    "III IV II",
    "III IV V",
    "IV I II",
    "IV I III",
    "IV I V",
    "IV II I",
    "IV II III",
    "IV I V",
    "IV II I",
    "IV II III",
    "IV II V",
    "IV III I",
    "IV III II",
    "IV III V",
    "IV V I",
    "IV V II",
    "IV V III",
    "V I II",
    "V I III",
    "V I IV",
    "V II I",
    "V II III",
    "V II IV",
    "V III I",
    "V III II",
    "V III IV",
    "V IV I",
    "V IV II",
    "V IV III",
]


def find_roto_start(rotor_choice, ciphertext, cribtext):
    from enigma.machine import EnigmaMachine

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    machine = EnigmaMachine.from_key_sheet(
        rotors=rotor_choice,
        reflector="B",
        ring_settings="1 1 1",
        plugboard_settings="AV BS CG DL FU HZ IN KM OW RX",
    )
    for rotor1 in alphabet:
        for rotor2 in alphabet:
            for rotor3 in alphabet:
                start_pos = rotor1 + rotor2 + rotor3
                machine.set_display(start_pos)
                plaintext = machine.process_text(ciphertext)
                if cribtext in plaintext:
                    print("Valid settings found!")
                    print(plaintext)
                    return rotor_choice, start_pos, plaintext
                    break
    return rotor_choice, False


def process_text(text):
    regex = re.compile("[^a-zA-Z]")
    punc_free = regex.sub("", text)
    space_free = punc_free.replace(" ", "")
    # print(space_free.upper())
    return space_free.upper()


def solveText(ciphertext):
    for x in tqdm.tqdm(rotors):
        cribtext = "Sept Fourth"
        test = find_roto_start(x, process_text(ciphertext), process_text(cribtext))
        if test[1] != False:
            print(test[2])
            return(test[2])
