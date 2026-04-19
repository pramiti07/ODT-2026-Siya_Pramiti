from machine import Pin, SoftI2C, PWM
import ssd1306
import framebuf
import time

# -------- OLED SETUP --------
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# -------- BUZZER SETUP --------
buzzer = Pin(25, Pin.OUT)

# -------- SERVO SETUP --------
servo = PWM(Pin(12), freq=50)

# -------- SERVO FUNCTION --------
def set_angle(angle):
    duty = int((angle / 180) * 75 + 40)
    servo.duty(duty)

# original position
REST = 140

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

# -------- DISPLAY FUNCTION --------
def show_big(text):
    oled.fill(0)

    if text == "3" or text == "2" or text == "1":
        draw_big_text(oled, text, 48, 16, 4)
    elif text == "GO":
        draw_big_text(oled, text, 18, 16, 4)

    oled.show()

# -------- FLASH EFFECT --------
def flash():
    oled.fill(1)
    oled.show()
    time.sleep(0.08)
    oled.fill(0)
    oled.show()
    time.sleep(0.08)

# -------- INITIAL SERVO POSITION --------
set_angle(REST)
time.sleep(1)

# -------- COUNTDOWN --------
show_big("3")
beep()
time.sleep(0.6)
flash()

show_big("2")
beep()
time.sleep(0.6)
flash()

show_big("1")
beep()
time.sleep(0.6)
flash()

show_big("GO")
beep(0.1)
time.sleep(0.1)
beep(0.2)
time.sleep(1)

# -------- SERVO MOVE ONCE --------
set_angle(0)

# wait 5 seconds
time.sleep(5)

# -------- RETURN TO ORIGINAL --------
set_angle(REST)

# clear screen
oled.fill(0)
oled.show()