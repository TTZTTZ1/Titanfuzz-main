
import torch
input_tensor = torch.tensor([1, 2, 3])
output = torch.atleast_1d(input_tensor)
print(output)
