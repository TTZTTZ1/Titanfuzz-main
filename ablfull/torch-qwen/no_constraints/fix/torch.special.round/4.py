import torch
input_data = torch.tensor([(- 1.5), (- 0.4), 0.2, 0.6, 1.8], dtype=torch.float32)
result = torch.special.round(input_data)
print(result)