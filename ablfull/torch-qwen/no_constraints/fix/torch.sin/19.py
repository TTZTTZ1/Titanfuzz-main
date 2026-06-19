import torch
input_data = torch.tensor([0.5, (- 0.5), 0.0], dtype=torch.float32)
result = torch.sin(input_data)