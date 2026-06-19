import torch

# Create an Embedding layer with 1000 words, each represented by a 50-dimensional vector
embedding_layer = torch.nn.Embedding(num_embeddings=1000, embedding_dim=50)

# Example input: batch of 2 sentences, each containing 5 words
input_indices = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Output should be torch.Size([2, 5, 50])