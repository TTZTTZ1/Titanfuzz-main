import torch
dtype = 'float'
from_val = 0
to_val = 5
generator = None
tensor = torch.tensor(0, dtype=torch.float)
tensor.random_(from_val, to_val, generator=generator)