import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def find_most_similar_chunks(query_embedding, chunk_embeddings, top_n=4):
    """
    Finds the top N most similar chunks based on cosine similarity between query and chunk embeddings.

    Parameters:
    - query_embedding: numpy array, shape (1, embedding_dim) - The embedding of the query
    - chunk_embeddings: numpy array, shape (num_chunks, embedding_dim) - Embeddings of the text chunks
    - top_n: int, number of most similar chunks to return (default is 4)

    Returns:
    - List of tuples: (index, similarity_score) for the top N similar chunks
    """
    if chunk_embeddings.shape[0] == 0:
        return []  # Handle edge case where there are no chunk embeddings

    # Calculate cosine similarity between the query embedding and chunk embeddings
    similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]

    # Get the top N most similar chunks (sorting in descending order)
    top_indices = np.argsort(similarities)[-top_n:][::-1]

    # Return the top N most similar chunks with their corresponding similarity scores
    return [(int(idx), float(similarities[idx])) for idx in top_indices]
