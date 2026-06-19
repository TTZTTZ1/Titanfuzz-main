import torch
tensor = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([4.0, 5.0, 6.0])
weight = 0.5
tensor.lerp_(other, weight)
print(tensor)