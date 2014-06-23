from .census import Census
from .dartmouth import Dartmouth
from .ers import Ers

assert all((Census, Dartmouth, Ers))  # pyflakes be quiet
