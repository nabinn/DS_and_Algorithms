# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}  # key = character; value = TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # start from root node
        current_node = self.root
        # for each character in the word
        for ch in word:
            if ch not in current_node.children:
                # add a new TrieNode with key=ch and value=new TrieNode
                current_node.children[ch] = TrieNode()
            # switch to the child TrieNode
            current_node = current_node.children[ch]
        # for last TrieNode, set is_word to True
        current_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                return False
            current_node = current_node.children[ch]
        return current_node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for ch in prefix:
            if ch not in current_node.children:
                return False
            current_node = current_node.children[ch]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    res1 = trie.search("apple")  # returns True
    res2 = trie.search("app")  # returns False
    res3 = trie.startsWith("app")  # returns True
    trie.insert("app")
    res4 = trie.search("app")  # returns True
    
    print(res1, res2, res3, res4) # should print True False True True
