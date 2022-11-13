from ..HashMap import HashMap

def setup_hash_map(hash_map):
    for i in range(1000):
        hash_map.set(str(i), i)

def test_insertion():
    hash_map = HashMap()
    assert hash_map.get("abc") is None
    
    hash_map.set("abc", 1)
    assert hash_map.get("abc") == 1

    hash_map.set("def", 3)
    assert hash_map.get("def") == 3

    setup_hash_map(hash_map)

    for i in range(1000):
        assert hash_map.get(str(i)) == i, ("Val: " + str(i) + "\ni: " + str(i))

def test_deletion():
    hash_map = HashMap()
    assert hash_map.get("abc") is None
    hash_map.set("abc", 1)
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

def test_probe_sequence_generation():
    def test_probe_sequence_with_size_exponent(size_exponent):
        hash_map = HashMap()
        num_of_values = 2**size_exponent
        for i in range(num_of_values):
            hash_map.set(str(i), i)
        
        for i in range(num_of_values):
            probe_sequence = []
            for index in hash_map._create_probe_sequence(str(i)):
                probe_sequence.append(index)
            assert len(probe_sequence) == len(hash_map._arr), ("i: " + str(i))
            assert len(set(probe_sequence)) == len(hash_map._arr), ("i: " + str(i))
    
    test_probe_sequence_with_size_exponent(2)
    test_probe_sequence_with_size_exponent(5)
    test_probe_sequence_with_size_exponent(8)