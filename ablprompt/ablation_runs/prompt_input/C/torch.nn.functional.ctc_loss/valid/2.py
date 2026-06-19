import torch
import torch.nn.functional as F

# Example data
T, N, C = 5, 3, 8  # Input length, batch size, alphabet size
S = 4  # Average target length
log_probs = torch.randn(T, N, C).log_softmax(dim=2)  # Log probabilities
targets = torch.randint(1, C - 1, (N, S))  # Target sequences, excluding blank
input_lengths = torch.full((N,), T, dtype=torch.long)  # All inputs have the same length
target_lengths = torch.full((N,), S, dtype=torch.long)  # All targets have the same length

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(f"CTC Loss: {loss.item()}")