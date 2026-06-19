import torch
import torch.nn as nn

# Create an embedding layer with 5000 words, each represented by a 128-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5000, embedding_dim=128)

# Example input: batch of 3 sentences, each containing 10 words
input_indices = torch.randint(low=0, high=5000, size=(3, 10))

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Should print: torch.Size([3, 10, 128])