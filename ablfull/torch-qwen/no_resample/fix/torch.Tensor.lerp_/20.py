import torch
tensor = torch.tensor([1.0, 2.0, 3.0])
end = torch.tensor([4.0, 5.0, 6.0])
weight = 0.5
result = tensor.lerp_(end, weight)