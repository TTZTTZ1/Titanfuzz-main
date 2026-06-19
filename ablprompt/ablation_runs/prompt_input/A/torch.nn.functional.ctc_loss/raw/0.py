import torch
import torch.nn.functional as F

# Example inputs for CTC loss
log_probs = torch.randn(5, 8, 20)  # shape: (time, batch, output_dim)
targets = torch.tensor([1, 2, 3, 4, 5])  # shape: (batch,)
input_lengths = torch.tensor([8] * 5)  # shape: (batch,)
target_lengths = torch.tensor([5] * 5)  # shape: (batch,)

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, reduction='mean')
print(loss.item())