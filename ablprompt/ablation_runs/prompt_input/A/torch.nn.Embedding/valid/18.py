import torch

# Define the embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input: indices of shape (2,)
input_indices = torch.tensor([1, 4])

# Get embeddings for the input indices
embeddings = embedding(input_indices)

print(embeddings)