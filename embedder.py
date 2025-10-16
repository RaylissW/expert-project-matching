from sentence_transformers import SentenceTransformer

def get_embeddings(df, column='processed_text', model_name='distiluse-base-multilingual-cased-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(df[column].tolist(), batch_size=32)
    return embeddings