
import torch
input_data = torch.tensor([(- 1.7), (- 0.5), 0.2, 1.8], dtype=torch.float)
result = torch.ceil(input_data)
print(result)
