import torch

# Define parameters for the embedding layer
embedding_dim = 10
vocab_size = 5

# Create an instance of the Embedding layer
embedding_layer = torch.nn.Embedding(vocab_size, embedding_dim)

# Example input: indices of tokens in the vocabulary
input_indices = torch.LongTensor([0, 4, 2])

# Get embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings)