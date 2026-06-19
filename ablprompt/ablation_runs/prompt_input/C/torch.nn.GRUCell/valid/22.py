import torch
import torch.nn as nn

# Define the GRUCell
gru_cell = nn.GRUCell(input_size=10, hidden_size=20)

# Initialize input and hidden state
input_tensor = torch.randn(1, 10)  # Batch size of 1, sequence length of 1, feature dimension of 10
hidden_state = torch.randn(1, 20)   # Batch size of 1, hidden state dimension of 20

# Update the hidden state
updated_hidden_state = gru_cell(input_tensor, hidden_state)

print(updated_hidden_state)