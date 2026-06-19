import torch

input_tensor = torch.tensor([1.0], dtype=torch.float32)
eps = torch.tensor(1e-5, dtype=torch.float32)

result = torch.nextafter(input_tensor, eps)