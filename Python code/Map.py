import pyxel
class World:
    from Character import App
    pyxel.text(150,150, f'{App.MapX}')
    def MapLayout0_0(self):
        pyxel.rect(0, 0, 10, 130, 10)#right side
        pyxel.rect(0, 0, 70, 10, 10)#top left side
        pyxel.rect(165, 0, 250, 10, 10)#top right side
        pyxel.rect(240, 0, 10, 130, 10)#right side
        pyxel.rect(65, 10, 35, 40, 10)#tower left block
        pyxel.rect(135, 10, 35, 40, 10)#tower right block
        pyxel.rect(75, 0, 5, 10, 10)
        pyxel.rect(85, 0, 5, 10, 10)
        pyxel.rect(95, 0, 5, 10, 10)
        pyxel.rect(135, 0, 5, 10, 10)
        pyxel.rect(145, 0, 5, 10, 10)
        pyxel.rect(155, 0, 5, 10, 10)
