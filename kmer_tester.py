"""
Description of algorithm tester
"""

import time

from dna import dna_full
from dna import dna_short

from kmer_counter import dna_seq_big_dictionary
from kmer_counter import dna_seq_counter_trie
from kmer_counter import dna_seq_bloom_filter


def main():
    dna_seq = dna_full.replace("\n", "")
    func_names = ["dna_seq_big_dictionary", "dna_seq_counter_trie"]
    functions = [dna_seq_big_dictionary, dna_seq_counter_trie]

    func_times, func_results = run_functions(functions, dna_seq, 2)

    for i in range(0, len(func_names)):
        print func_names[i]
        print func_times[i]
        print func_results[i]
        print ""

def run_functions(functions, dna_seq, k):
    func_times = []
    func_results = []

    for i in range(0, len(functions)):
        start = time.time()
        func_results.append(functions[i](dna_seq, k))
        func_times.append(time.time() - start)
    return func_times, func_results



if __name__ == "__main__":
    main()
