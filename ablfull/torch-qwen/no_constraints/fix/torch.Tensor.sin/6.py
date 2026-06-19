import torch
input_data = torch.tensor([0.0, 1.5708, 3.1416], dtype=torch.float32)
result = torch.sin(input_data)
print(result)