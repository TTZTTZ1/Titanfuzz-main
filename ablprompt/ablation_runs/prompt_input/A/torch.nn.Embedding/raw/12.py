import torch

# Define the embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create some input indices
indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings for the indices
embeddings = embedding(indices)

print(embeddings)