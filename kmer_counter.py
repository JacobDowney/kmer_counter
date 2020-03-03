"""
Description of kmer_counter
"""

import time

import os
import sys
import argparse
from dna_seq_counter_trie import DnaSeqCounterTrie

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
    Space Complexity: O(n) ????
    :param dna_seq: A dna sequence string to be analyzed
    :param k: Length of dna sequence to search for matches
    :return: A list of dictionaries with name and sequence pairs
    """
    trie = DnaSeqCounterTrie(k)
    for i in range(0, len(dna_seq) - k + 1):
        trie.insert(dna_seq[i:i+k])
    return trie.getDictOfMatches()

def dna_seq_bloom_filter(dna_seq, k):
    """
    Description
    """
    seq_matches = {}
    return seq_matches

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
    return seq_matches




# end
