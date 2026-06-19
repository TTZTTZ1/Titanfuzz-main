import torch

# Generate sparse COO tensor
indices = torch.tensor([[0, 1], [2, 3]])
values = torch.tensor([4.0, 5.0])
sparse_tensor = torch.sparse_coo_tensor(indices, values, size=(4, 4))

# Ensure the tensor is coalesced
coalesced_tensor = sparse_tensor.coalesce()

# Call the API
result = coalesced_tensor.values()
print(result)