import torch

input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
other_tensor = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)
result = torch.add(input_tensor, other_tensor)
print(result)