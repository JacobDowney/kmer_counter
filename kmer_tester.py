"""
Description of algorithm tester
"""

import time

from dna import dna_full
from dna import dna_short

from kmer_counter import dna_seq_set_and_dict
from kmer_counter import dna_seq_counter_trie
from kmer_counter import dna_seq_bloom_filter


def main():
    run_k_start_finish(2, 51)


def run_k(k):
    dna_seq = dna_full.replace("\n", "")
    func_names = ["dna_seq_set_and_dict", "dna_seq_counter_trie"]
    functions = [dna_seq_set_and_dict, dna_seq_counter_trie]
    func_times, func_memories, func_results = run_functions(functions, dna_seq, k)

    for i in range(0, len(func_names)):
        print "Name: " + str(func_names[i])
        print "Time: " + str(func_times[i])
        print "Memory used: " + str(func_memories[i])
        print ""


def run_k_start_finish(start, finish):
    dna_seq = dna_full.replace("\n", "")
    func_names = ["dna_seq_set_and_dict", "dna_seq_bloom_filter"]
    functions = [dna_seq_set_and_dict, dna_seq_bloom_filter]
    func_times = []
    func_mems = []
    func_results = []

    for func in functions:
        f_times = []
        f_mems = []
        f_results = []
        for i in range(start, finish):
            start_time = time.time()
            res_, mem_ = func(dna_seq, i)
            f_times.append(time.time() - start_time)
            f_mems.append(mem_)
            f_results.append(res_)
        func_times.append(f_times)
        func_mems.append(f_mems)
        func_results.append(f_results)

    name = "k  | "
    for func_name in func_names:
        name += func_name + "       "
    print name
    for i in range(0, len(func_times[0])):
        line = ("%02d | " % (i + start))
        for j in range(0, len(functions)):
            line += ("%5.3f , %12d" % (func_times[j][i], func_mems[j][i]))
            if j != len(functions) - 1:
                line += "   |   "
        print line


def run_functions(functions, dna_seq, k):
    func_times = []
    func_results = []
    func_memories = []

    for i in range(0, len(functions)):
        start = time.time()
        res_, mem_ = functions[i](dna_seq, k)
        func_results.append(res_)
        func_memories.append(mem_)
        func_times.append(time.time() - start)
    return func_times, func_memories, func_results



if __name__ == "__main__":
    main()
