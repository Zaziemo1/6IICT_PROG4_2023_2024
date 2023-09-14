# Maak gebruik van onderstaande dictionary gevuld met laptop-info.
laptop_korneel = {
    "serial": "R44508ZH1",
    "model": {"id": 8, "name": "L390", "touch": True},
    "assigned_to": {"username": "VAKO190900", "name": "Korneel Valo"},
    "category": {"id": 4, "status": "laptopMETtouch"},
    "manufacturer": {"id": 2, "name": "LENOVO"},
    "supplier": "???",
    "supplier_2": "bol.com"
}
laptop_korneel.pop("supplier_2")

laptop_korneel["supplier"] = "signpost"
laptop_korneel["status"] = "deployed"




print(laptop_korneel)