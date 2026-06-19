import torch
input_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
eps_tensor = torch.tensor([1e-05, 1e-05], dtype=torch.float32)
result = input_tensor.nextafter_(eps_tensor)