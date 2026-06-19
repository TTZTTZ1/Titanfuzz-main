import torch
import torch.nn as nn

# Define the embedding layer
embedding_layer = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Create some input data
input_data = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding_layer(input_data)

print(embeddings)