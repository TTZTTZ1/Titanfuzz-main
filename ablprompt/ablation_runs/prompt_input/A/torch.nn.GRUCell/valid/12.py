import torch
from torch import nn

# Initialize GRUCell
input_size = 10
hidden_size = 20
gru_cell = nn.GRUCell(input_size, hidden_size)

# Input and hidden state
input_data = torch.randn(3, input_size)  # 3 timesteps, each of size input_size
hidden_state = torch.randn(3, hidden_size)  # 3 timesteps, each of size hidden_size

# Forward pass through GRUCell
output = gru_cell(input_data, hidden_state)
print(output)