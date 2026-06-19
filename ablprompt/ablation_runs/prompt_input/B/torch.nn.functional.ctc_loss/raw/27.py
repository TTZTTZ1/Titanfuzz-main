import torch
import torch.nn.functional as F

# Example log probabilities tensor (batch_size=2, sequence_length=5, alphabet_size=3)
log_probs = torch.tensor([[[0.1, 0.2, 0.7], [0.6, 0.2, 0.2], [0.1, 0.8, 0.1], [0.4, 0.3, 0.3], [0.2, 0.5, 0.3]],
                           [[0.7, 0.1, 0.2], [0.2, 0.6, 0.2], [0.1, 0.2, 0.7], [0.3, 0.3, 0.4], [0.5, 0.2, 0.3]]])

# Example target sequences tensor (batch_size=2, sequence_length=3)
targets = torch.tensor([[1, 2, 0],
                        [0, 1, 2]])

# Example input lengths tensor (batch_size=2)
input_lengths = torch.tensor([5, 5])

# Example target lengths tensor (batch_size=2)
target_lengths = torch.tensor([3, 3])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean', zero_infinity=False)

print(f"CTC Loss: {loss.item()}")