import models, interfaces
import persistence

def main():

    fm = models.FinanceManager()

    c1 = fm.add_category("food")
    c2 = fm.add_category("gas")
    c3 = fm.add_category("internet")

    m1 = fm.add_movement("nachos",4500,"expense",c1)
    m2 = fm.add_movement("car",10000,"expense",c2)
    m3 = fm.add_movement("claro",25000,"expense",c3)
    m4 = fm.add_movement("motorcicle",10000,"income",c2)

    c1.name = "fast_food"

    for cat in fm.categories.values():
        print(cat.name)
    for mov in fm.movements:
        print(f"{mov.name} {mov.value} {mov.type} {mov.category.name}")


    persistence.store_categories(fm.categories)

if __name__ == "__main__":
    main()