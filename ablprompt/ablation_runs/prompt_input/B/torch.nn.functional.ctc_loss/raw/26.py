import torch
import torch.nn.functional as F

# Example log probabilities tensor (batch_size=2, input_length=5, alphabet_size=3)
log_probs = torch.tensor([[[0.1, 0.2, 0.7],
                           [0.6, 0.2, 0.2],
                           [0.1, 0.8, 0.1],
                           [0.4, 0.1, 0.5],
                           [0.7, 0.1, 0.2]],
                          [[0.2, 0.7, 0.1],
                           [0.1, 0.3, 0.6],
                           [0.8, 0.1, 0.1],
                           [0.2, 0.5, 0.3],
                           [0.1, 0.4, 0.5]]])

# Example target sequences tensor (batch_size=2, sequence_length=3)
targets = torch.tensor([[1, 2, 0],  # 0 is the blank label
                        [2, 0, 1]])

# Example lengths of each input sequence
input_lengths = torch.tensor([5, 5])

# Example lengths of each target sequence
target_lengths = torch.tensor([3, 2])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(f"CTC Loss: {loss.item()}")