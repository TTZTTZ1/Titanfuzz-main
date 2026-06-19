import torch

# Create an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3)

# Example input: indices of embeddings to use
indices = torch.tensor([1, 2, 4, 5])

# Example offsets: where each bag starts in the indices list
offsets = torch.tensor([0, 2])

# Get the embedded bag
embedded_bag = embedding_bag(indices, offsets)

print(embedded_bag)