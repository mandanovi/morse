print("MORSE")

morse = {"A" : ".- ", "B" : "-... ", "C":"-.-. ", "D":"-.. ", "E":". ", "F":"..-. ", "G":"--. ", "H": ".... ",
         "I":".. ", "J":".--- ", "K": "-.- ", "L":".-.. ", "M":"-- ", "N":"-. ", "O":"--- ", "P":".--. ",
         "Q":"--.- ", "R":".-. ", "S":"... ", "T":"- ","U":"..- ", "V":"...- ", "W":".-- ", "X":"-..- ", "Y":"-.-- ", "Z":"--.. "}

user_input = input("Translate a Message. Input your code here: ").upper()

morse_code = ""

for key, value in morse.items():
    for letter in user_input:
        if letter == key:
            morse_code += f"{value} "

print(f"Translate to morse: {morse_code}")