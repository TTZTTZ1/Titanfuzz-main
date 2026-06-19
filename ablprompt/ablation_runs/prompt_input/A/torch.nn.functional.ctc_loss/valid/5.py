import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.tensor([[[0.1, 0.6, 0.3], [0.05, 0.8, 0.15]], [[0.2, 0.7, 0.1], [0.1, 0.9, 0.0]]])
targets = torch.tensor([[1, 2], [0, 2]])
input_lengths = torch.tensor([2, 2])
target_lengths = torch.tensor([2, 1])

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)

print(f"CTC Loss: {loss.item()}")