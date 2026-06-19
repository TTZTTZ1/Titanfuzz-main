import torch
import torch.nn.functional as F

# Example log probabilities tensor (batch_size=3, sequence_length=5, num_classes=4)
log_probs = torch.randn(5, 3, 4).log_softmax(dim=-1)

# Example target sequences tensor (batch_size=3, max_target_length=7)
targets = torch.tensor([[1, 2], [0, 3], [1]])

# Example input lengths tensor (batch_size=3)
input_lengths = torch.tensor([5, 4, 3])

# Example target lengths tensor (batch_size=3)
target_lengths = torch.tensor([2, 1, 3])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(loss.item())