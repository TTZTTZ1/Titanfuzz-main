import torch
import torch.nn.functional as F

# Example usage of ctc_loss
log_probs = torch.randn(5, 80, 26).log_softmax(2)  # Log probabilities from your model
targets = torch.tensor([1, 2, 3, 4, 5])  # Ground truth labels
input_lengths = torch.tensor([80])  # Lengths of input sequences
target_lengths = torch.tensor([5])  # Lengths of target sequences

loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)
print(loss.item())