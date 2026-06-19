import torch

input_data = torch.tensor([1.0, -1.0], dtype=torch.float32)
result = torch.atan2(input_data[0], input_data[1])
print(result)