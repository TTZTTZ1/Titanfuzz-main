import torch

# Create an embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input: tensor of indices
input_indices = torch.LongTensor([4, 2, 9])

# Get embeddings for the given indices
embeddings = embedding(input_indices)

print(embeddings)