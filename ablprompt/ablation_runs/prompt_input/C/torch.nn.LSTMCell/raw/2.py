import torch

# Define the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden states
input_tensor = torch.randn(1, 10)  # Batch size of 1, input size of 10
hidden_state = torch.zeros(1, 20)   # Hidden state size of 20
cell_state = torch.zeros(1, 20)     # Cell state size of 20

# Forward pass through the LSTMCell
new_hidden_state, new_cell_state = lstm_cell(input_tensor, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)