from chat_gpt import inverse_square_root
from quake_3 import fast_inverse_square_root
from time import time
    
def on_event(callback, number):
    start = time()
    result = callback(number)
    duration = time() - start

    return result, duration

print(on_event(inverse_square_root, 123413242343242324323424342.23424902903842))
print(on_event(fast_inverse_square_root, 123413242343242324323424342.23424902903842))