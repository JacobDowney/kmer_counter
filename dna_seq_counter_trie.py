"""
Description of Trie Structure
"""

class TrieNode:

    def __init__(self, end):
        if not end:
            self.children = [None] * 4


class DnaSeqCounterTrie:

    # Assumes k is larger than 1

    def __init__(self, k):
        self.__base_to_index = {"a" : 0, "t" : 1, "c" : 2, "g" : 3}
        self.__matches = {}
        self.__depth = k
        self.root = self.getNode(False)

    def getNode(self, end):
        # Returns a new trie node initialized to all None's
        return TrieNode(end)

    def insert(self, key):
        crawl = self.root
        for i in range(0, self.__depth):
            index = self.__base_to_index.get(key[i])       # error if k not atcg
            if not crawl.children[index]:
                crawl.children[index] = self.getNode(i == self.__depth - 1)
                if i == self.__depth - 1:
                    return
            crawl = crawl.children[index]

        # Since we exited the first time we found the sequence and put it in the
        # trie, if we get here its because were seen it again
        self.__matches[key] = self.__matches.get(key, 1) + 1

    def getDictOfMatches(self):
        return self.__matches
