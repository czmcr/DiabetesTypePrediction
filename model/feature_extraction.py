from data_preprocessing import preprocess_input
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(preprocessed_texts):
    """Fit and transform the preprocessed text data into TF-IDF features."""
    # Initialize a TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the preprocessed texts and transform the texts into TF-IDF features
    tfidf_features = tfidf_vectorizer.fit_transform(preprocessed_texts)

    return tfidf_features

# Example usage for a single piece of text
# This function now expects a list of texts, where each text is preprocessed.
# If you have just one piece of text, wrap it in a list before calling this function.
preprocessed_texts = [preprocess_input("Your preprocessed input text here")]
tfidf_features = extract_features(preprocessed_texts)
