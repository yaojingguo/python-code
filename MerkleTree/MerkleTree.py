#!/usr/bin/env python
import hashlib
import unittest

# Play with Merkle tree concepts.

block_size = 10

def hash(data):
  sha1 = hashlib.sha1()
  sha1.update(data)
  print sha1.hexdigest()
  return sha1.digest()

# The height of the Merkle tree is 1. It is like a hash list.
def build(pathname):
  print("file: %s" % pathname)
  # Compute hash for data blocks
  f = open(pathname)
  content = f.read()
  length = len(content)
  block_no = 0
  digest = []
  print "Digest:"
  while (block_no * block_size) < length:
    begin = block_no * block_size
    end = (block_no + 1) * block_size
    if end > length:
      end = length
    digest.append(hash(content[begin:end]))
    block_no += 1

  # Build the binary tree
  top = []
  for i in range(20):
    byte = 0
    for finger in digest:
      byte = byte ^ ord(finger[i])
    top.append(byte)
  str = ""
  for byte in top:
    str += hex(byte)[2:]
  print "top: ", str


class Test(unittest.TestCase):
  def test_hash(self):
    build("data_1")
    build("data_2")

if __name__ == "__main__":
  unittest.main()
