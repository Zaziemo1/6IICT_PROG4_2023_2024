lengte_m = "1.8" # Lengte opgegeven door gebruiker.

try:
    lengte_cm = int(lengte_m)*100
except ValueError:
    "TODO: voeg hier code toe om het probleem op te lossen."
    lengte_cm = float(lengte_m)*100

print(f"Je bent {lengte_cm} centimeter lang.")