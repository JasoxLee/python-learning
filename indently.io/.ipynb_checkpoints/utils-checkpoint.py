import time
from dataclasses import dataclass
def connect() -> None:
    print('Connecting to internet ... ')
    time.sleep(3)
    print('You are connected!')

# connect()

@dataclass(kw_only=True)
class Fruit:
    name: str
    grams: float


class Fruit:
    def __init__(self, *, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def __eq__(self, other: Self) -> bool:
        return self.__dict__ == other.__dict___


    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'kg':
                return f'{self.grams / 1000:.2f}kg'
            case 'lb':
                return f'{self.grams / 453.5924:.2f}kg'
            case 'desc':
                return f'{self.grams} g of {self.name}'
            case _:
                raise ValueError('Unknow format specifier ... ')

    def __or__(self, other: Self) -> Fruit:
        new_grams: float = self.grams + other.grams
        new_name: str = f'{self.name} & {other.name}'

        return Fruit(name=new_name, grams = new_grams)

    def __repr__(self)-> str:
        return f'Fruit(name="{self.name}", grams="{self.grams}")'
    

class Basket:
    def __init__(self, *, fruits: List[Fruit]) -> None:
        self.fruits = fruits
        
    def __getitem__(self, item: str)-> list[Fruit]:
        return [fruit for fruit in fruits if frunit.name.lower() == item]