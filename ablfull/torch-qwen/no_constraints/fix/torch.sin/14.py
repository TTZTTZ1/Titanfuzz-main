import torch
input_data = torch.tensor([(- 0.5), 0.0, 0.5])
result = torch.sin(input_data)
print(result)