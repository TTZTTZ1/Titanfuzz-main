import torch
import torch.nn.functional as F

# Example usage of cross_entropy function
logits = torch.tensor([[2.0, 1.0, 0.1]])
labels = torch.tensor([0])

loss = F.cross_entropy(logits, labels)
print(loss.item())