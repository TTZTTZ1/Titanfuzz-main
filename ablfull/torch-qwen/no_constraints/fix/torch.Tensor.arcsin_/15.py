import torch
input_tensor = torch.tensor([(- 0.5), 0.0, 0.5], dtype=torch.float32)
result = torch.Tensor.arcsin_(input_tensor)