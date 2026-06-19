
import torch
index = torch.tensor([0, 1, 2])
source = torch.tensor([10, 20, 30])
result_tensor = torch.tensor([5, 5, 5])
result_tensor.put_(index, source)
print(result_tensor)
