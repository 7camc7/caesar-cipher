import art 
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(variable_text, variable_shift, variable_direction):
  end_text = ''
  if variable_direction == "decode":
      variable_shift *= -1
  for char in variable_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + variable_shift
        end_text += alphabet[new_position] 
    else:
        end_text += char

  print(f"The {variable_direction}d text is '{end_text}'")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(variable_text= text, variable_shift= shift, variable_direction= direction)

    restart = input("Do you want to restart the cipher: yes or no? ")
    if restart == "no":
        should_continue = False
        print("Bye!")
