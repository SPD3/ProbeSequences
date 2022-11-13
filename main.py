from HashMap import HashMap

def main():
    hash_map = HashMap()

    print('hash_map.set("abc", 30): ', hash_map.set("abc", 30))
    print('hash_map.set("def", 20): ', hash_map.set("def", 20))
    print('hash_map.set("ghi", 40): ', hash_map.set("ghi", 40))
    print()
    
    print('hash_map.get("abc"): ', hash_map.get("abc"))
    print('hash_map.get("def"): ', hash_map.get("def"))
    print('hash_map.get("ghi"): ', hash_map.get("ghi"))
    print('hash_map.get("jkl"): ', hash_map.get("jkl"))
    print()

    print('hash_map.delete("def"): ', hash_map.delete("def"))
    print('hash_map.delete("def"): ', hash_map.delete("def"))
    print('hash_map.delete("jkl"): ', hash_map.delete("jkl"))
    print()

    print('hash_map.get("abc"): ', hash_map.get("abc"))
    print('hash_map.get("def"): ', hash_map.get("def"))
    print('hash_map.get("ghi"): ', hash_map.get("ghi"))
    print('hash_map.get("jkl"): ', hash_map.get("jkl"))


if __name__ == "__main__":
    main()