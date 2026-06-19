import torch
import torch.nn as nn

# Create an Embedding layer with 5 words and each word represented by a 3-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5, embedding_dim=3)

# Example input: a batch of 2 sentences, each containing 3 words
input_indices = torch.tensor([[0, 1, 2], [3, 4, 0]])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings)