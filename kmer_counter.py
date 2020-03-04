"""
Description of kmer_counter
"""

import time

import os
import sys
import argparse
from dna_seq_counter_trie import DnaSeqCounterTrie
from bloom_filter import BloomFilter

from dna import dna_full
from dna import dna_short
#from Bio.Seq import Seq

def read_fasta_seqio(filename):
    """
    Description
    """

    parsed = SeqIO.parse(filename, "fasta")
    print parsed

def read_fasta_lbl(filename):
    """
    Read a fasta file and return a list of dictionaries with name and sequence
    pairs.
    :param filename: The file name to read from
    :return: A list of dictionaries with name and sequence pairs
    """
    """
    list_of_sequences = []
    if os.path.exists(filename):
        try:
            file = open(filename, 'r')
            while True:
                char = file.read(1)
                if not char:
                    break
                if char == "\n":
                    continue
                if char == ">":

        except IOError as e:
            print "Unable to open file: " + filename
        except:
            print "Unexpected error:", sys.exc_info()[0]

    return list_of_sequences



    try:
        if filename.endswith('fna'):
            file = open(filename, 'r')
    except IO
    file_contents = open(filename).read()
    return file_contents
    """


def kmer_counter(dna_sequence, k):
    """
    Description
    """
    brute_force(dna_sequence)


### Don't know Space Complexity yet ###
def dna_seq_counter_trie(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    Time Complexity: O(nk)
    Space Complexity: O(n) or O(4^k) at most ????
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    trie = DnaSeqCounterTrie(k)
    for i in range(0, len(dna_seq) - k + 1):
        trie.insert(dna_seq[i:i+k])
    memory_used = sys.getsizeof(trie) + trie.getMemorySize()
    return trie.getDictOfMatches(), memory_used

# Probabilistic data structure conceived by Burton Howard Bloom in 1970
# Tests whether an element is a member of a set

# Google uses them to store malicious url

# More hash functions used the more probabilistic u found it, but more space
#       will be needed in the bit array to store the more hash bits

# M number of hash functions -> m checks on the bloom filter, but its constant

# Store the bits as actual base 10 numbers

# Disadvantage: you need to know the expected size of input -> len(dna_seq)

# 40 million records -> 1 in 10million mistake, 159mb storage, 23 hash functions

# More than 2 hash functions
def dna_seq_bloom_filter(dna_seq, k):
    """
    Description
    """
    num_bits = 1048576
    num_hash_funcs = 7
    seq_matches = {}
    bloom_filter = BloomFilter(num_bits, num_hash_funcs)
    for i in range(0, len(dna_seq) - k + 1):
        seq = dna_seq[i:i+k]
        if bloom_filter.is_present_or_insert(seq):
            seq_matches[seq] = seq_matches.get(seq, 1) + 1
    memory_used = bloom_filter.get_memory_size() + sys.getsizeof(seq_matches)
    return seq_matches, memory_used

# Problems:
# Space is very large
# Not really O(1) when very large bc probing is O(m) or O(logm) w/ m collisions
# Store data on disk which takes more time to read
def dna_seq_set_and_dict(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    Time Complexity: O(n)
    Space Complexity: O(n) ???
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    seq_set = set()
    seq_matches = {}
    for i in range(0, len(dna_seq) - k + 1):
        seq = dna_seq[i:i+k]
        if seq in seq_set:
            seq_matches[seq] = seq_matches.get(seq, 1) + 1
        else:
            seq_set.add(seq)
    memory_used = sys.getsizeof(seq_set) + sys.getsizeof(seq_matches)
    return seq_matches, memory_used




# end
