import torch
import torch.nn as nn

# Create an embedding layer
embedding = nn.Embedding(num_embeddings=1000, embedding_dim=50)

# Create input indices
input_indices = torch.LongTensor([123, 456, 789])

# Get the embeddings
embeddings = embedding(input_indices)

print(embeddings.shape)  # Output should be (3, 50)