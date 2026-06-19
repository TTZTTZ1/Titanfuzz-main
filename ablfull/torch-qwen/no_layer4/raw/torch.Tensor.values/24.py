import torch

# Create a sparse COO tensor
tensor = torch.sparse_coo_tensor([[0, 1, 1], [2, 0, 2]], [3, 4, 5], size=(2, 3))

# Ensure the tensor is coalesced
tensor = tensor.coalesce()

# Call the API
values = tensor.values()
print(values)