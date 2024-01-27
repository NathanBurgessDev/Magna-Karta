from gpiozero import DistanceSensor

class SensorController:

    def __init__(self, in_range_cb, out_of_range_cb) -> None:
        self.sensor = DistanceSensor(echo=18, trigger=4, threshold_distance=0.2)
        self.sensor.when_in_range = in_range_cb
        self.sensor.when_out_of_range = out_of_range_cb

    def set_threshold(self, distance: float):
        self.sensor.threshold_distance = distance
