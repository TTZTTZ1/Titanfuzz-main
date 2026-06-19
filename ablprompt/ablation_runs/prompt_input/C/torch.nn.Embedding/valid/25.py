import torch
import torch.nn as nn

# Create an Embedding layer with 5 embeddings of dimension 3
embedding_layer = nn.Embedding(num_embeddings=5, embedding_dim=3)

# Example input tensor of indices
input_tensor = torch.LongTensor([1, 2, 4])

# Get the embeddings for the input indices
output_embeddings = embedding_layer(input_tensor)

print(output_embeddings)