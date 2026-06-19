import torch
import torch.nn.functional as F

# Example usage of torch.nn.functional.softmax
input_tensor = torch.tensor([1.0, 2.0, 3.0])
softmax_output = F.softmax(input_tensor, dim=0)
print(softmax_output)