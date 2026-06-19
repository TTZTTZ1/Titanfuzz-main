import torch
input_tensor = torch.tensor([(- 1.7), (- 0.5), 0.3, 1.9])
result = torch.ceil(input_tensor)
print(result)