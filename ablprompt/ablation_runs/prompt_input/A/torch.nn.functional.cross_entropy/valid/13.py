import torch
import torch.nn.functional as F

# Example usage of torch.nn.functional.cross_entropy
logits = torch.tensor([[2.0, 1.0, 0.1]])
labels = torch.tensor([0])

loss = F.cross_entropy(logits, labels)
print(f"Cross-Entropy Loss: {loss.item()}")