import torch

input_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
eps = 1e-5
result = input_tensor.nextafter(eps)