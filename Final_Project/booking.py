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

    def cancel(self):
        if not self.active:
            raise ValueError(
                "This booking is already cancelled."
            )

        self.active = False
        self.item.available = True

    def __str__(self):
        status = "Active" if self.active else "Cancelled"

        return (
            f"Booking {self.booking_id}: "
            f"{self.member.name} - "
            f"{self.item.title} - {status}"
        )


# book = Booking()