class Banner:
    def __init__(self, message, width=0):
        self.message = message
        self.width = width
        if self.width > 9:
            self.msg_len = width
        else:
            self.msg_len = len(message)


    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f'| {' '*(self.msg_len)} |'

    def _horizontal_rule(self):
        return f'+-{'-'*(self.msg_len)}-+'

    def _message_line(self):
        if self.width < 10:
            return f"| {self.message} |"

        fit_msg = ''
        tmp_msg = self.message
        num = len(self.message) // self.width + 1
        msg_len = self.msg_len

        for i in range(num):
            if i == range(num)[-1]:
                fit_msg += f"| {tmp_msg[:msg_len].center(msg_len)} |"
                return fit_msg

            fit_msg += f"| {tmp_msg[:self.msg_len]} |\n"
            tmp_msg = tmp_msg[self.msg_len:]

        return fit_msg

# Complete this class so that the test cases shown below work as intended. You are free to add any methods or instance variables you need. However, methods prefixed with an underscore are intended for internal use and should not be called externally.
#
# You may assume that the input will always fit in your terminal window.

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 17)
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
