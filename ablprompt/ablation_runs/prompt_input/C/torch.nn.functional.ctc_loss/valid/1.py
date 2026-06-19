import torch
import torch.nn.functional as F

# Example data
batch_size = 4
sequence_length = 5
alphabet_size = 10
num_sequences = [3, 4, 2, 5]

# Generate random log probabilities
log_probs = torch.randn(sequence_length, batch_size, alphabet_size).log_softmax(dim=-1)

# Generate random target sequences
targets = torch.randint(1, alphabet_size - 1, (batch_size, max(num_sequences)))

# Generate input lengths
input_lengths = torch.tensor(num_sequences)

# Generate target lengths
target_lengths = torch.tensor([len(tgt) for tgt in targets])

# Compute CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean')

print(f"CTC Loss: {loss.item()}")