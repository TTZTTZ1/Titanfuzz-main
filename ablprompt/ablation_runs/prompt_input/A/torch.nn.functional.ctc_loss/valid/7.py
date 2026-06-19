import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 10, requires_grad=True)  # (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3])  # Target sequence of class indices
input_lengths = torch.tensor([5])  # Lengths of each input sequence
target_lengths = torch.tensor([3])  # Lengths of each target sequence

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(loss)