import torch
import torch.nn.functional as F

# Example usage of ctc_loss
log_probs = torch.randn(5, 8, 20)  # shape: (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3])  # shape: (batch_size,)
input_lengths = torch.tensor([8])  # shape: (batch_size,)
target_lengths = torch.tensor([3])  # shape: (batch_size,)

loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)
print(loss.item())