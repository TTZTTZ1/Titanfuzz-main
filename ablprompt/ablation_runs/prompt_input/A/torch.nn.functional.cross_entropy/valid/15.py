import torch
import torch.nn.functional as F

# Example usage of cross_entropy
logits = torch.tensor([[2.0, 1.0, 0.1], [0.5, 2.0, 0.3]])
labels = torch.tensor([0, 1])

loss = F.cross_entropy(logits, labels)
print(loss.item())