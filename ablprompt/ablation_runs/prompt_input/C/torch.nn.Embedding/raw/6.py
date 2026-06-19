import torch
import torch.nn as nn

# Create an embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input tensor
input_tensor = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding(input_tensor)

print(embeddings)