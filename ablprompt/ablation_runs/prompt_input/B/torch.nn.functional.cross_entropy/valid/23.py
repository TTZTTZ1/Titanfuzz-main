import torch
import torch.nn.functional as F

# Create random logits and target tensors
logits = torch.randn(3, 5)
target_indices = torch.randint(0, 5, (3,))
target_probs = torch.softmax(logits, dim=1)

# Calculate cross-entropy loss using different methods
loss1 = F.cross_entropy(logits, target_indices)
loss2 = F.cross_entropy(target_probs, target_indices, reduction='none')
loss3 = F.cross_entropy(logits, target_indices, weight=torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5]), ignore_index=4)

print("Loss 1:", loss1.item())
print("Loss 2:", loss2.tolist())
print("Loss 3:", loss3.item())