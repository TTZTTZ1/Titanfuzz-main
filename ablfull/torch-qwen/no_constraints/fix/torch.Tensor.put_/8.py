import torch
tensor = torch.tensor([1, 2, 3, 4])
index = torch.tensor([0, 2])
source = torch.tensor([99, 88])
tensor.put_(index, source)
print(tensor)