import torch
import torch.nn.functional as F

# Example inputs for CTC loss calculation
log_probs = torch.randn(5, 8, 20)  # (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3])  # Targets without padding
input_lengths = torch.tensor([8])  # Lengths of input sequences
target_lengths = torch.tensor([3])  # Lengths of target sequences

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(loss)