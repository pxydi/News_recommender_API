# Recommender.py

# Libraries
import pandas as pd
import numpy as np
import os,json
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity

def recommender(sample_text, categories, k=10):
    '''
    Finds similar documents for a provided sample_text

    INPUTS:
    - sample_text:  str, sample document
    - k          :  int, number of similar documents to returns
    - categories :  list of str, returns only similar documents from the
                    requested categories

    OUTPUTS:
    - df_similarity: DataFrame, contains k most similar documents
    '''

   # Load cleaned documents
    df = pd.read_csv(os.path.join('data', 'clean_documents.csv'))

    # Load embeddings
    with np.load(os.path.join('data', 'embeddings.npz'),allow_pickle=False) as data:
        X_embed = data['embeddings']

    # Extract embedding for text sample
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    embed_sample = embed([sample_text.strip()])

    # Compute similarity scores
    similarity_scores = cosine_similarity(embed_sample, X_embed)[0]
    # Sort in descending order
    sorted_indexes = np.argsort(similarity_scores)[::-1]

    # Find most similar documents
    df_similarity = pd.concat([df,pd.Series(similarity_scores)],axis=1)
    df_similarity = df_similarity.iloc[sorted_indexes]
    df_similarity.columns = ['id', 'category', 'title', 'similarity_score']

    # Return only similar documents from the requested categories
    if categories != "none":
        categories = list(categories.split(','))
        df_similarity = df_similarity.loc[df_similarity['category'].isin(categories)].sort_values(by = 'similarity_score', ascending=False)


    return df_similarity[0:int(k)].to_dict('records')
