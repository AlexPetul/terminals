import re

from django.core.exceptions import ValidationError


class NumberValidator:
    def validate(self, password, user=None):
        if not re.findall(r"\d", password):
            raise ValidationError(
                "The password must contain at least 1 digit, 0-9.",
                code="password_no_number",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 digit, 0-9.")


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall("[A-Z]", password):
            raise ValidationError(
                "The password must contain at least 1 uppercase letter, A-Z.", code="password_no_upper"
            )

    def get_help_text(self):
        return "Your password must contain at least 1 uppercase letter, A-Z."


class LowercaseValidator:
    def validate(self, password, user=None):
        if not re.findall("[a-z]", password):
            raise ValidationError(
                "The password must contain at least 1 lowercase letter, a-z.", code="password_no_lower"
            )

    def get_help_text(self):
        return "Your password must contain at least 1 lowercase letter, a-z."


class SymbolValidator:
    def validate(self, password, user=None):
        if not re.findall(r"[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]", password):
            raise ValidationError(
                "The password must contain at least 1 symbol: " + r"()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?",
                code="password_no_symbol",
            )

    def get_help_text(self):
        return "Your password must contain at least 1 symbol: " + r"()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
