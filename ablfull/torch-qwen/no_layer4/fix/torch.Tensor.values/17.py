import torch
sparse_tensor = torch.sparse_coo_tensor([[0, 1], [1, 0]], [1.0, 2.0], size=(2, 2))
coalesced_tensor = sparse_tensor.coalesce()
values = coalesced_tensor.values()
print(values)