import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0], dtype=torch.float32)
result = torch.std_mean(x)
print(result)