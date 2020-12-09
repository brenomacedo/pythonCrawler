import hashlib
from art import text2art
from termcolor import colored

print(colored(text2art('HASH  GEN'), 'red', attrs=['bold']))

string = str(input('Digite o texto para gerar o hash')).encode('utf-8')

print(colored('digite 0 para MD5', 'blue'))
print(colored('digite 1 para SHA1', 'blue'))
print(colored('digite 2 para SHA256', 'blue'))
print(colored('digite 3 para SHA512', 'blue'))

hash_type = int(input(colored('Qual hash utilizar?', 'blue')))

if hash_type == 0:
    hash = hashlib.md5(string)
elif hash_type == 1:
    hash = hashlib.sha1(string)
elif hash_type == 2:
    hash = hashlib.sha256(string)
elif hash_type == 3:
    hash = hashlib.sha512(string)

print(hash.hexdigest())
