

class HashV1:
    def __init__(self) -> None:
        self.arr = [None] * 2
        self.current_factorial = 2
        self.size_powers_arr = [1,2]
        self.num_of_slots_taken = 0
        self.num_of_elements = 0
    
    
    def __resize__(self, new_size):
        assert new_size >= self.num_of_slots_taken
        new_arr = [None] * new_size
        self.size_powers_arr = [1] * new_size
        self.current_factorial = 1

        for i in range(1,new_size):
            self.size_powers_arr[i] = self.size_powers_arr[i] * new_size
            self.current_factorial *= (i + 1)
        self.num_of_slots_taken = 0
        for item in self.arr:
            if item is None:
                continue
            key, val = item
            if key is None:
                continue
            
            assert self.__insert_into_arr__(key, val, new_arr)
            self.num_of_slots_taken += 1
        
        self.arr = new_arr

    def __insert_into_arr__(self, key, val, arr):
        for index in self.__create_probe_sequence__(key, len(arr)):
            if arr[index] is None:
                arr[index] = (key, val)
                return True
        return False

    def __create_probe_sequence__(self, key, original_arr_size):
        probe_index = hash(key) % self.current_factorial
        swap_mem = 0

        for i in range(original_arr_size):
            valid_probe_sub_arr_size = original_arr_size - i
            pre_swap_index = probe_index % valid_probe_sub_arr_size
            probe_index // valid_probe_sub_arr_size

            swap_adjustment = (swap_mem // self.size_powers_arr[pre_swap_index]) % original_arr_size
            index = (pre_swap_index + swap_adjustment) % original_arr_size
            
            yield index

            swap_mem_diff = (valid_probe_sub_arr_size - 1) - pre_swap_index
            assert swap_mem_diff >= 0
            swap_mem += swap_mem_diff * self.size_powers_arr[pre_swap_index]
            

    def get(self, key):
        for index in self.__create_probe_sequence__(key, original_arr_size = len(self.arr)):
            if self.arr[index] is None:
                return None
            curr_key, current_val = self.arr[index]
            if curr_key == key:
                return current_val
        return None

    def add(self, key, value):
        if self.num_of_slots_taken == len(self.arr):
            self.__resize__(len(self.arr) * 2)
        if self.__insert_into_arr__(key, value, self.arr):
            self.num_of_slots_taken += 1
            self.num_of_elements += 1
            return True
        return False
        
        
    def delete(self, key):
        for index in self.__create_probe_sequence__(key, len(self.arr)):
            if self.arr[index] == None:
                return False
            curr_key, _ = self.arr[index]
            if curr_key == key:
                self.arr[index] = (None, None)
                self.num_of_elements -= 1
                if self.num_of_elements <= (len(self.arr) // 4):
                    self.__resize__(len(self.arr) // 2)
                return True
        return False

    def __str__(self) -> str:
        return str(self.arr)