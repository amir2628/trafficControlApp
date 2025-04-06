from django.db import models

# Create your models here.

class TrafficLightConfiguration(models.Model):
    # Duration of each traffic light phase in seconds.
    red_duration = models.PositiveIntegerField(default=30, verbose_name="Red Duration (seconds)")
    yellow_duration = models.PositiveIntegerField(default=5, verbose_name="Yellow Duration (seconds)")
    green_duration = models.PositiveIntegerField(default=25, verbose_name="Green Duration (seconds)")
    
    # Current state of the traffic light: options are "Red", "Yellow", "Green"
    current_state = models.CharField(
        max_length=10,
        default="Red",
        choices=[("Red", "Red"), ("Yellow", "Yellow"), ("Green", "Green")],
        verbose_name="Current State"
    )
    
    # Auto-updated timestamp when the configuration is modified
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Traffic Light - {self.current_state}"

    def next_state(self):
        """
        Simulate the next state of the traffic light.
        The logic is:
         - If the current state is Red, the next state will be Green.
         - If the current state is Green, the next state will be Yellow.
         - If the current state is Yellow, the next state will be Red.
        """
        if self.current_state == "Red":
            return "Green"
        elif self.current_state == "Green":
            return "Yellow"
        elif self.current_state == "Yellow":
            return "Red"
        else:
            return "Red"
