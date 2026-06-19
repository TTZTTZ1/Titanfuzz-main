import torch
dtype = torch.int
from_val = 0
to_val = 5
result = torch.tensor(0, dtype=dtype)
result.random_(from_val, to_val)
print(result)