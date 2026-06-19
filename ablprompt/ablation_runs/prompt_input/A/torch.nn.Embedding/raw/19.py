import torch

# Define the vocabulary size and embedding dimension
vocab_size = 10
embedding_dim = 5

# Create an Embedding layer
embedding = torch.nn.Embedding(vocab_size, embedding_dim)

# Example input: indices of words in the vocabulary
input_indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings for the given indices
embeddings = embedding(input_indices)

print(embeddings)