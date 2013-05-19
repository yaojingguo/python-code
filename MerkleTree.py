#!/usr/bin/env python

import hashlib
import unittest

block_size = 10


def hash(data):
  sha1 = hashlib.sha1()
  sha1.update(data)
  return sha1.digest()

def build(pathname):
  # Compute hash for data blocks
  f = open(pathname)
  content = f.read()
  length = len(content)
  block_no = 0
  while offset < length:
    begin = block_no * block_size
    end = (block_no + 1) * block_size
    if end > length:
      end = length
    digest[block_no] = hash(content[begin:end])
    print str(digest[block_no]).encode("hex")

  # Build the binary tree
  for i in range(20):
    top[i] = 0
    for finger in digest:
      top[i] = top[i] ^ finger[i]
  


class Test(unittest.TestCase):
  def test_hash(self):
    data = "01234567890123456789"
    digest = hash(data)



if __name__ == "__main__":
  unittest.main()
