import torch
import torch.nn.functional as F

# Example usage of torch.nn.functional.softmax
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output_tensor = F.softmax(input_tensor, dim=1)
print(output_tensor)