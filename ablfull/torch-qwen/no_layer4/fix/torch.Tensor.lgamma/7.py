import torch
input_data = torch.tensor([0.5, 1.0, 2.0])
result = input_data.lgamma()
print(result)