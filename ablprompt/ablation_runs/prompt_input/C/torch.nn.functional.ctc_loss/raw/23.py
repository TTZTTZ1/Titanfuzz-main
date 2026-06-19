import torch
import torch.nn.functional as F

# Example log probabilities tensor (batch_size=3, seq_length=5, alphabet_size=8)
log_probs = torch.randn(5, 3, 8).log_softmax(dim=-1)

# Example target sequences (batch_size=3, max_seq_length=4)
targets = torch.tensor([[1, 2, 3], [2, 3], [1]])

# Example input lengths (batch_size=3)
input_lengths = torch.tensor([5, 5, 5])

# Example target lengths (batch_size=3)
target_lengths = torch.tensor([3, 2, 1])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(loss.item())