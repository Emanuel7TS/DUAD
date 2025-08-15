# Ejercicios Extra sobre Diccionarios  ✔



"""
1. Dada una lista de ventas con la siguiente información:
`date`
`customer_email`
`items`
Y cada item teniendo la siguiente información:
`name`
`upc`
`unit_price`
Cree un diccionario que guarde el total de ventas de cada UPC
"""

sales_list = [
    {
        "date": "2025-06-24",
        "customer_email": "emanuel@compra.com",
        "items": [
            {"name": "Ryzen 7 5700X", "upc": "1111", "unit_price": 250.0},
            {"name": "Kingston NVMe 1TB", "upc": "2222", "unit_price": 90.0}
        ]
    },
    {
        "date": "2025-06-24",
        "customer_email": "alek@compra.com",
        "items": [
            {"name": "Ryzen 7 5700X", "upc": "1111", "unit_price": 250.0},
            {"name": "ASUS B550M", "upc": "3333", "unit_price": 130.0}
        ]
    },
    {
        "date": "2025-06-24",
        "customer_email": "jeancarlo@compra.com",
        "items": [
            {"name": "NZXT 850W", "upc": "4444", "unit_price": 120.0},
            {"name": "Kingston NVMe 1TB", "upc": "2222", "unit_price": 90.0}
        ]
    }
]


total_sales_by_upc = {}

for sale in sales_list:
    for item in sale["items"]:
        upc = item["upc"]
        price = item["unit_price"]
        if upc in total_sales_by_upc:
            total_sales_by_upc[upc] += price
        else:
            total_sales_by_upc[upc] = price


for upc, total in total_sales_by_upc.items():
    print(f"UPC: {upc} → Total vendido: ${total:.2f}")