import torch
dtype = torch.float
from_val = 0
to_val = 5
shape = (3, 3)
result = torch.empty(shape, dtype=dtype).random_(from_val, to_val)