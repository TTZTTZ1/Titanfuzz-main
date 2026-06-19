import torch

input_tensor = torch.tensor([4.0, 8.0, 15.0])
other_tensor = torch.tensor([2.0, 4.0, 8.0])

result = torch.divide(input_tensor, other_tensor)
print(result)