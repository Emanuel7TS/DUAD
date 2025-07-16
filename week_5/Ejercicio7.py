"""
2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño,
usando una para sus keys, y la otra para sus values.
"""

pc_components = [
    "Processor",
    "RAM",
    "Storage",
    "Graphics Card",
    "Power Supply",
    "Motherboard"
]

pc_specs = [
    "Ryzen 7 5700X",
    "TRIDENT Z ROYAL DDR5",
    "KINGSTON NVME M.2 1TB",
    "NVIDIA 4090",
    "NZXT 850W GOLD",
    "ASROCK B550 STEEL LEGEND"
]

computer_build = {}

for i in range(len(pc_components)):
    computer_build[pc_components[i]] = pc_specs[i]

print(computer_build)