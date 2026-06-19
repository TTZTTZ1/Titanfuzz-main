import torch
import torch.nn as nn

# Create an embedding layer with 5000 words and each word represented by a 128-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5000, embedding_dim=128)

# Example input: batch of 3 sentences, each sentence has 7 words
input_indices = torch.LongTensor([[1, 2, 3, 4, 5, 6, 7], 
                                  [8, 9, 10, 11, 12, 13, 14], 
                                  [15, 16, 17, 18, 19, 20, 21]])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings.shape)  # Expected shape: (3, 7, 128)