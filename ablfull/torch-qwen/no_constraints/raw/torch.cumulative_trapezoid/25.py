import torch

y = torch.tensor([1.0, 2.0, 4.0, 7.0], dtype=torch.float32)
x = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float32)

result = torch.cumulative_trapezoid(y, x, dx=None, axis=-1, initial=None)
print(result)