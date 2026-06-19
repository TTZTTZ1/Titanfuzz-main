import torch
import torch.nn.functional as F

# Example input tensor
input_tensor = torch.tensor([[1.0, 2.0, 3.0]])

# Call log_softmax function
output_tensor = F.log_softmax(input_tensor, dim=1)

print(output_tensor)