import torch
import torch.nn as nn

# Define an LSTMCell
lstm_cell = nn.LSTMCell(input_size=10, hidden_size=20)

# Input data (batch_size, input_size)
input_data = torch.randn(5, 10)

# Hidden state and cell state initialization (batch_size, hidden_size)
hidden_state = torch.zeros(5, 20)
cell_state = torch.zeros(5, 20)

# Forward pass through the LSTMCell
new_hidden_state, new_cell_state = lstm_cell(input_data, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)