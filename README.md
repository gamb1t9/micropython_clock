# micropython_clock
ESP32 with micropython
WSL won't work due to the fact that it can't control USB
tools required/suggested:
  ampy for listing, up- and downloading sketches
  esptool - for erasing and uploading firmware
  picocom - for serial terminal

useful commands:
  picocom /dev/ttyUSB0 -b 115200
  ampy -p /dev/ttyUSB0 get/put/ls    #rmdir won't work if it's not empty!
  esptool reset_flash || write_flash -z 0x1000 <esp32_micropython_firmware.bin>

python stuff:
  ota:
    https://github.com/RangerDigital/senko
  list stuff:
    import os
    os.listdir("your_directory_path_or_empty_for_root")
  reset board:
    import machine
    machine.reset()

misc:
  reset USB hub if ESP32 hangs (which it often does when you try something that should yield an error):
    from usb.core import find as finddev
    dev = finddev(idVendor=0x10c4, idProduct=0xea60)
    dev.reset()
    #the pyusb module is required
