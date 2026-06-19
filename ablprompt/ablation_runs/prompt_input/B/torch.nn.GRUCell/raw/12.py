import torch
from torch.nn import GRUCell

# Initialize the GRUCell
gru_cell = GRUCell(input_size=10, hidden_size=20)

# Create random input and hidden state
input_tensor = torch.randn(5, 10)  # Sequence length of 5, feature dimension of 10
hidden_state = torch.randn(5, 20)  # Sequence length of 5, hidden dimension of 20

# Update the hidden state step-by-step
for i in range(input_tensor.size(0)):
    hidden_state = gru_cell(input_tensor[i], hidden_state)

print(hidden_state)