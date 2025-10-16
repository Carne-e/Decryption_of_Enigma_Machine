mode = input().strip()
shift = int(input().strip())
rotor1 = input().strip()
rotor2 = input().strip()
rotor3 = input().strip()
message = input().strip()

rotors = [rotor1, rotor2, rotor3]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = []
s = shift

for ch in message:
    if mode == "ENCODE":
        ch = chr((ord(ch) - 65 + s) % 26 + 65)
        for r in rotors:
            ch = r[alphabet.index(ch)]
    else:
        for r in reversed(rotors):
            ch = alphabet[r.index(ch)]
        ch = chr((ord(ch) - 65 - s) % 26 + 65)
    res.append(ch)
    s += 1

print(''.join(res))
