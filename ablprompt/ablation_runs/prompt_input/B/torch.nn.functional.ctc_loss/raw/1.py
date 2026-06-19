```python
import torch
import torch.nn.functional as F

# Example log probabilities tensor (batch_size=3, sequence_length=5, alphabet_size=4)
log_probs = torch.tensor([[[0.1, 0.2, 0.3, 0.4],
                           [0.5, 0.6, 0.7, 0.8],
                           [0.9, 1.0, 0.1, 0.2],
                           [0.3, 0.4, 0.5, 0.6],
                           [0.7, 0.8, 0.9, 1.0]],
                          [[0.2, 0.3, 0.4, 0.5],
                           [0.6, 0.7, 0.8, 0.9],
                           [0.1, 0.2, 0.3, 0.4],
                           [0.5, 0.6, 0.7, 0.8],
                           [0.9, 1.0, 0.1, 0.2]],
                          [[0.3, 0.4, 0.5, 0.6],
                           [0.7, 0.8, 0.9, 1.0],
                           [0.2, 0.3, 0.4, 0.5],
                           [0.6, 0.7, 0.8, 0.9],
                           [0.1, 0.2, 0.3, 0.4]]])

# Example target sequences tensor (batch_size=3, sequence_length=4)
targets = torch.tensor([[1, 2, 3, 0],  # 0 is the blank label
                        [2, 3, 0, 0],
                        [3, 0, 0, 0]])

# Example input lengths tensor (batch_size=3)
input_lengths = torch.tensor([5, 5, 5])

# Example target lengths tensor (batch_size=3)
target_lengths = torch.tensor([4, 2, 1])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print("CTC Loss:", loss.item())