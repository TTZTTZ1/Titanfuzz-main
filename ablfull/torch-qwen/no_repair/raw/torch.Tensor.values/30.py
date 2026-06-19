import torch

# Create a sparse COO tensor
sparse_tensor = torch.sparse_coo_tensor(indices=torch.tensor([[0, 1], [2, 3]]), values=torch.tensor([4, 5]), size=(4, 4))

# Ensure the tensor is coalesced
coalesced_tensor = sparse_tensor.coalesce()

# Call the API
values = coalesced_tensor.values()