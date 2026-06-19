import torch
import torch.nn as nn

# Define an LSTMCell
lstm_cell = nn.LSTMCell(input_size=10, hidden_size=20)

# Create input and hidden state
input_data = torch.randn(5, 10)  # (sequence_length, batch_size, input_size)
hidden_state = torch.randn(5, 20)  # (batch_size, hidden_size)
cell_state = torch.randn(5, 20)   # (batch_size, hidden_size)

# Forward pass through LSTMCell
new_hidden_state, new_cell_state = lstm_cell(input_data, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state.shape)
print("New Cell State:", new_cell_state.shape)