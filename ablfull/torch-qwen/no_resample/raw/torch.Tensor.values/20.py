import torch

# Create a sparse COO tensor
tensor = torch.tensor([[0., 0., 0.], [0., 5., 0.]], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_tensor(indices=torch.nonzero(tensor), values=tensor[tensor != 0].view(-1))

# Ensure it is coalesced
coalesced_sparse_tensor = sparse_tensor.coalesce()

# Call the API
values = coalesced_sparse_tensor.values()