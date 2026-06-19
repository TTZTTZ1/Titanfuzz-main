import torch
import torch.nn.functional as F

# Example inputs for CTC Loss
log_probs = torch.randn(5, 10, requires_grad=True)  # (time, batch_size, num_classes)
targets = torch.tensor([1, 2, 3, 4])  # (batch_size,)
input_lengths = torch.tensor([5])  # (batch_size,)
target_lengths = torch.tensor([4])  # (batch_size,)

# Call the CTC Loss function
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, reduction='mean')

print(loss)