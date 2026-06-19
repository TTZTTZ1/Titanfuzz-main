
import torch
tensor = torch.tensor([1.0], dtype=torch.float32)
other = torch.tensor([1.1], dtype=torch.float32)
result = tensor.nextafter_(other)
