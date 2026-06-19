import torch
from torch.nn import functional as F

# Example tensors
log_probs = torch.randn(5, 3, 8, requires_grad=True)  # (T, N, C)
targets = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.long)  # (N, S)
input_lengths = torch.tensor([5, 5])  # (N,)
target_lengths = torch.tensor([3, 3])  # (N,)

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(loss)