from flask import flash


def set_flash_message(message, class_='alert-success'):
    flash({"class": class_, "text": message})
