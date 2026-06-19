import torch

# Define the model parameters
input_size = 10
hidden_size = 20

# Initialize the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
batch_size = 5
input_tensor = torch.randn(batch_size, input_size)
h_0 = torch.zeros(batch_size, hidden_size)
c_0 = torch.zeros(batch_size, hidden_size)

# Process the input through the LSTMCell
h_1, c_1 = lstm_cell(input_tensor, (h_0, c_0))

print("Hidden State:", h_1)
print("Cell State:", c_1)