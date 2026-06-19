
import torch
torch.set_grad_enabled(False)
result = torch.is_grad_enabled()
print(result)
