import torch
import torch.nn.functional as F

# Example usage of cross_entropy from torch.nn.functional
logits = torch.tensor([[2.0, 1.0, 0.1]])
targets = torch.tensor([0])

loss = F.cross_entropy(logits, targets)
print(loss.item())