import torch

input_tensor = torch.tensor([4., 5.])
other_tensor = torch.tensor([2., 3.])

result = torch.divide(input_tensor, other_tensor)
print(result)