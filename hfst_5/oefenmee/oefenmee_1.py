class Hond:
    naam = "Mohammed sumbul"
    massa = "1000 kg"

    def miauw(self):
        print(f"{Hond.naam} zegt blaf")

hond = Hond()
huisdier = Hond()

print(hond.naam, hond.massa)
print(huisdier.naam, huisdier.massa)