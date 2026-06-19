
import torch
dtype = torch.float
from_val = 0
to_val = 5
tensor = torch.Tensor(3)
tensor.random_(from_val, to_val)
print(tensor)
