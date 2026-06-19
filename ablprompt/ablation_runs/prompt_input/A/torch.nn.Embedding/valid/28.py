import torch

# Define the embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create some input indices
indices = torch.tensor([1, 2, 4, 5])

# Get the embeddings for the given indices
embedded_output = embedding(indices)

print(embedded_output)