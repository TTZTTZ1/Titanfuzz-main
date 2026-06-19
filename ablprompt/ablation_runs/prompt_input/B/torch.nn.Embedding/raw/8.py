import torch
import torch.nn as nn

# Create an embedding layer
embedding = nn.Embedding(num_embeddings=100, embedding_dim=50)

# Example input indices
input_indices = torch.LongTensor([10, 20, 30])

# Get the embeddings
embeddings = embedding(input_indices)

print(embeddings.shape)  # Should be (3, 50)