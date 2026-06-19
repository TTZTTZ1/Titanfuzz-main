import torch

# Create a sparse COO tensor
tensor = torch.tensor([[0, 0, 0], [0, 0, 3], [4, 0, 0]], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_from(tensor.nonzero(), tensor[tensor != 0])

# Ensure the tensor is coalesced
coalesced_sparse_tensor = sparse_tensor.coalesce()

# Call the API
values = coalesced_sparse_tensor.values()