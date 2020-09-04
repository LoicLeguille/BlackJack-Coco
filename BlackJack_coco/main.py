# art from Kenney.nl

from gui import *

# main function
def main():
    root = Tk()
    g = Gui(root)
    g.pack(fill = BOTH, expand = 'yes')
    root.mainloop()

# run game
if __name__ == '__main__':
    main()
