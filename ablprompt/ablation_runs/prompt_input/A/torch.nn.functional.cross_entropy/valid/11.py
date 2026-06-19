import torch
import torch.nn.functional as F

# Example usage of cross_entropy
input = torch.randn(3, 5, requires_grad=True)
target = torch.tensor([1, 0, 4])
output = F.cross_entropy(input, target)
print(output)