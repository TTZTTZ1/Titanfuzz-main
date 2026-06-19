import torch
import torch.nn.functional as F

# Example input tensors
input = torch.randn(3, 5, requires_grad=True)
target = torch.tensor([1, 0, 4])

# Call to cross_entropy
loss = F.cross_entropy(input, target)

print(loss)