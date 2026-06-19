import torch
input_tensor = torch.tensor([4.0, 5.0], dtype=torch.float32)
other_tensor = torch.tensor([2.0, 2.0], dtype=torch.float32)
result = torch.divide(input_tensor, other_tensor)
print(result)