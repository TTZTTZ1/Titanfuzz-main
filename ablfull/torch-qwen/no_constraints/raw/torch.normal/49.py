import torch

mean = torch.tensor(0.0)
stddev = torch.tensor(1.0)
size = (2, 3)

result = torch.normal(mean, stddev, size)
print(result)