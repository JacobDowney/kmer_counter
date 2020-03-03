"""
Description of kmer_counter
"""

import time

import os
import sys
import argparse
from dna_seq_counter_trie import DnaSeqCounterTrie
from dna import dna_str
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

def dna_seq_counter_trie(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    Time Complexity: O(nk)
    Space Complexity: O(n) ???? ###### FIND OUT #####
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    trie = DnaSeqCounterTrie(k)
    for i in range(0, len(dna_seq) - k + 1):
        trie.insert(dna_seq[i:i+k])
    return trie.getDictOfMatches()

def brute_force_with_hashing(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values. Compares the dna
    sequence hashes first which is an O(1) comparison instead of O(k) comparison
    then when the hashes are equal compares the strings to make sure they are
    the same. ###### NAME OF ALGORITHM #####
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    seq_matches = {}
    for i in range(0, len(dna_seq) - k):
        i_seq = dna_seq[i:i+k]
        i_hash = hash(dna_seq[i:i+k])
        for j in range(i + 1, len(dna_seq) - k + 1):
            if i_hash == hash(dna_seq[j:j+k]) and i_seq == dna_seq[j:j+k]:
                seq_matches[i_seq] = seq_matches.get(i_seq, 1) + 1
    return seq_matches

def brute_force(dna_seq, k):
    """
    Returns a dictionary of dna sequences of length k as keys that have appeared
    more than two times with the number of times as the values.
    Time Complexity: O(n^2 * k)
    Space Complexity: O(n)
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    seq_matches = {}
    for i in range(0, len(dna_seq) - k):
        i_seq = dna_seq[i:i+k]
        for j in range(i + 1, len(dna_seq) - k + 1):
            if i_seq == dna_seq[j:j+k]:
                seq_matches[i_seq] = seq_matches.get(i_seq, 1) + 1
    return seq_matches


dna_str = dna_str.replace("\n", "")

dna = "tacgtactg"

"""
time_1 = time.time()
dict_1 = brute_force_with_hashing(dna_str, 2)
time_1_end = time.time()
"""

time_2 = time.time()
dict_2 = dna_seq_counter_trie(dna_str, 2)
time_2_end = time.time()

#print "Function 1 Time: " + str(time_1_end - time_1)
print "Function 2 Time: " + str(time_2_end - time_2)

print ""

#print dict_1
print dict_2


# end
