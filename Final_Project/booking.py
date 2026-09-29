# Responsibility: Reserving and returning library items.

class Booking:
    def __init__(self, booking_id, member, item):
        if not item.available:
            raise ValueError(
                f"'{item.title} is not available"
            )

        self.booking_id = booking_id
        self.member = member
        self.item = item
        self.active = True

        item.available = False

