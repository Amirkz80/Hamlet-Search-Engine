import unittest
from ranking.ranking_functions import ranker

class TestRanker(unittest.TestCase):
    """A class to test ranker function"""

    def setUp(self) -> None:
        self.query = ['hamlet', 'likes', 'france']
        # The correct list that contains doc ids and
        # Is sorted by each doc id TF score, for this query
        # (CONSIDERING CURRENT Index Table DATABASE!)
        # is as follows :
        # [6, 1, 8, 10, 5, 11, 7, 3]
        # scores of each doc descends in the list 

    def test_ranker_function(self):
        self.assertEqual(ranker(self.query), [6, 1, 8, 10, 5, 11, 7, 3])

if __name__=='__main__':
    
    unittest.main()