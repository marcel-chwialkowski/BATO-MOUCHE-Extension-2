import marceltransport
import time 

start = time.time()
marceltransport.otp_calculate_route_time_new((48.86107, 2.364267), (48.84900, 2.330620))
end = time.time()
print(f"Time taken: {end - start}") #this takes way longer than it should #like 0.2 seconds