import torch
x = torch.tensor(0.0)
y = torch.tensor(0.1)
result = torch.Tensor.nextafter_(x, y)
print(result)