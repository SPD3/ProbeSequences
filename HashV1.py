

class HashV1:
    def __init__(self) -> None:
        self.arr = [None] * 2
        self.number_of_possible_probe_sequences = 2
        self.size_powers_arr = [1,2]
        self.num_of_slots_taken = 0
        self.num_of_elements = 0
    
    
    def __resize__(self, new_size):
        assert new_size >= self.num_of_slots_taken
        key_val_pairs = self.__get_all_key_val_pairs__()

        self.__reset_arr_to_size__(new_size)

        for key, val in key_val_pairs:
            assert self.__insert_into_arr__(key, val)
        
        self.num_of_slots_taken = self.num_of_elements


    def __get_all_key_val_pairs__(self):
        key_val_pairs = [None] * self.num_of_elements
        key_val_pair_count = 0
        for i in range(len(self.arr)):
            if (not self.__is_arr_index_filled__(i)) or \
                    self.__is_arr_index_deleted__(i):
                continue
            key_val_pairs[key_val_pair_count] = self.arr[i]
            key_val_pair_count += 1
        
        return key_val_pairs


    def __is_arr_index_filled__(self, index):
        return self.arr[index] != None


    def __is_arr_index_deleted__(self, index):
        key, val = self.arr[index]
        return key == None and val == None


    def __reset_arr_to_size__(self, size):
        new_arr = [None] * size
        self.size_powers_arr = [1] * size
        self.number_of_possible_probe_sequences = 1
        for i in range(1,size):
            self.size_powers_arr[i] = self.size_powers_arr[i] * size
            self.number_of_possible_probe_sequences *= (i + 1)
        self.arr = new_arr


    def __insert_into_arr__(self, key, val):
        for index in self.__create_probe_sequence__(key, len(self.arr)):
            if not self.__is_arr_index_filled__(index):
                self.arr[index] = (key, val)
                return True
        return False


    def __create_probe_sequence__(self, key, original_arr_size):
        probe_index = hash(key) % self.number_of_possible_probe_sequences
        swap_mem = 0

        for i in range(original_arr_size):
            num_of_valid_indices = original_arr_size - i
            pre_swap_index = probe_index % num_of_valid_indices
            probe_index // num_of_valid_indices

            swap_adjustment = (swap_mem // self.size_powers_arr[pre_swap_index]) % original_arr_size
            index = (pre_swap_index + swap_adjustment) % original_arr_size
            
            yield index

            new_swap_adjustment = (num_of_valid_indices - 1) - pre_swap_index
            assert new_swap_adjustment >= 0
            swap_mem += new_swap_adjustment * self.size_powers_arr[pre_swap_index]


    def get(self, key):
        for index in self.__create_probe_sequence__(key, original_arr_size = len(self.arr)):
            if not self.__is_arr_index_filled__(index):
                return None
            curr_key, current_val = self.arr[index]
            if curr_key == key:
                return current_val
        return None


    def add(self, key, value):
        if self.num_of_slots_taken == len(self.arr):
            self.__resize__(len(self.arr) * 2)
        if self.__insert_into_arr__(key, value):
            self.num_of_slots_taken += 1
            self.num_of_elements += 1
            return True
        return False
        
        
    def delete(self, key):
        for index in self.__create_probe_sequence__(key, len(self.arr)):
            if not self.__is_arr_index_filled__(index):
                return False
            curr_key, _ = self.arr[index]
            if curr_key == key:
                self.__set_index_as_deleted__(index)
                self.num_of_elements -= 1
                if self.num_of_elements <= (len(self.arr) // 4):
                    self.__resize__(len(self.arr) // 2)
                return True
        return False


    def __set_index_as_deleted__(self, index):
        self.arr[index] = (None, None)