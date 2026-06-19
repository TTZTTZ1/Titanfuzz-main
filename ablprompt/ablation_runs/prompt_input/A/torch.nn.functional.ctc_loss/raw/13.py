import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 8, 20, requires_grad=True)  # (time, batch_size, alphabet_size)
targets = torch.tensor([1, 2, 3, 4, 5])  # (batch_size,)
input_lengths = torch.tensor([8] * 5)  # (batch_size,)
target_lengths = torch.tensor([5] * 5)  # (batch_size,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, reduction='mean')

print(loss)