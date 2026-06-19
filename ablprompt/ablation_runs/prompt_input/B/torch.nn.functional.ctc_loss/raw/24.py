import torch
import torch.nn.functional as F

# Example data
log_probs = torch.randn(5, 3, 8, requires_grad=True)  # (T=5, N=3, C=8)
targets = torch.tensor([[1, 2, 3], [4, 5], [6]])  # (N=3, S=[3, 2, 1])
input_lengths = torch.tensor([5, 5, 5])  # (N=3)
target_lengths = torch.tensor([3, 2, 1])  # (N=3)

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(loss)