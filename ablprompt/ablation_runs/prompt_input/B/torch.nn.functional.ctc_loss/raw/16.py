import torch
import torch.nn.functional as F

# Example data
T, N, C = 5, 3, 8  # Input length, batch size, alphabet size
S = 4  # Maximum target length

# Generate random log probabilities
log_probs = torch.randn(T, N, C).log_softmax(dim=2)

# Generate random target sequences
targets = torch.randint(1, C - 1, (N, S))

# Generate random input lengths
input_lengths = torch.randint(1, T + 1, (N,))

# Generate random target lengths
target_lengths = torch.randint(1, S + 1, (N,))

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean', zero_infinity=False)

print(loss.item())