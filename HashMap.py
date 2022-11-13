

class HashMap:
    def __init__(self) -> None:
        self._arr = [None] * 2
        self._number_of_possible_probe_sequences = 2
        self._size_powers_arr = [1,2]
        self._num_of_slots_taken = 0
        self._num_of_elements = 0
    
    
    def _resize(self, new_size:int):
        assert new_size >= self._num_of_slots_taken
        key_val_pairs = self._get_all_key_val_pairs()

        self._reset_arr_to_size(new_size)

        for key, val in key_val_pairs:
            assert self._insert_into_arr(key, val)
        
        self._num_of_slots_taken = self._num_of_elements


    def _get_all_key_val_pairs(self):
        key_val_pairs = [None] * self._num_of_elements
        key_val_pair_count = 0
        for i in range(len(self._arr)):
            if (not self._is_arr_index_filled(i)) or \
                    self._is_arr_index_deleted(i):
                continue
            key_val_pairs[key_val_pair_count] = self._arr[i]
            key_val_pair_count += 1
        
        return key_val_pairs


    def _is_arr_index_filled(self, index:int):
        return self._arr[index] != None


    def _is_arr_index_deleted(self, index:int):
        key, val = self._arr[index]
        return key == None and val == None


    def _reset_arr_to_size(self, size:int):
        new_arr = [None] * size
        self._size_powers_arr = [1] * size
        self._number_of_possible_probe_sequences = 1
        for i in range(1,size):
            self._size_powers_arr[i] = self._size_powers_arr[i-1] * size
            self._number_of_possible_probe_sequences *= (i + 1)
        self._arr = new_arr


    def _insert_into_arr(self, key:str, val:object):
        for index in self._create_probe_sequence(key):
            if not self._is_arr_index_filled(index):
                self._arr[index] = (key, val)
                return True
        return False


    def _create_probe_sequence(self, key:str):
        probe_index = hash(key) % self._number_of_possible_probe_sequences
        swap_mem = 0
        arr_size = len(self._arr)

        for i in range(arr_size):
            num_of_valid_indices = arr_size - i

            pre_swap_index = probe_index % num_of_valid_indices
            probe_index // num_of_valid_indices

            index = self._get_index_adjusted_for_swaps(pre_swap_index, swap_mem)
            yield index

            swap_mem = self._get_swap_encoding(num_of_valid_indices, \
                pre_swap_index, swap_mem)
            continue

    def _get_index_adjusted_for_swaps(self, pre_swap_index:int,\
         swap_mem:int):
        arr_size = len(self._arr)
        swap_adjustment = (swap_mem // self._size_powers_arr[pre_swap_index]) \
            % arr_size
        index = (pre_swap_index + swap_adjustment) % arr_size
        return index
    

    def _get_swap_encoding(self, num_of_valid_indices:int, \
         pre_swap_index:int, swap_mem:int):
        last_index = self._get_index_adjusted_for_swaps(\
            num_of_valid_indices - 1, swap_mem)
        arr_size = len(self._arr)

        swap_encoding = (last_index - pre_swap_index) % arr_size
        curr_pre_swap_encoding = swap_mem // \
            self._size_powers_arr[pre_swap_index] % arr_size

        swap_mem += (swap_encoding - curr_pre_swap_encoding) * \
            self._size_powers_arr[pre_swap_index]
        return swap_mem


    def get(self, key:str):
        for index in self._create_probe_sequence(key):
            if not self._is_arr_index_filled(index):
                return None
            curr_key, current_val = self._arr[index]
            if curr_key == key:
                return current_val

        return None


    def add(self, key:str, value:object):
        if self._num_of_slots_taken == len(self._arr):
            self._resize(len(self._arr) * 2)
        if self._insert_into_arr(key, value):
            self._num_of_slots_taken += 1
            self._num_of_elements += 1
            return True
        return False
        
        
    def delete(self, key:int):
        for index in self._create_probe_sequence(key):
            if not self._is_arr_index_filled(index):
                return False
            curr_key, _ = self._arr[index]
            if curr_key == key:
                self._set_index_as_deleted(index)
                self._num_of_elements -= 1
                if self._num_of_elements <= (len(self._arr) // 4):
                    self._resize(len(self._arr) // 2)
                return True
        return False


    def _set_index_as_deleted(self, index:int):
        self._arr[index] = (None, None)