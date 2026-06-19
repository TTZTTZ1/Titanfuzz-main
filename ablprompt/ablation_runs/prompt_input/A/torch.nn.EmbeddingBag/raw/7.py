import torch

# Define the embedding bag parameters
num_embeddings = 10
embedding_dim = 3
max_norm = None
norm_type = 2.0
scale_grad_by_freq = False
mode = 'sum'
sparse = False
padding_idx = -1

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm, norm_type, scale_grad_by_freq, mode, sparse, padding_idx)

# Example input tensor (batch of indices)
indices = torch.tensor([[4, 5, 6], [7, 8, 9]])

# Example offsets tensor (start and end positions for each sequence in the batch)
offsets = torch.tensor([0, 3])

# Call the EmbeddingBag layer
output = embedding_bag(indices, offsets)

print(output)