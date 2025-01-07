import numpy as np
from sentence_transformers import SentenceTransformer

# Load pre-trained model for sentence embeddings (STSB Roberta model)
model = SentenceTransformer("stsb-roberta-large")


def process_chunks(chunks):
    """
    Converts the provided chunks of text into embeddings.

    Parameters:
    - chunks: list of str, text chunks to embed

    Returns:
    - numpy array: embeddings for the chunks
    """
    embeddings = []

    # Convert each chunk into a vector embedding
    for chunk in chunks:
        chunk_embedding = model.encode([chunk], convert_to_numpy=True)[0]
        embeddings.append(chunk_embedding)

    # Convert list of embeddings into a NumPy array for consistent dimensionality
    return np.array(embeddings)


def process_query(query, boost_factor=1.5):
    """
    Converts the user query into an embedding, boosting the embeddings for words
    that match the keywords from headings.

    Parameters:
    - query: str, user query
    - boost_factor: float, factor by which to boost the embeddings of heading keywords

    Returns:
    - numpy array: boosted embedding for the query
    """
    query_embedding = model.encode([query], convert_to_numpy=True)[0]

    # Optionally boost certain words' embeddings if they match heading keywords (if heading keywords are stored)
    # This would be customized based on heading_keywords, if provided in another part of the application
    # For now, we just use the plain query embedding without boosts.

    query_embedding = np.reshape(
        query_embedding, (1, -1)
    )  # Ensure the query is in the right shape for matching

    return query_embedding
