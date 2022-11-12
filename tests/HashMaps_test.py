import unittest
from ProbeSequences.HashV1 import HashV1

def test5():
    assert 5 == 5 

def test5WithHash():
    hashV1 = HashV1()
    assert 5 == hashV1.doSomething()