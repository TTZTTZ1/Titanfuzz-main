import torch
input_data = torch.tensor([0.5, (- 0.5)], dtype=torch.float32)
result = torch.atan2(input_data[0], input_data[1])