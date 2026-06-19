import torch
tensor = torch.sparse_coo_tensor([[0, 1], [2, 3]], [4.0, 5.0], size=(4, 4))
tensor = tensor.coalesce()
values = tensor.values()