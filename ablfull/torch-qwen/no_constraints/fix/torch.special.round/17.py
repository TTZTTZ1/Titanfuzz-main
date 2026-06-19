import torch
input_data = torch.tensor([(- 1.5), (- 0.4), 0.2, 1.7], dtype=torch.float32)
result = torch.special.round(input_data)
print(result)