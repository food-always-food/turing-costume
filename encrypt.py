from enigma.machine import EnigmaMachine
import re

def clean_text(text):
    regex = re.compile('[^a-zA-Z]')
    punc_free = regex.sub('', text)
    space_free = punc_free.replace(" ", "")
    return(space_free.upper())

def encryptMessage(text, rotorPositions):
    machine = EnigmaMachine.from_key_sheet(
    rotors=rotorPositions,
    reflector="B",
    ring_settings='1 1 1',
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
    )
    machine.set_display("UYT")
    msg_key = machine.process_text('PWR')
    ciphertext = machine.process_text(clean_text(text))
    return ciphertext



# text = encryptMessage("September Fourth, twenty twenty-one Welcome to the party, this is my design. I love you!","I II III")

# print(text)