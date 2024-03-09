import pickle

def load_model(filename):
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    return model

# Example usage:
# Load the saved model parameters from 'my_model.pkl'
my_model = load_model('my_model.pkl')
print("successfully loaded the model")

