import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 10, requires_grad=True)  # shape: (seq_len, batch_size, num_classes)
targets = torch.tensor([1, 2, 3])  # shape: (batch_size,)
input_lengths = torch.tensor([5])  # shape: (batch_size,)
target_lengths = torch.tensor([3])  # shape: (batch_size,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0)

print(loss)