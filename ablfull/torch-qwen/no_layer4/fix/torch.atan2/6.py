import torch
input_data = torch.tensor([0.5, (- 0.5)], dtype=torch.float32)
other_data = torch.tensor([0.5, 0.5], dtype=torch.float32)
result = torch.atan2(input_data, other_data)
print(result)