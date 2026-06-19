import torch

# Create an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum', sparse=True)

# Define input tensors
input = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
offsets = torch.LongTensor([0, 4])

# Compute the embedding bag
output = embedding_bag(input, offsets)

print(output)