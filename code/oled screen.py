from machine import Pin, SoftI2C
import ssd1306
import framebuf
import time

# -------- OLED SETUP --------
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# -------- BUZZER SETUP --------
buzzer = Pin(25, Pin.OUT)

# -------- BUZZER FUNCTION --------
def beep(t=0.12):
    buzzer.on()
    time.sleep(t)
    buzzer.off()

# -------- BIG TEXT FUNCTION --------
def draw_big_text(oled, text, x, y, scale=3):
    for i, char in enumerate(text):
        buf = bytearray(8)
        fbuf = framebuf.FrameBuffer(buf, 8, 8, framebuf.MONO_HLSB)
        fbuf.text(char, 0, 0)

        for row in range(8):
            for col in range(8):
                if fbuf.pixel(col, row):
                    oled.fill_rect(
                        x + (i * 8 + col) * scale,
                        y + row * scale,
                        scale,
                        scale,
                        1
                    )

# -------- DISPLAY FUNCTIONS --------
def show_big(text):
    oled.fill(0)

    if text == "3" or text == "2" or text == "1":
        draw_big_text(oled, text, 48, 16, 4)   # moved lower
    elif text == "GO":
        draw_big_text(oled, text, 18, 16, 4)   # bigger GO
    else:
        draw_big_text(oled, text, 20, 18, 2)

    oled.show()

# -------- MAIN LOOP --------
while True:
    show_big("3")
    beep()
    time.sleep(0.7)

    show_big("2")
    beep()
    time.sleep(0.7)

    show_big("1")
    beep()
    time.sleep(0.7)

    show_big("GO")
    beep(0.1)
    time.sleep(0.1)
    beep(0.2)
    time.sleep(1.5)

    oled.fill(0)
    oled.show()
    time.sleep(2)