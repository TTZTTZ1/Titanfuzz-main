import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
result = torch.std_mean(x)
print(result)