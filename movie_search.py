"""
Movie Semantic Search Module

This module provides functionality to search for movies based on plot descriptions
using semantic similarity with SentenceTransformers.
"""

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Global variables to store the model and embeddings
model = None
movie_embeddings = None
movies_df = None

def load_data_and_model():
    """
    Load the movie data and initialize the SentenceTransformer model.
    This function should be called once to set up the search system.
    """
    global model, movie_embeddings, movies_df
    
    # Load the movie dataset
    movies_df = pd.read_csv('movies.csv')
    
    # Initialize the SentenceTransformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Create embeddings for all movie plots
    movie_plots = movies_df['plot'].tolist()
    movie_embeddings = model.encode(movie_plots)
    
    print(f"Loaded {len(movies_df)} movies and created embeddings.")

def search_movies(query, top_n=5):
    """
    Search for movies based on a text query using semantic similarity.
    
    Args:
        query (str): The search query describing the type of movie desired
        top_n (int): Number of top results to return (default: 5)
    
    Returns:
        pandas.DataFrame: DataFrame containing top_n movies with columns:
                         - title: Movie title
                         - plot: Movie plot description  
                         - similarity_score: Cosine similarity score (0-1)
    """
    global model, movie_embeddings, movies_df
    
    if model is None:
        load_data_and_model()
    
    # Encode the search query
    query_embedding = model.encode([query])
    
    # Calculate cosine similarity between query and all movie plots
    similarities = cosine_similarity(query_embedding, movie_embeddings)[0]
    
    # Get indices of top_n most similar movies
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    # Create result DataFrame
    result_df = movies_df.iloc[top_indices].copy()
    result_df['similarity_score'] = similarities[top_indices]
    
    # Reset index for clean output
    result_df = result_df.reset_index(drop=True)
    
    return result_df[['title', 'plot', 'similarity_score']]

if __name__ == "__main__":
    # Example usage
    load_data_and_model()
    
    # Test the search function
    results = search_movies('spy thriller in Paris', top_n=5)
    print("Search Results for 'spy thriller in Paris':")
    print(results)