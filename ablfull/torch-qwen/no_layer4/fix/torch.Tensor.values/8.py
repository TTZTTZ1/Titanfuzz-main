import torch
sparse_tensor = torch.sparse_coo_tensor([[0, 1, 1], [2, 0, 2]], [3, 4, 5], size=(2, 3))
coalesced_tensor = sparse_tensor.coalesce()
values = coalesced_tensor.values()