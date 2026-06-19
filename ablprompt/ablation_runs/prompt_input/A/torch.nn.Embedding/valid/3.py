import torch

# Define the vocabulary size and embedding dimension
vocab_size = 10
embedding_dim = 5

# Create an instance of Embedding
embedding = torch.nn.Embedding(vocab_size, embedding_dim)

# Example input: tensor of indices
indices = torch.tensor([1, 2, 4, 5])

# Get embeddings for the given indices
embeddings = embedding(indices)

print(embeddings)