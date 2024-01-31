import json

pad = "hfst_4//oef2_kluizen.json"
kluizen = {}

with open(pad, "r") as fp:
    kluizen = json.load(fp)