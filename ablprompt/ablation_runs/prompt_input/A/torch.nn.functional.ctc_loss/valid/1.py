import torch
import torch.nn.functional as F

# Example input tensors for CTC loss calculation
log_probs = torch.randn(5, 10, requires_grad=True)  # (time, batch, alphabet_size)
targets = torch.tensor([1, 2, 3])  # (batch,)
input_lengths = torch.tensor([5])  # (batch,)
target_lengths = torch.tensor([3])  # (batch,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, reduction='sum')

print(f"CTC Loss: {loss.item()}")