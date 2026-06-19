import torch
dtype = torch.float
from_val = 0
to_val = 1
tensor = torch.tensor(0.5, dtype=dtype)
tensor.random_(from_val, to_val)