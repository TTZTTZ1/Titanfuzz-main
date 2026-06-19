
import torch
tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
other = torch.tensor([1.5, 2.5], dtype=torch.float32)
result = tensor.nextafter_(other)
