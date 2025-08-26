import unittest
import pandas as pd
import numpy as np
from movie_search import search_movies

class TestMovieSearch(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # This will be called before each test
        pass
    
    def test_output_format(self):
        """Test that search_movies returns a DataFrame with correct columns."""
        result = search_movies('spy thriller', top_n=5)
        
        # Check if result is a DataFrame
        self.assertIsInstance(result, pd.DataFrame, "Result should be a pandas DataFrame")
        
        # Check if DataFrame has the required columns
        expected_columns = ['title', 'plot', 'similarity_score']
        self.assertListEqual(list(result.columns), expected_columns, 
                           f"DataFrame should have columns: {expected_columns}")
    
    def test_top_n_parameter(self):
        """Test that the function returns the correct number of results."""
        top_n = 3
        result = search_movies('spy thriller', top_n=top_n)
        
        # Check if the number of returned movies matches top_n
        self.assertEqual(len(result), top_n, 
                        f"Function should return exactly {top_n} movies")
    
    def test_similarity_scores(self):
        """Test that similarity scores are in descending order."""
        result = search_movies('spy thriller', top_n=5)
        
        # Check if similarity scores are in descending order
        similarity_scores = result['similarity_score'].values
        self.assertTrue(all(similarity_scores[i] >= similarity_scores[i+1] 
                           for i in range(len(similarity_scores)-1)),
                       "Similarity scores should be in descending order")
        
        # Check if similarity scores are between 0 and 1
        self.assertTrue(all(0 <= score <= 1 for score in similarity_scores),
                       "Similarity scores should be between 0 and 1")
    
    def test_query_relevance(self):
        """Test that the function returns relevant results for a specific query."""
        result = search_movies('spy thriller in Paris', top_n=5)
        
        # Check if any of the top results contain spy-related keywords
        top_titles = result['title'].str.lower().tolist()
        top_plots = result['plot'].str.lower().tolist()
        
        # Look for spy-related terms in titles or plots
        spy_terms = ['spy', 'agent', 'cia', 'mission', 'secret', 'undercover', 'intelligence']
        
        found_relevant = False
        for title, plot in zip(top_titles, top_plots):
            if any(term in title or term in plot for term in spy_terms):
                found_relevant = True
                break
        
        self.assertTrue(found_relevant, 
                       "At least one of the top results should contain spy-related terms")

if __name__ == '__main__':
    unittest.main()