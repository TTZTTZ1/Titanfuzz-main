import torch
import torch.nn.functional as F

# Example inputs for CTC Loss
log_probs = torch.randn(5, 8, 20)  # (time, batch, alphabet_size)
targets = torch.tensor([1, 2, 3, 4, 5])  # (batch,)
input_lengths = torch.full((8,), 5)  # Lengths of each input sequence
target_lengths = torch.tensor([5])  # Lengths of each target sequence

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(loss)