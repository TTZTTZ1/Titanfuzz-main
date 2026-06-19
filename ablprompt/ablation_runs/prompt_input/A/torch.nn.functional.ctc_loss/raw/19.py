import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 8, 20)  # shape: (time steps, batch size, number of classes)
targets = torch.tensor([1, 2, 3, 4, 5])  # shape: (batch size,)
input_lengths = torch.full((1,), log_probs.size(0))  # shape: (batch size,)
target_lengths = torch.tensor([5])  # shape: (batch size,)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0)
print(f"CTC Loss: {loss.item()}")