
import torch
dtype = torch.float
from_ = 0
to = 10
result = torch.tensor(0.0, dtype=dtype)
result.random_(from_, to)
print(result)
