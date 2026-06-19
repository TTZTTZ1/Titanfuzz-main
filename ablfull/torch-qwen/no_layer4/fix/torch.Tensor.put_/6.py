import torch
index = torch.tensor([0, 1, 2])
source = torch.tensor([3, 4, 5])
result_tensor = torch.tensor([0, 0, 0])
result_tensor.put_(index, source)
print(result_tensor)