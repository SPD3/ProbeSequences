from ..HashV1 import HashV1
import random

def test5():
    assert 5 == 5 

def setup_hash_map(hash_map):
    for i in range(1000):
        hash_map.add(str(i), i)

def insertion_tests(hash_map):
    assert hash_map.get("abc") is None
    
    assert hash_map.add("abc", 1)
    assert hash_map.get("abc") == 1

    assert hash_map.add("def", 3)
    assert hash_map.get("def") == 3

    setup_hash_map(hash_map)

    for i in range(1000):
        assert hash_map.get(str(i)) == i, ("Val: " + str(i) + "\ni: " + str(i))

def deletion_tests(hash_map):
    assert hash_map.get("abc") is None
    hash_map.add("abc", 1)
    assert hash_map.get("abc") == 1
    assert hash_map.delete("abc")
    assert hash_map.get("abc") is None

    assert not hash_map.delete("efg")

    setup_hash_map(hash_map)
    for i in range(250, 750):
        hash_map.delete(str(i))
    
    for i in range(250,750):
        assert hash_map.get(str(i)) is None, ("i: " + str(i))

    for i in range(250):
        assert hash_map.get(str(i)) == i, ("Val: " + str(i))

    for i in range(750,1000):
        assert hash_map.get(str(i)) == i, ("Val: " + str(i))

def test_hash_map():

    hashV1 = HashV1()
    insertion_tests(hashV1)
    hashV1 = HashV1()
    deletion_tests(hashV1)

def test_probe_sequence_generation():
    def test_probe_sequence_with_size_exponent(size_exponent):
        hash_map = HashV1()
        num_of_values = 2**size_exponent
        for i in range(num_of_values):
            hash_map.add(str(i), i)
        
        for i in range(num_of_values):
            probe_sequence = []
            for index in hash_map._create_probe_sequence(str(i)):
                probe_sequence.append(index)
            assert len(probe_sequence) == len(hash_map._arr), ("i: " + str(i))
            assert len(set(probe_sequence)) == len(hash_map._arr), ("i: " + str(i))
    
    test_probe_sequence_with_size_exponent(2)
        