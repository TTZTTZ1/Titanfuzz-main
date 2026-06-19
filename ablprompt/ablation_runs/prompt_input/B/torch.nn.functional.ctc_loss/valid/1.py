import torch
import torch.nn.functional as F

# Example log_probs tensor with shape (T, N, C)
log_probs = torch.randn(5, 3, 8, requires_grad=True)

# Example targets tensor with shape (N, S)
targets = torch.tensor([[1, 2], [2, 3], [4, 5]])

# Example input_lengths tensor with shape (N,)
input_lengths = torch.tensor([5, 5, 5])

# Example target_lengths tensor with shape (N,)
target_lengths = torch.tensor([2, 2, 2])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(loss)