# Movie Semantic Search Assignment

This repository contains my solution for the semantic search on movie plots assignment using SentenceTransformers.

## Project Overview

This project implements a semantic search engine that can find movies based on plot descriptions using AI embeddings. The system uses the `all-MiniLM-L6-v2` model from SentenceTransformers to create vector representations of movie plots and then finds the most similar movies to a given search query using cosine similarity.

## Features

- **Semantic Search**: Find movies based on meaning, not just keyword matching
- **SentenceTransformers**: Uses the efficient `all-MiniLM-L6-v2` model
- **Cosine Similarity**: Ranks results by semantic similarity scores
- **Easy to Use**: Simple function interface with pandas DataFrame output

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/movie-search-assignment.git
   cd movie-search-assignment
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Jupyter notebook:**
   ```bash
   jupyter notebook movie_search_solution.ipynb
   ```

## Usage

### Using the Python Module

```python
from movie_search import search_movies

# Search for movies
results = search_movies('spy thriller in Paris', top_n=5)
print(results)
```

### Using the Jupyter Notebook

Open `movie_search_solution.ipynb` and run all cells to see the complete implementation and examples.

## Testing

Run the unit tests to verify the implementation:

```bash
python -m unittest tests/test_movie_search.py -v
```

The tests verify:
- ✅ Correct output format (DataFrame with required columns)
- ✅ Proper handling of `top_n` parameter
- ✅ Similarity scores in descending order
- ✅ Relevant results for spy-related queries

## Example Output

```
Search Results for: 'spy thriller in Paris'

1. The Bourne Identity (Score: 0.7234)
2. Casino Royale (Score: 0.6891)
3. Mission: Impossible (Score: 0.6745)
4. Tinker Tailor Soldier Spy (Score: 0.6234)
5. Spy Game (Score: 0.6012)
```

## File Structure

```
movie-search-assignment/
├── movie_search.py              # Main Python module
├── movie_search_solution.ipynb  # Jupyter notebook solution
├── movies.csv                   # Movie dataset
├── requirements.txt             # Python dependencies
├── tests/
│   └── test_movie_search.py     # Unit tests
└── README.md                    # This file
```

## Implementation Details

### Core Components

1. **Data Loading**: Loads movie data from CSV file
2. **Model Initialization**: Uses SentenceTransformers `all-MiniLM-L6-v2` model
3. **Embedding Creation**: Converts movie plots to 384-dimensional vectors
4. **Search Function**: Computes cosine similarity and returns top results

### Key Functions

- `load_data_and_model()`: Initializes the search system
- `search_movies(query, top_n=5)`: Main search function

## Dependencies

- `sentence-transformers==2.2.2`: For creating semantic embeddings
- `pandas==2.1.4`: For data manipulation
- `scikit-learn==1.3.2`: For cosine similarity calculation
- `numpy==1.24.4`: For numerical operations
- `jupyter==1.0.0`: For notebook interface

## Assignment Requirements Met

- ✅ Uses SentenceTransformers with `all-MiniLM-L6-v2` model
- ✅ Implements semantic search on movie plots
- ✅ Returns DataFrame with title, plot, and similarity_score
- ✅ Handles `top_n` parameter correctly
- ✅ Includes comprehensive unit tests
- ✅ Well-documented code with comments
- ✅ Complete Jupyter notebook implementation

## Author

[Your Name Here]  
Assignment for AI Systems Development - IIIT Naya Raipur  
Due: August 26, 2025