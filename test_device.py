import device_reader

# no errors
def test_scale1():
    result = device_reader.json_read("scale1.json")
    assert result == 0
    
# extra comma in json file 
def test_therm1():
    result = device_reader.json_read("therm1.json")
    assert result == 1

# missing type of measurement field
def test_spygh1():
    result = device_reader.json_read("spygh1.json")
    assert result == 2

# invalid data type in device ID field
def test_glu1():
    result = device_reader.json_read("glu1.json")
    assert result == 3

# negative temp in measurement
def test_therm2():
    result = device_reader.json_read("therm2.json")
    assert result == 4

# wrong unit, lb instead of mmHg
def test_oxi1():
    result = device_reader.json_read("oxi1.json")
    assert result == 5