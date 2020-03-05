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
    func_names = ["dna_seq_set_and_dict", "dna_seq_bloom_filter"]
    functions = [dna_seq_set_and_dict, dna_seq_bloom_filter]

    dna_seq = dna_full.replace("\n", "")

    run_k_start_finish(func_names, functions, dna_seq, 2, 35)
    #run_k(func_names, functions, dna_seq, 26)


def run_k(func_names, functions, dna_seq, k):
    func_times = []
    func_mems = []
    func_results = []

    for func in functions:
        start_time = time.time()
        res_, mem_ = func(dna_seq, k)
        func_times.append(time.time() - start_time)
        func_mems.append(mem_)
        func_results.append(res_)

    for i in range(0, len(func_names)):
        #print "{} : {} : {}".format(func_names[i], func_times[i], func_mems[i])
        #print(func_results[i])
        print(len(func_results[i]))
    #print(func_results[0])


def run_k_start_finish(func_names, functions, dna_seq, start, finish):
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
    print(name)
    for i in range(0, len(func_times[0])):
        line = ("%02d | " % (i + start))
        for j in range(0, len(functions)):
            line += ("%5.3f , %12d" % (func_times[j][i], len(func_results[j][i])))
            if j != len(functions) - 1:
                line += "   |   "
        print(line)



if __name__ == "__main__":
    main()
