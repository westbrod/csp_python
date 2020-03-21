import gdx 

collection = int(input(" How long would you to collect data for?"))

samples = int(input("how many samples would you want per second?"))

print(collection, samples)

gdx = gdx.gdx()
gdx.open_usb()
gdx.select_sensors()
gdx.start()



for _ in range(20):
    measurements = gdx.read()
    print(measurements)




# collection = int(input(" How long would you to collect data for? "))

# samples = int(input(" how many samples would you want per second?")

