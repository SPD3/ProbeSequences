from ..HashV1 import HashV1
import random

def test5():
    assert 5 == 5 

def setup_hash_map(hash_map):
    for i in range(1000):
        hash_map.add(str(i), i)

def insertion_tests(hash_map):
    assert hash_map.get("abc") is None
    
    hash_map.add("abc", 1)
    assert hash_map.get("abc") == 1

    hash_map.add("def", 3)
    assert hash_map.get("def") == 3

    setup_hash_map(hash_map)

    for i in range(20):
        val = random.randint(0,999)
        assert hash_map.get(str(val)) == val, ("Val: " + str(val))

def deletionTests(hash_map):
    assert hash_map.get("abc") is None
    hash_map.add("abc", 1)
    assert hash_map.get("abc") == 1
    hash_map.delete("abc")
    assert hash_map.get("abc") is None

    hash_map.delete("efg")

    setup_hash_map(hash_map)
    for i in range(250, 750):
        hash_map.delete(str(i))
    
    for i in range(20):
        val = random.randint(250,749)
        assert hash_map.get(str(val)) is None, ("Val: " + str(val))

    for i in range(20):
        val = random.randint(0,499)
        if val >= 250:
            val = val + 500
        assert hash_map.get(str(val)) == val, ("Val: " + str(val))
    

def testHashV1():
    hashV1 = HashV1()
    insertion_tests(hashV1)
    deletionTests(hashV1)
