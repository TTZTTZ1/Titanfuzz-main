import torch

# Create an embedding layer with 5 embeddings of size 3
embedding = torch.nn.Embedding(num_embeddings=5, embedding_dim=3)

# Define input indices
input_indices = torch.LongTensor([0, 1, 2, 3, 4])

# Get the embeddings for the given indices
output_embeddings = embedding(input_indices)

print(output_embeddings)