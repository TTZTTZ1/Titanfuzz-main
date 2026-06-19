import torch
import torch.nn as nn

# Create an embedding layer for a vocabulary of 5 words, each represented by a 3-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5, embedding_dim=3)

# Define some input indices
input_indices = torch.LongTensor([1, 0, 4])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings)