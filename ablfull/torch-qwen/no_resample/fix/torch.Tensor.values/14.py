import torch
tensor = torch.tensor([[0, 2], [3, 0]], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_tensor(indices=torch.nonzero(tensor), values=tensor[(tensor != 0)].view((- 1)), size=tensor.size())
coalesced_sparse_tensor = sparse_tensor.coalesce()
values = coalesced_sparse_tensor.values()
print(values)