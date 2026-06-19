import torch
input_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
other_tensor = torch.tensor([1.0, 3.0], dtype=torch.float32)
result = torch.atan2(input_tensor, other_tensor)
print(result)