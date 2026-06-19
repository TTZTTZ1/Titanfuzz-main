import torch
x = torch.tensor(1.0)
y = torch.tensor(2.0)
result = torch.Tensor.nextafter_(x, y)
print(result)