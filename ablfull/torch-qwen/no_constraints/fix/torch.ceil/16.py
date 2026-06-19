import torch
input_data = torch.tensor([(- 1.5), (- 0.1), 0.0, 0.9, 1.1])
result = torch.ceil(input_data)
print(result)