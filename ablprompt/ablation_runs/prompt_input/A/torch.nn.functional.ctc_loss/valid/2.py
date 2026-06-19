import torch
import torch.nn.functional as F

# Example input tensors for CTC loss calculation
log_probs = torch.tensor([[-0.1, -0.2, -0.3],
                           [-0.4, -0.5, -0.6],
                           [-0.7, -0.8, -0.9]], dtype=torch.float32)
targets = torch.tensor([0, 1], dtype=torch.long)
input_lengths = torch.tensor([3], dtype=torch.int)
target_lengths = torch.tensor([2], dtype=torch.int)

# Calculate CTC loss
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths, reduction='sum')
print(loss.item())