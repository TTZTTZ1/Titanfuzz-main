import torch
input_tensor = torch.tensor([0.5])
result = torch.special.logit(input_tensor)
print(result)