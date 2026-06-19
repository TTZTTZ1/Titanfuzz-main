import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 8, 20)  # (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3, 4, 5])  # Target sequence without padding
input_lengths = torch.tensor([5] * 8)  # Lengths of input sequences
target_lengths = torch.tensor([5] * 8)  # Lengths of target sequences

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(f"CTC Loss: {loss.item()}")