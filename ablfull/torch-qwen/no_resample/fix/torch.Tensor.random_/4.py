import torch
dtype = torch.float
from_val = 0
to_val = None
result = torch.empty(5, dtype=dtype).random_(from_val, to_val)