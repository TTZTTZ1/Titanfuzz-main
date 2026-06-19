import torch
import torch.nn.functional as F

# Example inputs for CTC loss calculation
log_probs = torch.randn(5, 80, 26)  # (time, batch, output_dim)
targets = torch.tensor([1, 2, 3, 4, 5])  # (batch,)
input_lengths = torch.tensor([5] * 1)  # (batch,)
target_lengths = torch.tensor([5] * 1)  # (batch,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0)

print(f"CTC Loss: {loss.item()}")