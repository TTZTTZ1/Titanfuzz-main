
import torch
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3.0, 4.0, 5.0])
sparse_tensor = torch.sparse_coo_tensor(indices, values, size=(2, 3))
coalesced_tensor = sparse_tensor.coalesce()
result = coalesced_tensor.values()
