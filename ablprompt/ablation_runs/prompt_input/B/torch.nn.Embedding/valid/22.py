import torch
import torch.nn as nn

# Create an embedding layer with 500 words, each represented by a 300-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=500, embedding_dim=300)

# Example input: batch of 4 sentences, each containing 7 words
input_indices = torch.LongTensor([[10, 20, 30, 40, 50, 60, 70],
                                  [80, 90, 100, 110, 120, 130, 140],
                                  [150, 160, 170, 180, 190, 200, 210],
                                  [220, 230, 240, 250, 260, 270, 280]])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Should be (4, 7, 300)