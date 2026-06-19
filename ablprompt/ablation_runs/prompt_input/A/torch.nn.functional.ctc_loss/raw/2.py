import torch
import torch.nn.functional as F

# Define some example inputs for CTC loss
log_probs = torch.randn(5, 8, 20)  # (time, batch, alphabet_size)
targets = torch.tensor([1, 2, 3, 4, 5])  # Example target sequence
input_lengths = torch.tensor([8] * 5)  # Lengths of each input sequence
target_lengths = torch.tensor([5] * 5)  # Lengths of each target sequence

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(f"CTC Loss: {loss.item()}")