import torch
start = torch.tensor([0.0, 1.0], dtype=torch.float32)
end = torch.tensor([2.0, 3.0], dtype=torch.float32)
weight = 0.5
result = start.lerp_(end, weight)
print(result)