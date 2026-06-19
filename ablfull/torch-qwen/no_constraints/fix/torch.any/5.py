import torch
input_data = torch.tensor([False, True, False])
result = torch.any(input_data)
print(result)