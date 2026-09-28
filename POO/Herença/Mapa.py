class Mapa:
    def __init__(self, titulo, legenda, escala):
        self.titulo = titulo
        self.legenda = legenda
        self.escala = escala

    def __str__(self):
        return f'Titulo: {self.titulo} Legenda: {self.legenda} Escala: {self.escala}'

class MapaTopografico(Mapa):
    def __init__(self, titulo, legenda, escala, curva_de_nivel):
        super().__init__(titulo, legenda, escala)
        self.curva_de_nivel = curva_de_nivel

    def __str__(self):
        return f'Titulo: {self.titulo} Legenda: {self.legenda} Escala: {self.escala} Curva de Nível: {self.curva_de_nivel}'


mp = MapaTopografico("Meu primeiro mapinha topografico",
                     "mapa de localização", "1:1000",
                     "90º")
print(mp)