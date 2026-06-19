import torch
import torch.nn as nn

# Create an embedding layer with 5000 tokens and each token having an embedding dimension of 128
embedding_layer = nn.Embedding(num_embeddings=5000, embedding_dim=128)

# Example input: batch of 3 sentences, each containing 10 words (tokens)
input_indices = torch.randint(0, 5000, (3, 10))

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Should be (3, 10, 128)