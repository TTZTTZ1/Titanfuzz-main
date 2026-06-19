import torch

# Define an embedding layer with 10 tokens and each token having an embedding size of 5
embedding = torch.nn.Embedding(10, 5)

# Create a tensor of indices for which we want to get embeddings
indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings for the given indices
embeddings = embedding(indices)

print(embeddings)