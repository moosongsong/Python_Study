from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


struct_val = InventoryItem("candy", 2.22, 10)
struct_val_q = InventoryItem("candy", 2.22)

print(struct_val)

print(struct_val_q)

print(dir(struct_val))

print(dir(struct_val_q))