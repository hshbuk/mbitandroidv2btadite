def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global g_color, g_ctrl, g_mode, g_music, g_RGBMode
    g_color = 0
    g_ctrl = 0
    g_mode = 0
    g_music = 0
    g_RGBMode = 0
    Tinybit.RGB_Car_Program().clear()
    Tinybit.RGB_Car_Program().show()
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
    basic.show_icon(IconNames.SAD)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def Music():
    music.set_built_in_speaker_enabled(False)
    music.set_volume(127)
    if g_music == 1:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    elif g_music == 2:
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
    elif g_music == 3:
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
    elif g_music == 4:
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
    elif g_music == 5:
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    elif g_music == 6:
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
    elif g_music == 7:
        music.play_tone(494, music.beat(BeatFraction.WHOLE))
    elif g_music == 8:
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
    elif g_music == 9:
        music.play_tone(554, music.beat(BeatFraction.WHOLE))
    elif g_music == 10:
        music.play_tone(622, music.beat(BeatFraction.WHOLE))
    elif g_music == 11:
        music.play_tone(740, music.beat(BeatFraction.WHOLE))
    elif g_music == 12:
        music.play_tone(831, music.beat(BeatFraction.WHOLE))
    elif g_music == 13:
        music.play_tone(932, music.beat(BeatFraction.WHOLE))
    elif g_music == 0:
        music.set_volume(0)
def BlueCtrl():
    if g_ctrl == 1:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 255)
    elif g_ctrl == 2:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_BACK, 255)
    elif g_ctrl == 3:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_LEFT, 255)
    elif g_ctrl == 4:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RIGHT, 255)
    elif g_ctrl == 5:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, 255)
    elif g_ctrl == 6:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 255)
    elif g_ctrl == 0:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_STOP, 0)

def on_uart_data_received():
    global uartData, g_ctrl, g_music, g_color, g_RGBMode, g_mode
    uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    if uartData == "A":
        g_ctrl = 1
    elif uartData == "B":
        g_ctrl = 2
    elif uartData == "C":
        g_ctrl = 3
    elif uartData == "D":
        g_ctrl = 4
    elif uartData == "E":
        g_ctrl = 5
    elif uartData == "F":
        g_ctrl = 6
    elif uartData == "0":
        g_ctrl = 0
    elif uartData == "1":
        g_music = 1
    elif uartData == "2":
        g_music = 2
    elif uartData == "3":
        g_music = 3
    elif uartData == "4":
        g_music = 4
    elif uartData == "5":
        g_music = 5
    elif uartData == "6":
        g_music = 6
    elif uartData == "7":
        g_music = 7
    elif uartData == "8":
        g_music = 8
    elif uartData == "B1":
        g_music = 9
    elif uartData == "B2":
        g_music = 10
    elif uartData == "B3":
        g_music = 11
    elif uartData == "B4":
        g_music = 12
    elif uartData == "B5":
        g_music = 13
    elif uartData == "O":
        g_music = 0
    elif uartData == "G":
        g_color = 1
    elif uartData == "H":
        g_color = 2
    elif uartData == "I":
        g_color = 3
    elif uartData == "J":
        g_color = 4
    elif uartData == "K":
        g_color = 5
    elif uartData == "L":
        g_color = 6
    elif uartData == "M":
        g_color = 0
    elif uartData == "N":
        g_RGBMode = 1
    elif uartData == "P":
        g_RGBMode = 2
    elif uartData == "Q":
        g_RGBMode = 3
    elif uartData == "R":
        g_RGBMode = 4
    elif uartData == "W":
        g_RGBMode = 0
    elif uartData == "S":
        g_mode = 1
    elif uartData == "T":
        g_mode = 2
    elif uartData == "U":
        g_mode = 3
    elif uartData == "V":
        g_mode = 0
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

uartData = ""
g_RGBMode = 0
g_music = 0
g_mode = 0
g_ctrl = 0
g_color = 0
g_color = 0
g_ctrl = 0
g_mode = 0
g_music = 0
g_RGBMode = 0
Tinybit.RGB_Car_Program().clear()
Tinybit.RGB_Car_Program().show()
Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
basic.show_string("S")
bluetooth.set_transmit_power(7)
bluetooth.start_uart_service()

def on_forever():
    BlueCtrl()
    Music()
basic.forever(on_forever)
