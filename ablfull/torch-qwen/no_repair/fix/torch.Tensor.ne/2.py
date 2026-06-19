
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0])
other_tensor = torch.tensor([1.0, 2.5, 3.0])
result = input_tensor.ne(other_tensor)
print(result)
