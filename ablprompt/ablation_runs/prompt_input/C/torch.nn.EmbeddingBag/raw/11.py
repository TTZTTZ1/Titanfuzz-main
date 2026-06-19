import torch

# Define the EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum')

# Create input tensor with fixed-length bags
input_fixed_length = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9]], dtype=torch.long)

# Compute the sum of embeddings for each bag
output_fixed_length = embedding_bag(input_fixed_length)
print("Output for fixed-length bags:", output_fixed_length)

# Create input tensor with variable-length bags using offsets
input_variable_length = torch.tensor([1, 2, 4, 5, 4, 3, 2, 9], dtype=torch.long)
offsets_variable_length = torch.tensor([0, 4], dtype=torch.long)

# Compute the sum of embeddings for each variable-length bag
output_variable_length = embedding_bag(input_variable_length, offsets_variable_length)
print("Output for variable-length bags:", output_variable_length)