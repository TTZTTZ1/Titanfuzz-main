import torch
tensor = torch.tensor([[0.0, 0.0, 3.0], [4.0, 0.0, 0.0]], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_tensor(torch.nonzero(tensor), tensor[(tensor != 0)], size=tensor.size())
coalesced_sparse_tensor = sparse_tensor.coalesce()
values = coalesced_sparse_tensor.values()