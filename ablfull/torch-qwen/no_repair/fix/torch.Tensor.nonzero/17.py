
import torch
tensor = torch.tensor([[0, 1], [2, 0]], dtype=torch.int)
result = tensor.nonzero(as_tuple=True)
