import torch
import torch.nn.functional as F

# Example inputs for CTC Loss
log_probs = torch.randn(5, 8, 20)  # shape: (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3, 4, 5])  # shape: (batch_size,)
input_lengths = torch.tensor([8] * 5)  # shape: (batch_size,)
target_lengths = torch.tensor([5] * 5)  # shape: (batch_size,)

# Apply CTC Loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0)
print(loss.item())