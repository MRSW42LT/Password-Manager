from cryptography.fernet import Fernet # import cryptography module


masterKey = input ("Master key: ") # get master password 123

    # This will create a new key and save it as key.key
    # This key will be used to encrypt and decrypt the passwords.txt file
    # This key should be kept safe and not shared with anyone
    # If you lose this key, you will lose access to your passwords
    # If you want to use a different key, replace the key.key file with the new key
    
# uncomment the following lines to create a new key
#def encrypt_key(): #
#    key = Fernet.generate_key()
#    with open('key.key', 'wb') as key_file:
#        key_file.write(key)
# 
#encrypt_key() 


def load_key(): # load the previously generated key
    return open('key.key', 'rb').read()
key = load_key() + masterKey.bytes # load the key
fer = Fernet(key) # create a Fernet object

def view_passwords(): # decrypt and view passwords
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            user, passw = line.split('|')
            print ("User:",user + " " + "Password:",fer.decrypt(passw.encode()).decode())

def add_password(): # encrypt and add passwords
    account_name = input ("Account name: ") # get account name
    account_password = input ("Account password: ") # get account password
    with open('passwords.txt', 'a') as f:
        f.write(account_name + "|" + fer.encrypt(account_password.encode()).decode()+'\n') # write to file # encrypt password # convert to bytes

while True: # main loop
    mode = input ("(1): View passwords \n(2): New password \n Press q to quit? ") # get mode
    if mode == "q":
        exit()
    if mode == "1":
        view_passwords()
    elif mode == "2":
        add_password()
    else:
        print ("Invalid mode")
        continue
