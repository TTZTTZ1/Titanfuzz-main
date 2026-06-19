import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 8, 20)  # (time_steps, batch_size, num_classes)
targets = torch.tensor([1, 2, 3, 4, 5])  # (batch_size,)
input_lengths = torch.full((1,), log_probs.size(0))  # (batch_size,)
target_lengths = torch.tensor([len(targets)])  # (batch_size,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0)
print(loss.item())