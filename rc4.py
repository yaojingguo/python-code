#!/usr/bin/env python3

A = ord('a')

def info_num(text):
  for c in text:
    print(ord(c) - A, " ", end="")
  print()

# Implementation of the example in http://en.wikipedia.org/wiki/Keystream
def keystream(plain, key):
  i = 0
  length = len(plain)
  result = ""
  while i < length:
    byte = (ord(plain[i]) - A + ord(key[i % 26]) - A) % 26
    print(byte, " ", end="")
    result += chr(byte + A)
    i = i + 1
  print()
  print("text: ", result)

# Refer to http://en.wikipedia.org/wiki/Rc4#The_key-scheduling_algorithm_.28KSA.29
def KSA(key):
  S = [c for c in range(256)]
  j = 0
  keylength = len(key)
  for i in range(256):
    j = (j + S[i] + key[i % keylength]) % 256
    S[i], S[j] = S[j], S[i]
  return S

# Refer to http://en.wikipedia.org/wiki/Rc4#The_pseudo-random_generation_algorithm_.28PRGA.29
def PRGA(data, S):
  i = 0
  j = 0
  m = 0
  length = len(data)
  while m < length:
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    k = data[m] ^ S[(S[i] + S[j]) % 256]
    print("%02X" % k, end="")
    m += 1;
  print()

def rc4(data_text, key_text):
  data = [ord(c) for c in data_text]
  key = [ord(c) for c in key_text]
  S = KSA(key)
  PRGA(data, S)


def test_keystream():
  plain = "attackatdawn"
  key = "kjcngmlhylyu"
  info_num(plain)
  info_num(key)
  keystream(plain, key)

def test_KSA():
  key = [97, 98, 99, 100, 101]
  S = KSA(key)
  print(S)

def test_rc4():
  rc4("Plaintext", "Key")

test_keystream()
test_KSA()
test_rc4()
