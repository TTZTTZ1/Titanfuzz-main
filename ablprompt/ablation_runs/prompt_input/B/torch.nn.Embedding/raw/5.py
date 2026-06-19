import torch
import torch.nn as nn

# Create an embedding layer with 5000 words, each represented by a 100-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5000, embedding_dim=100)

# Example input: batch of 3 sentences, each sentence has 5 tokens
input_indices = torch.LongTensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Should print: torch.Size([3, 5, 100])