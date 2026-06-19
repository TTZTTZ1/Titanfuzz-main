import torch
import torch.nn as nn

# Create an Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Prepare input indices
indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding(indices)

print(embeddings)