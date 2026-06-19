import torch
import torch.nn as nn

# Create an embedding layer with 5000 embeddings of size 128
embedding_layer = nn.Embedding(num_embeddings=5000, embedding_dim=128)

# Example input: batch of 3 sequences, each sequence has length 5
input_indices = torch.LongTensor([[1, 2, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16]])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Output should be (3, 5, 128)