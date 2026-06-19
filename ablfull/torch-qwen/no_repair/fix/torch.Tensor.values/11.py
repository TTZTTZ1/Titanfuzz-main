
import torch
tensor = torch.sparse_coo_tensor([[0, 1], [1, 0]], [2.0, 3.0], size=(2, 2))
tensor = tensor.coalesce()
values = tensor.values()
