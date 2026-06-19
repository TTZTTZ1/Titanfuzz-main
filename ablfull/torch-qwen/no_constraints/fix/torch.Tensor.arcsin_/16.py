import torch
input_data = torch.tensor([0.5], dtype=torch.float32)
output = torch.Tensor.arcsin_(input_data)