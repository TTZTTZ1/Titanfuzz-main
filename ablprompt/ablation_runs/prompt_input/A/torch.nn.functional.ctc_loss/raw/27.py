import torch
import torch.nn.functional as F

# Example inputs for CTC loss calculation
log_probs = torch.randn(5, 8, requires_grad=True)  # (time, batch, num_classes)
targets = torch.tensor([1, 2, 3, 4])  # Targets without padding
input_lengths = torch.tensor([8])  # Lengths of each input sequence
target_lengths = torch.tensor([4])  # Lengths of each target sequence

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(loss)