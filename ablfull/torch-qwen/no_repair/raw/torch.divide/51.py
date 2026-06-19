import torch

input_data = torch.tensor([4.0, 8.0, 12.0])
other_data = torch.tensor([2.0, 4.0, 6.0])

result = torch.divide(input_data, other_data)
print(result)