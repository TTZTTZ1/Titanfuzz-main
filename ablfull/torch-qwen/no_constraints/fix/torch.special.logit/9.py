import torch
input_data = torch.tensor([0.5, 0.75], dtype=torch.float32)
result = torch.special.logit(input_data)
print(result)