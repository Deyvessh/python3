alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

def encrypt(plain_text, shift_amount):
    cipher_text = ""        # defining a empty list
    for letter in plain_text:         # loop through letter in plain_text
        position = alphabet.index(letter)   # get the position(index) of that letter in alphabet 
        new_position = position + shift_amount    # shift the index to the shift_amount to get the new_position
        new_letter = alphabet[new_position]     # new_letter would be new_position in alphabet
        cipher_text += new_letter         # and putting new shift_letter into temp variable(list) we created 
    
    print(f"The encoded text is: {cipher_text}")


    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    # we re-copied the list from a to z again in list(alphabet)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
    
encrypt(plain_text=text, shift_amount=shift)