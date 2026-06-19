import torch

# Create a sparse COO tensor
tensor = torch.tensor([[0., 1., 0.], [0., 0., 2.]])
sparse_tensor = torch.sparse_coo_tensor(indices=torch.nonzero(tensor), values=tensor[tensor != 0])

# Ensure the tensor is coalesced
coalesced_sparse_tensor = sparse_tensor.coalesce()

# Call the API
values = coalesced_sparse_tensor.values()
print(values)