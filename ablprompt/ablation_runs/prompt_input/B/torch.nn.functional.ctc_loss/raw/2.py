import torch
from torch.nn.functional import ctc_loss

# Example tensors
log_probs = torch.randn(5, 3, 8, requires_grad=True)  # (T, N, C)
targets = torch.tensor([1, 2, 3], dtype=torch.long).unsqueeze(0)  # (N, S)
input_lengths = torch.tensor([5])  # (N,)
target_lengths = torch.tensor([3])  # (N,)

# Compute CTC loss
loss = ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(loss)