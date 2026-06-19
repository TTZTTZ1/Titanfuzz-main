import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 80, 26)  # (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3, 4, 5])  # (batch_size,)
input_lengths = torch.tensor([80])  # (batch_size,)
target_lengths = torch.tensor([5])  # (batch_size,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0)
print(loss.item())