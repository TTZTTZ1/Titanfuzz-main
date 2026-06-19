import torch
import torch.nn.functional as F

# Example tensor
input_tensor = torch.tensor([[1.0, 2.0, 3.0]])

# Applying log_softmax
log_softmax_output = F.log_softmax(input_tensor, dim=1)

print(log_softmax_output)