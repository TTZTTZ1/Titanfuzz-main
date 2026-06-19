import torch
input_data = torch.tensor([(- 0.5), 0.0, 0.5])
result = input_data.arcsin_()
print(result)