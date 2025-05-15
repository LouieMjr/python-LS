class Banner:
    def __init__(self, message, width=0):
        self.message = message
        self.width = width

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 9 and width < len(self.message):
            self._width = width
        else:
            self._width = len(self.message)

    def _empty_line(self):
        return f'| {' ' * self.width} |'

    def _horizontal_rule(self):
        return f'+-{'-' * self.width}-+'

    def _message_line(self):
        if self.width >= len(self.message):
            return f"| {self.message} |"

        chunk = ''
        fit_msg = ''

        msg_len = self.width
        word_list = self.message.split()

        for i, word in enumerate(word_list):

            if len(chunk + word) >= msg_len:
                fit_msg += f"| {chunk.center(msg_len)} |\n"
                chunk = ''

            # if its the last word in word_list
            if i == len(word_list) - 1:
                fit_msg += f"| {word.center(msg_len)} |"

            elif word != word_list[-1]:
                chunk += ' ' + word

        return fit_msg

# Complete this class so that the test cases shown below work as intended. You are free to add any methods or instance variables you need. However, methods prefixed with an underscore are intended for internal use and should not be called externally.
#
# You may assume that the input will always fit in your terminal window.

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 40)
print(banner)

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+
