
import torch
dtype = torch.float
from_val = 0
to_val = 5
tensor = torch.tensor(0, dtype=dtype)
tensor.random_(from_val, to_val)
print(tensor)
