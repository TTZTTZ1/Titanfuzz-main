import torch
import torch.nn.functional as F

# Define input tensors for CTC loss calculation
log_probs = torch.randn(5, 8, 20)  # (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3, 4, 5])  # Example target sequence
input_lengths = torch.tensor([5])  # Length of each input sequence
target_lengths = torch.tensor([5])  # Length of each target sequence

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(f"CTC Loss: {loss.item()}")