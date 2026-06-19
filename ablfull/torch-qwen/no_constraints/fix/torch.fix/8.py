import torch
input_data = torch.tensor([(- 1.5), 0.5, 2.5], dtype=torch.float32)
result = torch.fix(input_data)
print(result)