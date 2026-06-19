import torch

# Create a sparse COO tensor
tensor = torch.sparse_coo_tensor([[0, 1], [1, 0]], [2.0, 3.0], size=(2, 2))

# Ensure the tensor is coalesced
tensor = tensor.coalesce()

# Call the API
values = tensor.values()
print(values)