if __name__ == "__main__":
    from util.io import save_json, load_json

    obj = {
        "name": "Object-0",
        "value": [1, 2, 3]
    }

    save_json(data=obj, file_name='test_obj')

    loaded = load_json(file_name='test_obj')
    print(loaded)
