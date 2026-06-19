import torch

input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
other_tensor = torch.tensor([[5.0, 6.0], [7.0, 8.0]], dtype=torch.float32)

result = torch.atan2(input_tensor, other_tensor)
print(result)