# imports for time myo, time interval, saving and plotting data
import myo
from myo.utils import TimeInterval
import csv
import matplotlib.pyplot as plt
 
 
class Listener(myo.DeviceListener):
 
    def __init__(self):
        # the time in interval is in seconds
        self.interval = TimeInterval(None, 0.05)
        # define variables for saving the data
        self.orientation_data = []
        self.emg_data = []
        self.rssi = None
 
    def on_connected(self, event):
        # Request the signal strength from the device
        event.device.request_rssi()
        print("Hello, {}!".format(event.device_name))
        # Enable streaming the emg values
        event.device.stream_emg(True)
 
    # If received signal strength changes print information about it
    def on_rssi(self, event):
        self.rssi = event.rssi
        print("received signal strength = {}".format(self.rssi))
 
    def on_emg(self, event):
        # Save only after the interval passed
        if not self.interval.check_and_reset():
            return
        self.emg_data.append(event.emg)
 
    def on_orientation(self, event):
        if not self.interval.check_and_reset():
            return
        self.orientation_data.append(event.orientation)
 
    def save_emg_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.emg_data)
        print(f'Data saved to {filename}.')
 
    def save_orientation_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            # make a header for the csv file
            fieldnames = ['w', 'x', 'y', 'z']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.orientation_data:
                writer.writerow({'w': row[0], 'x': row[1], 'y': row[2], 'z': row[3]})
        print(f'Data saved to {filename}.')
 
    def plot_emg_data(self):
        fig, axs = plt.subplots(8, 1, figsize=(10, 20), sharex=True)
        fig.suptitle('EMG Data')
        # plot 8 plots: each for every sensor
        for i in range(8):
            axs[i].plot([sample[i] for sample in self.emg_data])
            axs[i].set_ylabel(f'Channel {i + 1}')
 
        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        plt.show()
 
 
if __name__ == '__main__':
    myo.init()
    hub = myo.Hub()
    listener = Listener()
    # As long as the program runs collect data
    # When the program is stopped collect the data and plot emg data
    try:
        print("Collecting data. Please perform gestures...")
        while hub.run(listener.on_event, 500):
            pass
    except KeyboardInterrupt:
        pass
    finally:
        hub.stop()
        # Save the data to a CSV file
        listener.save_emg_to_csv('csv/myo_emg_data.csv')
        listener.save_orientation_to_csv('csv/myo_orient_data.csv')
 
        # Create a plot
        listener.plot_emg_data()