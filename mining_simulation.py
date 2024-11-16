import random
import hashlib
import time

nonce = 1234

def generate():
    random_int = random.randint(1, 10000000000)
    return random_int, hashlib.sha256(str(random_int).encode()).hexdigest()

def simulate():
    block_height = 0
    prev_hash = 0
    difficulty = 2
    start_time = time.time()
    while True:
        generated_int, generated_hash = generate()
        if generated_hash.startswith("0" * difficulty):
            end_time = time.time()
            print("Výška bloku: ", block_height)
            print("Hash bloku: ", generated_hash)
            print("Hash předchozího: ", prev_hash)
            print("Data RAW: ", generated_int)
            print("Nonce: ", block_height * nonce)
            print("Obtížnost: ", difficulty)

            print(f"Čas těžby: {end_time - start_time} s")

            difficulty += 1
            prev_hash = generated_hash
            block_height += 1

            if difficulty == 7:
                return
            
            start_time = time.time()
        
simulate()

