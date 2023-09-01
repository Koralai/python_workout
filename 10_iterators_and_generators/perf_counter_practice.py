from time import perf_counter

t1_start = perf_counter()

msg = input("Type a message: ")

t1_stop = perf_counter()

t_elapsed = t1_stop - t1_start

print(f"You spent {t_elapsed:.2f} seconds typing.")
