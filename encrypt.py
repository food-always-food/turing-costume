from enigma.machine import EnigmaMachine
import re

machine = EnigmaMachine.from_key_sheet(
    rotors='I II III',
    reflector="B",
    ring_settings='1 1 1',
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
)

def process_text(text):
    regex = re.compile('[^a-zA-Z]')
    punc_free = regex.sub('', text)
    space_free = punc_free.replace(" ", "")
    return(space_free.upper())

machine.set_display("UYT")

msg_key = machine.process_text('PWE')
print(msg_key)

plaintext = "Test the Notes Poot poot boot WHTBEDFU"
# plaintext = 'THISXISXWORKING'
ciphertext = machine.process_text(process_text(plaintext))
print(ciphertext)