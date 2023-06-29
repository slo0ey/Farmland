if __name__ == "__main__":
    def test_display():
        import pygame

        pygame.display.set_mode((1600, 900))
        pygame.display.set_caption('Farmland! - Testing...')

    def test_io():
        from util.io import save_json, load_json

        obj = {
            "name": "Object-0",
            "value": [1, 2, 3]
        }

        save_json(data=obj, file_name='test_obj')

        loaded = load_json(file_name='test_obj')
        print(loaded)

    def test_pytmx():
        from pytmx import load_pygame, TiledTileLayer

        farm = load_pygame('./asset/map/farm.tmx')
        for layer in farm.layers:
            print(type(layer))

    test_display()
    test_pytmx()
