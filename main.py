from cryptography.fernet import Fernet

masterKey = input ("Master key: ") # get master password 123

''' # Uncomment this to generate a new key 
    # This will create a new key and save it as key.key
    # This key will be used to encrypt and decrypt the passwords.txt file
    # This key should be kept safe and not shared with anyone
    # If you lose this key, you will lose access to your passwords
    # If you want to use a different key, replace the key.key file with the new key
def encrypt_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

encrypt_key()
'''

def load_key():
    return open('key.key', 'rb').read() # load the previously generated key

def view_passwords(): # decrypt and view passwords
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            account_name, account_password = line.split('|')
            print ("User:",account_name + " " + "Password:",account_password)

def add_password(): # encrypt and add passwords
    account_name = input ("Account name: ") # get account name
    account_password = input ("Account password: ") # get account password
    with open('passwords.txt', 'a') as f:
        f.write(account_name + "|" + account_password+'\n')

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
