import torch
import torch.nn.functional as F

# Example tensors
log_probs = torch.randn(5, 3, 8, requires_grad=True)  # (T, N, C)
targets = torch.tensor([[1, 2], [2, 3]], dtype=torch.long)  # (N, S)
input_lengths = torch.tensor([5] * 3, dtype=torch.long)  # (N,)
target_lengths = torch.tensor([2, 2], dtype=torch.long)  # (N,)

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(loss)