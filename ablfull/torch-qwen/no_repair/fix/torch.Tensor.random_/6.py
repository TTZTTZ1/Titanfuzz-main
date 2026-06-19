
import torch
dtype = 'int'
from_val = (- 5)
to_val = 5
tensor = torch.tensor(0, dtype=torch.int)
tensor.random_(from_val, to_val)
print(tensor)
