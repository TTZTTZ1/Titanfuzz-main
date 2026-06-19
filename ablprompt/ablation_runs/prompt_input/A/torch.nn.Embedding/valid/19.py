import torch

# Define the embedding layer
embedding = torch.nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create an input tensor
input_tensor = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding(input_tensor)

print(embeddings)