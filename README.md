Here’s a rewritten version of your README, polished for clarity and flow, with your name included instead of the original author:

---

# 🎬 Movie Semantic Search Assignment

![Tests](https://github.com/jatingaur18/movie-search-assignment/workflows/Tests/badge.svg)

This repository contains my solution for the **semantic search on movie plots** assignment. The project leverages **SentenceTransformers** to perform meaning-based search on movie descriptions.

---

##  Project Overview

This project implements a **semantic search engine** that retrieves movies based on the meaning of a query rather than simple keyword matching. It uses the **`all-MiniLM-L6-v2`** model from SentenceTransformers to generate embeddings of movie plots, and then applies **cosine similarity** to rank results.

---

##  Features

*  **Semantic Search** – Finds movies by meaning, not just keywords
* **Efficient Embeddings** – Powered by `all-MiniLM-L6-v2`
* **Cosine Similarity** – Ranks results by semantic relevance
* **Simple Interface** – Easy function calls with clean DataFrame outputs

---

## Setup Instructions

### Prerequisites

* Python **3.9+**
* Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/jatingaur18/movie-search-assignment.git
   cd movie-search-assignment
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Jupyter Notebook**

   ```bash
   jupyter notebook movie_search_solution.ipynb
   ```

---

## Usage

### Using the Python Module

```python
from movie_search import search_movies

# Example: search for spy thrillers
results = search_movies("spy thriller in Paris", top_n=5)
print(results)
```

### Using the Jupyter Notebook

Open **`movie_search_solution.ipynb`** and run all cells to see the full implementation with examples.

---

## Testing

Run unit tests to validate functionality:

```bash
python -m unittest tests/test_movie_search.py -v
```

The tests check:

* Correct DataFrame output format
* Proper handling of the `top_n` parameter
* Results sorted by similarity (descending)
* Relevant matches for spy-related queries

---

## Example Output

```
Search Results for: "spy thriller in Paris"

1. The Bourne Identity (Score: 0.7234)
2. Casino Royale (Score: 0.6891)
3. Mission: Impossible (Score: 0.6745)
4. Tinker Tailor Soldier Spy (Score: 0.6234)
5. Spy Game (Score: 0.6012)
```

---

##  File Structure

```
movie-search-assignment/
├── movie_search.py              # Main module
├── movie_search_solution.ipynb  # Jupyter notebook solution
├── movies.csv                   # Dataset
├── requirements.txt             # Dependencies
├── tests/
│   └── test_movie_search.py     # Unit tests
└── README.md                    # Documentation
```

---

##  Implementation Details

### Core Components

1. **Data Loading** – Reads movie dataset from CSV
2. **Model Initialization** – Loads SentenceTransformers model
3. **Embedding Creation** – Converts plots into 384-dimensional embeddings
4. **Search Function** – Uses cosine similarity for ranking

### Key Functions

* `load_data_and_model()` – Initializes dataset + model
* `search_movies(query, top_n=5)` – Returns top matches

---

##  Dependencies

* `sentence-transformers==2.2.2`
* `pandas==2.1.4`
* `scikit-learn==1.3.2`
* `numpy==1.24.4`
* `jupyter==1.0.0`

---

## Assignment Requirements Met

* Uses SentenceTransformers with `all-MiniLM-L6-v2`
* Implements semantic search on movie plots
* Returns DataFrame with `title`, `plot`, and `similarity_score`
* Handles `top_n` parameter correctly
* Includes unit tests
* Provides full Jupyter notebook solution

---

##  Author

**Jatin Gaur**
Roll Number: *221010221* 

Assignment for **AI Systems Development – IIIT Naya Raipur**

 Due Date: August 26, 2025


