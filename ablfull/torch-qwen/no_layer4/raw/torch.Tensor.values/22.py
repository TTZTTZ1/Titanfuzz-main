import torch

# Create a sparse COO tensor
sparse_tensor = torch.sparse_coo_tensor([[0, 1], [1, 0]], [1.0, 2.0], size=(2, 2))

# Ensure the tensor is coalesced
coalesced_tensor = sparse_tensor.coalesce()

# Call the API
values = coalesced_tensor.values()
print(values)