"""
Description of Bloom Filter
"""

import sys

from random import randint
from random import choice

class HashFunction:

    def __init__(self, num_bits, prime, odd):
        self.__num_bits = num_bits
        self.__prime = prime
        self.__odd = odd

    def get_hash(self, word):
        return ((((hash(word) % self.__num_bits) * self.__prime) % self.__num_bits) * self.__odd) % self.__num_bits


class BloomFilter:

    def __init__(self, num_bits, num_hash_funcs):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.__bit_set = [False] * num_bits
        self.__hash_funcs = []
        for i in range(0, num_hash_funcs):
            hash_func = HashFunction(num_bits, choice(primes), randint(1, 51) - 1)
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
