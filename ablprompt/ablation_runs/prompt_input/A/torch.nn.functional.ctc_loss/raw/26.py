import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 10, requires_grad=True)  # (time, batch, alphabet)
targets = torch.tensor([1, 2, 3, 4])  # (batch,)
input_lengths = torch.tensor([5])  # (batch,)
target_lengths = torch.tensor([4])  # (batch,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, reduction='sum')
print(loss.item())