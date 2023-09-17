# TODO 1: Task
"""Caeser Cipher Encryption & Decription"""

# TODO 2: Art Zone
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# TODO 3: Lists
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# TODO 4: Functions for Encryption & Decryption
def Encrypt(List, Data, Shift_number):
    # Bringing shift number within range
    if Shift_number > 26:
        while not Shift_number <= 26:
            New_Shift_index = Shift_number - 26
            Shift_number = New_Shift_index

    # Encrypting data
    Encrypted_Data = ""
    for n in Data:
        if n in List:
            New_Index = (List.index(n)) + Shift_number
            Encrypted_Data += alphabet[New_Index]
        else:
            Encrypted_Data += n
    return Encrypted_Data

def Decrypt(List, Data, Shift_number):
    # Bringing shift number within range
    if Shift_number > 26:
        while not Shift_number <= 26:
            New_Shift_index = Shift_number - 26
            Shift_number = New_Shift_index

    # Decrypting data
    Decrypted_Data = ""
    for n in Data:
        if n in List:
            New_Index = (List.index(n)) - Shift_number
            Decrypted_Data += alphabet[New_Index]
        else:
            Decrypted_Data += n
    return Decrypted_Data

# TODO 5: Welcome Code
print(logo)
print("**************** We make your data safe ********************\n")

# TODO 6: Logic
On = True
while On:
    E_or_D = input("Encode or Decode (Type E or D) : ").lower()
    Data_by_user = input("Enter the Data : ").lower()
    Shift = int(input("Enter the shift : "))

    if E_or_D == "e" or E_or_D == "encode":
        print(f"Encrypted data is : '{Encrypt(alphabet, Data_by_user, Shift)}'")
    elif E_or_D == "d" or E_or_D == "decode":
        print(f"Decrypted data is : '{Decrypt(alphabet, Data_by_user, Shift)}'")
    else:
        print("You have entered the invalid option. So, kindly re-enter the data")

    Continue = input('Enter "C" for Continue & "E" for Exit : ').lower()
    if Continue == "e" or Continue == "exit":
        On = False





















