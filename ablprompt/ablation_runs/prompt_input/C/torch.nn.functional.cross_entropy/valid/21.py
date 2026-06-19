import torch
import torch.nn.functional as F

# Example input tensor (logits)
input_tensor = torch.randn(3, 5)

# Example target tensor (class indices)
target_tensor = torch.tensor([1, 0, 4])

# Compute cross-entropy loss
loss = F.cross_entropy(input_tensor, target_tensor, weight=torch.tensor([0.2, 0.3, 0.1, 0.4, 0.1]), ignore_index=0, reduction='mean', label_smoothing=0.1)

print(f"Cross-Entropy Loss: {loss.item()}")