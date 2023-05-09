import random

max_ascii = 126
message = input("Enter the message: ")
def encrypt(message):
  if len(message) == 0:
    return 0
  else:
    return ord(message[0]) * (max_ascii ** (len(message) - 1)) + encrypt(message[1:])
# this function works till ~ symbol
def leading_power(n):
  if n / max_ascii < 1 :
    return 0
  else :
    return 1 + leading_power(n / max_ascii)

def decrypt(cipher):
  if leading_power(cipher) == 0:
    return chr(cipher)
  
  c = int(cipher /  (max_ascii ** leading_power(cipher)))                      
  

  return chr(c) + decrypt(cipher % (max_ascii ** leading_power(cipher)))

print(encrypt(message))
print(decrypt(encrypt(message)))

def individual_key(a, b):
  n = random.randint(a, b)
  while not isPrime(n):
    n = random.randint(a, b)
  return 2 ** n - 1 # Mersenne primes

p = individual_key(51, 71)

q = individual_key(51, 71)

while q == p:
  q = individual_key(51, 71)

e = int((p + q) / 2 - random.randint(0, 1000))

def private_key(p, q, e):
  for k in range(1, (p - 1) * (q - 1) + 1):
    if (1 + k * (p - 1) * (q - 1)) % e == 0:
      return int((1 + k * (p - 1) * (q - 1)) / e)

d = private_key(p, q, e)

def digital_signature(message, d, n):
  return (message ** d) % n

def verify_signature(message, signature, e, n):
  return message == (signature ** e) % n

def message_to_cipher(message, e, n):
  return (message ** e) % n

def cipher_to_message(cipher, d, n):
  return (cipher ** d) % n
