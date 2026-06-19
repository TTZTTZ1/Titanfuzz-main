import torch

# Create an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=5, embedding_dim=3, mode='sum', sparse=True)

# Define some input data and offsets
input_data = torch.LongTensor([[1, 2, 4], [4, 3, 2]])
offsets = torch.LongTensor([0, 3])

# Compute the embedding bag
output = embedding_bag(input_data, offsets)

print(output)