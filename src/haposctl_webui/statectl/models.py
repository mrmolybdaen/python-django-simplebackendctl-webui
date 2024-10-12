from django.db import models

# from haproxyctl import state_change


# Create your models here.
class StatectlServer(models.Model):
    """This class provides the model for a project to switch between maint and up.
    """

    # URI to haproxy status page
    proxy_url = models.CharField(max_length=256, unique=False, null=False, blank=False)
    # Authentication credentials for HAProxy backend - this is dangerous!
    proxy_user = models.CharField(max_length=256, unique=False, null=True, blank=True)
    proxy_password = models.CharField(max_length=256, unique=False, null=True, blank=True)

    # Name of the haproxy backend
    backend_name = models.CharField(max_length=16, unique=False, null=False, blank=False)
    # Name of the production server backend as provided by HAProxy
    backend_server_name = models.CharField(max_length=64, unique=True, null=False, blank=False)
    # State of production backend server
    # -1 = UNKNOWN/no information on current state
    #  0 = OK/Ready
    #  1 = MAINT
    #  2 = DOWN
    backend_server_state = models.IntegerField(default=-1)

    def __str__(self) -> str:
        return str(self.backend_name)

    def get_state(self) -> int:
        """Get the current state of the server.
        """
        return 0

    def set_maint(self) -> models.IntegerField:
        """Set state to MAINT."""
        state = self.backend_server_state
        return state

    def set_ready(self) -> models.IntegerField:
        """Set state to READY."""
        state = self.backend_server_state
        return state
