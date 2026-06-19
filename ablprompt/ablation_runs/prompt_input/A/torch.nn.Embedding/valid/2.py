import torch
import torch.nn as nn

# Define an embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input: LongTensor of shape (batch_size, sequence_length)
input_tensor = torch.LongTensor([[1, 2, 4], [0, 5, 6]])

# Get embeddings for the input tensor
embedded_output = embedding(input_tensor)

print(embedded_output)