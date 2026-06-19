import torch
import torch.nn.functional as F

# Example tensors for CTC loss calculation
log_probs = torch.randn(5, 8, 20)  # log probabilities from model output
targets = torch.tensor([1, 2, 3, 4, 5])  # ground truth labels
input_lengths = torch.tensor([8] * 5)  # lengths of input sequences
target_lengths = torch.tensor([5] * 5)  # lengths of target sequences

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)
print(loss.item())