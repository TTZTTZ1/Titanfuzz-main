
import torch
dtype = torch.float
from_val = 0
to_val = 1
result = torch.tensor([from_val], dtype=dtype).random_(from_val, to_val)
print(result)
