import torch

# Create a sparse COO tensor
tensor = torch.sparse_coo_tensor(indices=torch.tensor([[0, 1], [2, 3]]), values=torch.tensor([4.0, 5.0]), size=(4, 4))

# Ensure it is coalesced
tensor = tensor.coalesce()

# Call the API
values = tensor.values()
print(values)