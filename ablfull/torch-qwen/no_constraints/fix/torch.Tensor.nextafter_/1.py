import torch
x = torch.tensor(1.0)
y = torch.tensor(2.0)
result = x.nextafter_(y)
print(result)