# Program name:  Caesar Cipher
# Programmer:  Eric Underwood 
# Date:  March 1, 2025

game_over = False
intro_graphic = '''

            ('-.       ('-.    .-')     ('-.     _  .-')                              _ (`-.  ('-. .-.   ('-.  _  .-')   
            ( OO ).-. _(  OO)  ( OO ).  ( OO ).-.( \( -O )                            ( (OO  )( OO )  / _(  OO)( \( -O )  
   .-----.  / . --. /(,------.(_)---\_) / . --. / ,------.          .-----.  ,-.-')  _.`     \,--. ,--.(,------.,------.  
  '  .--./  | \-.  \  |  .---'/    _ |  | \-.  \  |   /`. '        '  .--./  |  |OO)(__...--''|  | |  | |  .---'|   /`. ' 
  |  |('-..-'-'  |  | |  |    \  :` `..-'-'  |  | |  /  | |        |  |('-.  |  |  \ |  /  | ||   .|  | |  |    |  /  | | 
 /_) |OO  )\| |_.'  |(|  '--.  '..`''.)\| |_.'  | |  |_.' |       /_) |OO  ) |  |(_/ |  |_.' ||       |(|  '--. |  |_.' | 
 ||  |`-'|  |  .-.  | |  .--' .-._)   \ |  .-.  | |  .  '.'       ||  |`-'| ,|  |_.' |  .___.'|  .-.  | |  .--' |  .  '.' 
(_'  '--'\  |  | |  | |  `---.\       / |  | |  | |  |\  \       (_'  '--'\(_|  |    |  |     |  | |  | |  `---.|  |\  \  
   `-----'  `--' `--' `------' `-----'  `--' `--' `--' '--'         `-----'  `--'    `--'     `--' `--' `------'`--' '--' '''


def caesar(message, direction, shift):
    if direction == 'decode':
        shift *= -1  
    result = ""
    for letter in message.lower():
        if not letter.isalpha():
            result += letter
        else:
            index = alphabet.index(letter) + shift
            index %= len(alphabet)
            result += alphabet[index]
    print(f"Here's the {direction}d result:  {result}") 

print(intro_graphic) 

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

while not game_over:
    type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 
    message = input("Type your message:\n")
    shift = int(input("Type your shift number: \n"))  

    caesar(message, type, shift)

    if input("Type 'yes' if you want to go again.  Otherwise type 'no'.\n").lower() == "no":
        game_over = True
