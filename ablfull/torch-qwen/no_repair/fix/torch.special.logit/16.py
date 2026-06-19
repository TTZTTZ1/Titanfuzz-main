
import torch
input_tensor = torch.tensor([(- 1.0), 0.0, 1.0])
result = torch.special.logit(input_tensor)
print(result)
