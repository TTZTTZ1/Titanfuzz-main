import torch

# Define the embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input tensor
input_tensor = torch.LongTensor([4, 2, 1])

# Get embeddings for the input
embeddings = embedding(input_tensor)

print(embeddings)