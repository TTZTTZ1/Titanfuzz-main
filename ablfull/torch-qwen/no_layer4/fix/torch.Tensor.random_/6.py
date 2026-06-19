import torch
dtype = torch.float
from_val = 0
to_val = 1
tensor = torch.zeros(5)
tensor.random_(from_val, to_val)
print(tensor)