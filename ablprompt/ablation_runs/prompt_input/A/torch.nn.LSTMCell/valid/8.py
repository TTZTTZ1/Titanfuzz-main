import torch
import torch.nn as nn

# Define input size, hidden size, and batch size
input_size = 10
hidden_size = 20
batch_size = 5

# Create an instance of LSTMCell
lstm_cell = nn.LSTMCell(input_size, hidden_size)

# Initialize input data and hidden state/cell state
input_data = torch.randn(batch_size, input_size)
hidden_state = torch.zeros(batch_size, hidden_size)
cell_state = torch.zeros(batch_size, hidden_size)

# Forward pass through LSTMCell
new_hidden_state, new_cell_state = lstm_cell(input_data, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)