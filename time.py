import time

# Get the current time
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Time: {current_time}")

# Pause for 3 seconds
print("Pausing for 3 seconds...")
time.sleep(3)
print("Done waiting!")

# Measure execution time
start = time.time()
for i in range(1000000):
    pass
end = time.time()

print(f"Time taken to execute loop: {end - start:.6f} seconds")
