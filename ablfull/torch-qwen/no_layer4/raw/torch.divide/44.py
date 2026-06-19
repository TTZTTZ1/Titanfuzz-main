import torch

input_data = torch.tensor([4.0])
other_data = torch.tensor([2.0])
result = torch.divide(input_data, other_data)
print(result)