import torch
import torch.nn as nn

# Create an Embedding layer with 10 embeddings of size 3
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input: a batch of two sequences, each sequence has two tokens
input_indices = torch.LongTensor([[1, 2], [3, 4]])

# Get the embeddings for the input indices
output_embeddings = embedding(input_indices)

print(output_embeddings)