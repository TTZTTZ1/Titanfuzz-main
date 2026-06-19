
import torch
input_data = torch.tensor([(- 1.5), (- 0.5), 0.5, 1.5], dtype=torch.float)
result = torch.ceil(input_data)
print(result)
