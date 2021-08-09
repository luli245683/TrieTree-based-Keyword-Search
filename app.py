from libs.SearchModule import TrieTreeSearch

tree = TrieTreeSearch()
keys = ['a','b','c','d','e','f'] * 5000
docs = ['e','f','g','h','i'] * 5000
# tree.fit(keys)
res = tree.transform(docs)


