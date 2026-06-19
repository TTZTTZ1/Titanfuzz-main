import torch
input_data = torch.tensor([0.5, (- 0.5), 1.0], dtype=torch.float32)
result = input_data.sin()