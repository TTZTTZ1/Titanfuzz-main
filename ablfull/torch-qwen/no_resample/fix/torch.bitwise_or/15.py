import torch
input_tensor = torch.tensor([True, False], dtype=torch.bool)
other_tensor = torch.tensor([False, True], dtype=torch.bool)
result = torch.bitwise_or(input_tensor, other_tensor)
print(result)