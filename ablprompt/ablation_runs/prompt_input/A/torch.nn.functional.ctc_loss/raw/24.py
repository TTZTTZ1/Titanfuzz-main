import torch
import torch.nn.functional as F

# Example input tensors for CTC loss
log_probs = torch.randn(5, 8, 20)  # (time, batch, alphabet_size)
targets = torch.tensor([1, 2, 3, 4, 5])  # (batch,)
input_lengths = torch.tensor([8] * 5)  # (batch,)
target_lengths = torch.tensor([5] * 5)  # (batch,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0)

print(f"CTC Loss: {loss.item()}")