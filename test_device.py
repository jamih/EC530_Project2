import device_reader

def test_therm1():
    result = device_reader.json_read("therm1.json")
    assert result == 1

