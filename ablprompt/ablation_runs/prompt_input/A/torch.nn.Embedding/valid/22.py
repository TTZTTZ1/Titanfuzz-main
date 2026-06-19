import torch

# Create an embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Define some indices to look up embeddings for
indices = torch.tensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding(indices)

print(embeddings)