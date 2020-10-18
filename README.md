擦除

```
esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART erase_flash
```

烧录

```
esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 micropython_0fd0eb00a_esp32_idf4.x_ble_camera.bin
```

