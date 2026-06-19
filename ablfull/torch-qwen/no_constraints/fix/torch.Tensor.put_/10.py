import torch
tensor = torch.tensor([1, 2, 3])
index = torch.tensor([0, 2])
source = torch.tensor([9, 8])
tensor.put_(index, source)
print(tensor)