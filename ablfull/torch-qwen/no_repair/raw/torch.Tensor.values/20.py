import torch

# Create a sparse COO tensor
tensor = torch.tensor([[0, 0], [0, 2]], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_tensor(indices=[[0, 1], [1, 1]], values=[1, 2], size=(2, 2))

# Ensure the tensor is coalesced
coalesced_sparse_tensor = sparse_tensor.coalesce()

# Call the API
values = coalesced_sparse_tensor.values()
print(values)