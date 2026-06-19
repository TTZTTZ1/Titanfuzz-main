
import torch
tensor = torch.tensor([[0, 1], [2, 0]])
result = tensor.nonzero(as_tuple=True)
