import torch
import torch.nn as nn

# Create an Embedding layer with 5000 words and each word represented by a 128-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5000, embedding_dim=128)

# Example input: batch of 3 sentences with varying lengths
sentences = torch.tensor([
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
])

# Get the embeddings for the input sentences
embeddings = embedding_layer(sentences)

print(embeddings.shape)  # Should print: torch.Size([3, 4, 128])