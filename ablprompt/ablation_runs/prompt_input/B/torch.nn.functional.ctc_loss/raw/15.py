import torch
import torch.nn.functional as F

# Example log probabilities tensor (batch_size=3, time_steps=5, num_classes=8)
log_probs = torch.randn(5, 3, 8).log_softmax(dim=-1)

# Example target sequences (batch_size=3, max_target_length=7)
targets = torch.tensor([[1, 2, 3], [4, 5], [6]])

# Example lengths of input sequences (batch_size=3)
input_lengths = torch.tensor([5, 5, 5])

# Example lengths of target sequences (batch_size=3)
target_lengths = torch.tensor([3, 2, 1])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(f"CTC Loss: {loss.item()}")