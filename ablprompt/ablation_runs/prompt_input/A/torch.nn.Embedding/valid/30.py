import torch
import torch.nn as nn

# Define an Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input: LongTensor of shape (batch_size, sequence_length)
input_tensor = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])

# Get embeddings for each index in the input tensor
embeddings = embedding(input_tensor)

print(embeddings)