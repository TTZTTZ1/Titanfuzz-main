import torch
import torch.nn as nn

# Define an embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create some indices to look up embeddings for
indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding(indices)

print(embeddings)