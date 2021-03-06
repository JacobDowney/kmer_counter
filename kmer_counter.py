"""
Description of kmer_counter
"""

import os
import sys
import argparse
from dna_seq_counter_trie import DnaSeqCounterTrie
from my_bloom_filter import MyBloomFilter
from old_bloom_filter import OldBloomFilter

from bloom_filter import BloomFilter


def kmer_counter(dna_sequence, k):
    """
    Uses the best kmer counting function and return its result
    """
    return dna_seq_set_and_dict(dna_sequence, k)


def dna_seq_counter_trie(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    :Time Complexity: O(nk)
    :Space Complexity: O(n) or O(4^k) at most ????
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    trie = DnaSeqCounterTrie(k)
    for i in range(0, len(dna_seq) - k + 1):
        trie.insert(dna_seq[i:i+k])
    memory_used = sys.getsizeof(trie) + trie.getMemorySize()
    return trie.getDictOfMatches(), memory_used


def dna_seq_bloom_filter(dna_seq, k):
    seq_matches = {}
    error_r = 1 / len(dna_seq)
    bloom_filter = BloomFilter(max_elements=len(dna_seq), error_rate=error_r)
    for i in range(0, len(dna_seq) - k + 1):
        seq = dna_seq[i:i+k]
        if seq in bloom_filter:
            if seq in seq_matches:
                seq_matches[seq] += 1
            else:
                seq_matches[seq] = 2
        else:
            bloom_filter.add(seq)
    return seq_matches, 0

def dna_seq_my_bloom_filter(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    seq_matches = {}
    bloom_filter = MyBloomFilter(len(dna_seq), k)
    for i in range(0, len(dna_seq) - k + 1):
        seq = dna_seq[i:i+k]
        if bloom_filter.is_present_or_insert(seq):
            seq_matches[seq] = seq_matches.get(seq, 1) + 1
    return seq_matches, -1


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
def dna_seq_old_bloom_filter(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    seq_matches = {}
    bloom_filter = OldBloomFilter(len(dna_seq), k)
    pp_list = [0, 0, 0]
    for i in range(0, len(dna_seq) - k + 1):
        seq = dna_seq[i:i+k]
        seen, pp = bloom_filter.is_present_or_insert(seq)
        pp_list[pp] += 1
        if seen:
            if seq in seq_matches:
                seq_matches[seq] += 1
            else:
                seq_matches[seq] = 2
    memory_used = bloom_filter.get_memory_size() + sys.getsizeof(seq_matches)
    print(f"Correct Positives {pp_list[0]}")
    print(f"Incorrect Positives {pp_list[1]}")
    print(f"Correct Negative {pp_list[2]}")
    print(bloom_filter.get_percent_filled())
    return seq_matches, memory_used


# Problems:
# Space is very large
# Not really O(1) when very large bc probing is O(m) or O(logm) w/ m collisions
# Store data on disk which takes more time to read
def dna_seq_set_and_dict(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    :Time Complexity: O(n)
    :Space Complexity: O(n)
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    seq_set = set()
    seq_matches = {}
    for i in range(0, len(dna_seq) - k + 1):
        seq = dna_seq[i:i+k]
        if seq in seq_set:
            #seq_matches[seq] = seq_matches.get(seq, 1) + 1
            if seq in seq_matches:
                seq_matches[seq] += 1
            else:
                seq_matches[seq] = 2
        else:
            seq_set.add(seq)
    memory_used = sys.getsizeof(seq_set) + sys.getsizeof(seq_matches)
    return seq_matches, memory_used


def parse_fasta(filename):
    """
    Parses the fasta file to return a list of tuples containing the dna sequence
    name and it's full sequence following with all new line characters removed
    :param filename: The fasta file that is meant to be parsed
    :return: A list of tuples containing (name_of_dna_seq, dna_seq)
    :rtype: list of tuples
    """
    try:
        file = open(filename, 'r')
    except OSError:
        print(f"Count not open/read file: {args.filename}")
        sys.exit()
    dna_seqs = []
    with file:
        seqs = file.read().split('>')[1:]
        for seq in seqs:
            name_seq = seq.split('\n', 1)
            dna_seqs.append((name_seq[0], name_seq[1].replace('\n', '')))
    return dna_seqs


def main():
    """
    Parses arguments and uses the appropriate kmer counter function to count the
    kmers of length k for a specific fasta file.
    """
    parser = argparse.ArgumentParser(description="Process fna and k arguments")

    kmer_function_group = parser.add_mutually_exclusive_group()
    kmer_function_group.add_argument("-t", "--trie", action="store_true")
    kmer_function_group.add_argument("-b", "--bloom_filter", action="store_true")
    kmer_function_group.add_argument("-d", "--dictionary", action="store_true")

    parser.add_argument("filename", help="The fasta file to process", type=str)
    parser.add_argument("k", help="The length of kmer to count", type=int)
    parser.add_argument("-o", "--output", help="Output the kmer counts to a file",
                        action="store_true")
    args = parser.parse_args()

    dna_seqs = parse_fasta(args.filename)
    kmers = {}
    for dna_seq in dna_seqs:
        if args.trie:
            kmers[dna_seq[0]] = dna_seq_counter_trie(dna_seq[1], args.k)
        elif args.bloom_filter:
            kmers[dna_seq[0]] = dna_seq_bloom_filter(dna_seq[1], args.k)
        elif args.dictionary:
            kmers[dna_seq[0]] = dna_seq_set_and_dict(dna_seq[1], args.k)
        else:
            kmers[dna_seq[0]] = kmer_counter(dna_seq[1], args.k)
    print(kmers)
    if args.output:
        f = open("kmer_count.txt", "a")
        f.write(f"{kmers}\n")



if __name__ == "__main__":
    main()

# end
