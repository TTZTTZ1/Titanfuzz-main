import torch
tensor = torch.tensor([1.0, 2.0, 3.0])
end_tensor = torch.tensor([4.0, 5.0, 6.0])
weight = 0.5
tensor.lerp_(end_tensor, weight)
print(tensor)