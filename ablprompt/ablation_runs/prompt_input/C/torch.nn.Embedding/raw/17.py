import torch
import torch.nn as nn

# Create an embedding layer with 1000 words and each word represented by a 50-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=1000, embedding_dim=50)

# Example input: batch of 3 sentences with variable lengths
input_indices = torch.tensor([[1, 2, 3], [4, 5], [6]])

# Get the embeddings for the given input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Output should be (3, 3, 50)