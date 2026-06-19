import torch

# Create a sparse COO tensor
tensor = torch.sparse_coo_tensor([[0, 1], [2, 3]], [4.0, 5.0], size=(4, 4))

# Ensure the tensor is coalesced
tensor = tensor.coalesce()

# Call the API
values = tensor.values()