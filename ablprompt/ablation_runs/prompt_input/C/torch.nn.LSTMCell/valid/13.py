import torch

# Define the dimensions
input_size = 10
hidden_size = 20

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = torch.zeros(1, hidden_size)
cell_state = torch.zeros(1, hidden_size)

# Forward pass through the LSTMCell
new_hidden_state, new_cell_state = lstm_cell(input_tensor, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)