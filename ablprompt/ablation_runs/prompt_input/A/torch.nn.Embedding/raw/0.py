import torch

# Define the embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create an input tensor of indices
input_indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings for the given indices
embeddings = embedding(input_indices)

print(embeddings)