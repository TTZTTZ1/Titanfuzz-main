import torch
import torch.nn as nn

# Create an embedding layer with 5000 words and each word represented by a 128-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5000, embedding_dim=128)

# Example input: batch of 3 sentences, each containing 5 words
input_indices = torch.LongTensor([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Expected shape: (3, 5, 128)