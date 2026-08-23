import board
from kmk.kmk_keyboard import KMKKeyboard, DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

# 1. Hardware Pin Definitions
keyboard.row_pins = (
    board.GP16,  # Row 0
    board.GP17,  # Row 1
    board.GP18,  # Row 2
    board.GP19,  # Row 3
    board.GP20,  # Row 4
)

keyboard.col_pins = (
    board.GP15,  # Column 0
    board.GP14,  # Column 1
    board.GP13,  # Column 2
    board.GP12,  # Column 3
    board.GP11,  # Column 4
    board.GP10,  # Column 5
    board.GP09,  # Column 6
    board.GP08,  # Column 7
    board.GP07,  # Column 8
    board.GP06,  # Column 9
    board.GP05,  # Column 10
    board.GP04,  # Column 11
    board.GP03,  # Column 12
    board.GP02,  # Column 13
)

# 2. Matrix Properties
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 3. Keymap Definition (5 Rows x 14 Columns)
# Replace KC.TRNS or dummy keys below with your preferred layout keys.
# Use KC.NO for any grid intersections that don't have a physical switch installed.
keyboard.keymap = [
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.TRNS,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.UP,   KC.RSFT, KC.TRNS,
        KC.LCTL, KC.LGUI, KC.LALT, KC.TRNS, KC.SPC,  KC.TRNS, KC.SPC,  KC.TRNS, KC.RALT, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS,
    ]
]

if __name__ == '__main__':
    keyboard.go()
