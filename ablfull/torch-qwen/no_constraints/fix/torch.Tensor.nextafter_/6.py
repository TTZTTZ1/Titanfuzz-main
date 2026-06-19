import torch
a = torch.tensor(0.5)
b = torch.tensor(1.0)
result = torch.Tensor.nextafter_(a, b)
print(result)