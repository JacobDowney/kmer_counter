"""
Description of Bloom Filter
"""

import math
import mmh3
from bitarray import bitarray

class MyBloomFilter:

    def __init__(self, num_elements, k):
        false_pos_rate = 1 / num_elements
        self.num_bits = self.get_num_bits(num_elements, false_pos_rate)
        self.num_hash_funcs = self.get_num_hash_funcs(self.num_bits, num_elements)

        self.bit_array = bitarray(self.num_bits)
        self.bit_array.setall(0)

    def is_present_or_insert(self, element):
        found = True
        for i in range(self.num_hash_funcs):
            hash = mmh3.hash(element, i) % self.num_bits
            if self.bit_array[hash] == False:
                self.bit_array[hash] = True
                found = False
        return found

    @classmethod
    def get_num_bits(self, n, p):
        """
        m = -(n * lg(p)) / (lg(2)^2)
        """
        m = -(n * math.log(p)) / (math.log(2)**2)
        return int(m)

    @classmethod
    def get_num_hash_funcs(self, m, n):
        """
        k = (m / n) * lg(2)
        """
        k = (m / n) * math.log(2)
        return int(k)
