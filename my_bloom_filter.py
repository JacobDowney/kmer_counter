"""
Description of Bloom Filter
"""

import sys
import math

from random import randint
from random import choice

from bitarray import bitarray

class HashFunction:

    def __init__(self, num_bits, prime, odd):
        self.__num_bits = num_bits
        self.__prime = prime
        self.__odd = odd

    def get_hash(self, word):
        return ((((hash(word) % self.__num_bits) * self.__prime) % self.__num_bits) * self.__odd) % self.__num_bits


class MyBloomFilter:

    # Why does the num of expected repititions or matches not matter in formula?
    def __init__(self, num_elements, k, false_pos_rate):
        false_pos_rate = 1 / num_elements
        num_bits = math.ceil((num_elements * math.log(false_pos_rate)) / math.log(1 / (2**math.log(2))))
        num_hash_funcs = round((num_bits / num_elements) * math.log(2))

        self.__bit_set = bitarray(num_bits)
        self.__bit_set.setall(False)
        self.__hash_funcs = []

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for i in range(0, num_hash_funcs):
            hash_func = HashFunction(num_bits, choice(primes), (randint(1, 51) * 2) - 1)
            self.__hash_funcs.append(hash_func)

    def is_present_or_insert(self, word):
        present = True
        for hash_func in self.__hash_funcs:
            hash = hash_func.get_hash(word)
            if self.__bit_set[hash] == False:
                present = False
                self.__bit_set[hash] = True
        return present

    def get_memory_size(self):
        return sys.getsizeof(self.__bit_set) + sys.getsizeof(self.__hash_funcs)
