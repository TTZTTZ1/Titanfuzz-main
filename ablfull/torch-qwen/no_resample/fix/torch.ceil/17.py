import torch
input_data = torch.tensor([(- 1.5), 0.3, 2.7], dtype=torch.float)
result = torch.ceil(input_data)
print(result)