from libs.template.base import Search
from libs.log import exception, timed, create_logger
from itertools import compress
from typing import List, Union
logger = create_logger("SearchModule")


class TrieTreeSearch(Search):

    class TrieNode:
        def __init__(self):
            self.child = {}
            self.is_end = False

    def __init__(self):
        super().__init__()
        self._root = self.TrieNode()
        logger.info(f"Use {self.__class__.__name__} for seaching task.")
    
    @timed(logger)
    @exception(logger)
    def fit(self, 
            words:List[str]) -> List[str]:
        
        for word in words:
            self._insert(word)
            
        logger.info(f"Budding {self.__class__.__name__} successfully, within {len(words)} words.")
    
    @timed(logger)
    @exception(logger)
    def transform(self, 
                  docs:List[str]) -> List[str]:
        

        if len(self._root.child)<1:
            raise ValueError("Please fit your target word to build trie-tree befor transform your documents: \n"
                             "`from __ import TrieTreeSearcher` \n"
                             "`searcher = TrieTreeSearcher()` \n"
                             "`searcher.fit(__your data__)` \n")
        is_matches = []
        for doc in docs:
            is_matches.append(self._find(doc))
        
        res = list(compress(docs, is_matches))

        if len(res) < 1:
            logger.warning(f"Document Not Found!")
        else:
            logger.info(f"Find {len(res)} documents.")

        return res
        
    def _insert(self, word):

        node = self._root
        
        for char in word:
            if char not in node.child:
                node.child[char] = self.TrieNode()
            node = node.child[char]
        node.is_end = True

    def _find(self, doc):
        
        node = self._root
        
        
        for char in doc:
            node = node.child.get(char)
            if not node and char in self._root.child:
                node = self._root.child.get(char)
            elif not node:
                node = self._root
            if node.is_end:
                return True
    


