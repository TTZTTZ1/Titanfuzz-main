import torch
import torch.nn as nn

# Define the GRUCell
gru_cell = nn.GRUCell(input_size=10, hidden_size=20)

# Initialize input and hidden state
input_tensor = torch.randn(5, 10)  # Sequence length of 5, feature size of 10
hidden_state = torch.zeros(5, 20)   # Batch size of 5, hidden size of 20

# Process the sequence
for i in range(input_tensor.size(0)):
    hidden_state = gru_cell(input_tensor[i], hidden_state)

print(hidden_state)