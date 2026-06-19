import torch
import torch.nn.functional as F

# Example log probabilities tensor (batch_size=2, seq_len=5, vocab_size=4)
log_probs = torch.tensor([
    [[-0.1, -0.2, -0.3, -0.4], [-0.5, -0.6, -0.7, -0.8], [-0.9, -1.0, -1.1, -1.2], [-1.3, -1.4, -1.5, -1.6], [-1.7, -1.8, -1.9, -2.0]],
    [[-2.1, -2.2, -2.3, -2.4], [-2.5, -2.6, -2.7, -2.8], [-2.9, -3.0, -3.1, -3.2], [-3.3, -3.4, -3.5, -3.6], [-3.7, -3.8, -3.9, -4.0]]
])

# Example target sequences (batch_size=2, seq_len=3)
targets = torch.tensor([[1, 2, 3], [0, 1, 2]])

# Example input lengths (batch_size=2)
input_lengths = torch.tensor([5, 5])

# Example target lengths (batch_size=2)
target_lengths = torch.tensor([3, 3])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print("CTC Loss:", loss.item())