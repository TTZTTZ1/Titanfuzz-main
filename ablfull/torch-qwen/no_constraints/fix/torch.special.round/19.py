import torch
input_data = torch.tensor([1.5, (- 0.7), 2.3, (- 1.9)], dtype=torch.float32)
result = torch.special.round(input_data)
print(result)